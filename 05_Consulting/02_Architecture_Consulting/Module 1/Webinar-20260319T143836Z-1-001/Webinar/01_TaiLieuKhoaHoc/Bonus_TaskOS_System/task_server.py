import os
import re
import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import webbrowser

# ============================================================
# ANTIGRAVITY TASK OS — Core Engine v5.0 (REST API)
# ============================================================
# Endpoints:
#   GET  /tasks                  → Lấy tất cả tasks (JSON)
#   GET  /tasks?type=agent       → Filter theo type
#   GET  /tasks?project=5balance → Filter theo project
#   GET  /tasks?done=false       → Filter theo trạng thái
#   GET  /tasks?owner=AI_RM      → Filter theo agent owner
#   POST /tasks                  → Tạo task mới
#   POST /update                 → Re-scan toàn bộ
#   POST /delete-task            → Xóa task
#   POST /update-task            → Sửa tên task
# ============================================================

# ============================================================
# ANTIGRAVITY TASK OS — Core Engine v4.1 (Edit + Delete)
# ============================================================
# Chạy: python task_server.py
# Dashboard: http://localhost:8000/dashboard.html
# ============================================================

PORT = 8000
MAX_DEPTH = 5

SKIP_DIRS = {
    # Hệ thống & build
    '.gemini', '.agent', '.git', '__pycache__',
    'node_modules', '.vscode', '.claude', '.agents',
    # Task OS
    '_task-os', 'antigravity-task-os', 'sandbox',
    # Archive / cũ / tạm
    '_archive', 'archive', '_archived', 'archived',
    '_old', 'old', '_backup', 'backup',
    '_deprecated', 'deprecated',
    '99_Temp', '_temp', 'temp',
    'dist', 'build', '.next',
}

AGENT_FOLDER_PREFIXES = ('A_root_', 'Office_')


def detect_task_type(rel_path_parts, root_rel):
    first_part = rel_path_parts[0] if rel_path_parts else ""
    if any(first_part.startswith(p) for p in AGENT_FOLDER_PREFIXES):
        agent_name = first_part.replace("A_root_", "").replace("Office_", "")
        return "agent", agent_name
    if len(rel_path_parts) >= 2 and rel_path_parts[0] == "OPERATION":
        if rel_path_parts[1].startswith("Office_"):
            return "agent", rel_path_parts[1].replace("Office_", "")
    return "project", None


def parse_todos(search_dir):
    todos = []
    print(f"🔍 Rà soát workspace: {search_dir}")
    search_dir_norm = os.path.normpath(search_dir)

    for root, dirs, files in os.walk(search_dir):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
        current_rel = os.path.relpath(root, search_dir_norm)
        depth = len(current_rel.split(os.sep)) if current_rel != "." else 0
        if depth > MAX_DEPTH:
            dirs[:] = []
            continue

        for file in files:
            if file.lower() != 'todo.md':
                continue
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, search_dir_norm)
            path_parts = rel_path.split(os.sep)
            major_project = path_parts[0].upper() if len(path_parts) > 1 else "GLOBAL"
            module_name = " / ".join(path_parts[1:-1]) if len(path_parts) > 2 else ""
            task_type, owner = detect_task_type(path_parts, current_rel)

            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    for line_num, line in enumerate(f, 1):
                        match = re.match(r'^\s*-\s*\[([ xX/])\]\s*(.*)', line)
                        if match:
                            status_char = match.group(1).strip().lower()
                            task_text = match.group(2).strip()
                            is_done = status_char == 'x'
                            tags = re.findall(r'#\w+', task_text)
                            todos.append({
                                'type': task_type,
                                'owner': owner,
                                'project': major_project,
                                'module': module_name,
                                'file_path': rel_path,
                                'line': line_num,
                                'text': task_text,
                                'tags': tags,
                                'done': is_done
                            })
            except Exception as e:
                print(f"⚠️ Error reading {filepath}: {e}")

    print(f"✅ Tìm thấy {len(todos)} tasks ({sum(1 for t in todos if t['type']=='project')} project, {sum(1 for t in todos if t['type']=='agent')} agent)")
    return todos


def save_data(todos, json_file):
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def rescan(current_dir):
    workspace_root = os.path.dirname(current_dir)
    task_list = parse_todos(workspace_root)
    save_data(task_list, os.path.join(current_dir, "todos.json"))
    return task_list


class AntigravityHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)

        # === REST API: GET /tasks ===
        if parsed.path == '/tasks':
            current_dir = os.path.dirname(os.path.abspath(__file__))
            json_file = os.path.join(current_dir, 'todos.json')
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    tasks = json.load(f)
            except:
                tasks = []

            # Apply query filters
            params = parse_qs(parsed.query)
            t = params.get('type', [None])[0]
            p = params.get('project', [None])[0]
            d = params.get('done', [None])[0]
            o = params.get('owner', [None])[0]

            if t: tasks = [x for x in tasks if x.get('type', '').lower() == t.lower()]
            if p: tasks = [x for x in tasks if (x.get('project') or '').lower() == p.lower()]
            if d is not None:
                want_done = d.lower() in ('true', '1', 'yes')
                tasks = [x for x in tasks if x.get('done') == want_done]
            if o: tasks = [x for x in tasks if (x.get('owner') or '').lower() == o.lower()]

            body = json.dumps({
                'count': len(tasks),
                'tasks': tasks
            }, ensure_ascii=False, indent=2).encode()
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(body)
            return

        # Serve static files normally
        super().do_GET()

    def _read_body(self):
        length = int(self.headers.get('Content-Length', 0))
        return json.loads(self.rfile.read(length)) if length else {}

    def _send_json(self, data, code=200):
        body = json.dumps(data, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        workspace_root = os.path.dirname(current_dir)

        # SYNC
        if self.path == '/update':
            task_list = rescan(current_dir)
            self._send_json({
                "status": "success", "count": len(task_list),
                "project_count": sum(1 for t in task_list if t['type'] == 'project'),
                "agent_count": sum(1 for t in task_list if t['type'] == 'agent')
            })

        # DELETE TASK
        elif self.path == '/delete-task':
            try:
                body = self._read_body()
                rel_path = body.get('file_path', '').replace('/', os.sep).replace('\\', os.sep)
                line_num = int(body.get('line', 0))
                filepath = os.path.join(workspace_root, rel_path)

                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()

                if 1 <= line_num <= len(lines):
                    del lines[line_num - 1]
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.writelines(lines)
                    task_list = rescan(current_dir)
                    self._send_json({"status": "success", "count": len(task_list)})
                else:
                    self._send_json({"status": "error", "message": "Line out of range"}, 400)
            except Exception as e:
                self._send_json({"status": "error", "message": str(e)}, 500)

        # UPDATE TASK TEXT
        elif self.path == '/update-task':
            try:
                body = self._read_body()
                rel_path = body.get('file_path', '').replace('/', os.sep).replace('\\', os.sep)
                line_num = int(body.get('line', 0))
                new_text = body.get('new_text', '').strip()
                filepath = os.path.join(workspace_root, rel_path)

                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()

                if 1 <= line_num <= len(lines):
                    old_line = lines[line_num - 1]
                    m = re.match(r'^(\s*-\s*\[[ xX/]\]\s*)(.*)', old_line)
                    if m:
                        lines[line_num - 1] = m.group(1) + new_text + '\n'
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.writelines(lines)
                        task_list = rescan(current_dir)
                        self._send_json({"status": "success", "count": len(task_list)})
                    else:
                        self._send_json({"status": "error", "message": "Not a checkbox line"}, 400)
                else:
                    self._send_json({"status": "error", "message": "Line out of range"}, 400)
            except Exception as e:
                self._send_json({"status": "error", "message": str(e)}, 500)

        # CREATE TASK
        elif self.path == '/tasks':
            try:
                body = self._read_body()
                text = body.get('text', '').strip()
                file_path = body.get('file_path', '').strip()  # relative path, e.g. "05_5Balance\ToDo.md"

                if not text or not file_path:
                    self._send_json({'status': 'error', 'message': 'text and file_path required'}, 400)
                    return

                rel_path = file_path.replace('/', os.sep).replace('\\', os.sep)
                filepath = os.path.join(workspace_root, rel_path)

                if not os.path.exists(filepath):
                    self._send_json({'status': 'error', 'message': f'File not found: {rel_path}'}, 404)
                    return

                # Append task line before the last blank line / end of file
                new_line = f'- [ ] {text}\n'
                with open(filepath, 'a', encoding='utf-8') as f:
                    f.write(new_line)

                task_list = rescan(current_dir)
                self._send_json({'status': 'success', 'message': 'Task created', 'count': len(task_list)})
            except Exception as e:
                self._send_json({'status': 'error', 'message': str(e)}, 500)

        else:
            self.send_error(404)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, format, *args):
        pass


def start_http_server(port=PORT):
    httpd = HTTPServer(('', port), AntigravityHandler)
    print(f"🚀 Task Server running → http://localhost:{port}/dashboard.html")
    httpd.serve_forever()


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_root = os.path.dirname(current_dir)

    print(f"🎬 Antigravity Task OS v4.1 (Edit + Delete)")
    print(f"📁 Workspace: {workspace_root}")

    task_list = parse_todos(workspace_root)
    save_data(task_list, os.path.join(current_dir, "todos.json"))

    os.chdir(current_dir)
    webbrowser.open(f"http://localhost:{PORT}/dashboard.html")
    start_http_server(PORT)
