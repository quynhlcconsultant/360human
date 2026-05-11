
# Part 1 builder - writes the HTML file
path = 'C:/Users/Admin/Desktop/Visionaries_Startup_April/02_Production/Frontend/test/index.html'

p1 = '''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>360Human — Prototype v2</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono&family=Lora:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {
  --cream: #F7F3ED;
  --warm-white: #FFFDF9;
  --sand: #EDE6DA;
  --ink: #1C1917;
  --charcoal: #44403C;
  --stone: #78716C;
  --border: #E7E0D6;
  --gold: #B8860B;
  --gold-soft: #D4A843;
  --gold-bg: #F5ECD4;
  --sage: #6B8F71;
  --sage-bg: #DCE8DD;
  --ember: #B85C38;
  --ember-bg: #F2DDD3;
  --success: #2D6A4F;
  --success-bg: #D8F3DC;
  --error: #C53030;
  --error-bg: #FEE2E2;
  --font-heading: "Playfair Display", Georgia, serif;
  --font-body: "Inter", system-ui, sans-serif;
  --font-reading: "Lora", Georgia, serif;
  --font-mono: "JetBrains Mono", monospace;
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.12);
  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: var(--font-body); background: var(--cream); color: var(--ink); font-size: 16px; line-height: 1.7; min-height: 100vh; }
.screen { display: none; min-height: 100vh; position: relative; z-index: 1; }
.screen.active { display: block; }
.btn { display: inline-flex; align-items: center; justify-content: center; font-family: var(--font-body); font-weight: 500; font-size: 15px; border: none; border-radius: var(--radius-md); cursor: pointer; padding: 12px 24px; transition: all 0.15s ease; }
.btn-gold { background: var(--gold); color: var(--warm-white); }
.btn-gold:hover { background: var(--gold-soft); }
.btn-ghost { background: transparent; color: var(--charcoal); border: 1px solid var(--border); }
.btn-ghost:hover { background: var(--sand); }
.btn-sm { padding: 8px 16px; font-size: 13px; }
.btn-lg { padding: 16px 32px; font-size: 16px; }
.btn-full { width: 100%; }
.btn-destructive { background: transparent; color: var(--error); border: 1px solid var(--error); }
.btn-success { background: var(--success); color: #fff; }
.card { background: var(--warm-white); border: 1px solid var(--border); border-radius: var(--radius-lg); box-shadow: var(--shadow-sm); padding: 24px; }
.badge { display: inline-flex; padding: 4px 12px; font-size: 12px; font-weight: 600; border-radius: var(--radius-full); border: 1px solid; }
.badge-free { background: var(--sand); color: var(--charcoal); border-color: var(--border); }
.badge-pro  { background: var(--sage-bg); color: var(--sage); border-color: var(--sage); }
.badge-system { background: var(--sand); color: var(--stone); border-color: var(--border); font-family: var(--font-mono); font-size: 11px; font-weight: 400; }
.tier-gate { position: absolute; inset: 0; backdrop-filter: blur(4px); background: rgba(255,255,255,0.75); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 12px; border-radius: var(--radius-lg); }
h1 { font-family: var(--font-heading); font-size: 40px; font-weight: 700; line-height: 1.2; }
h2 { font-family: var(--font-heading); font-size: 24px; font-weight: 600; line-height: 1.4; }
h3 { font-family: var(--font-heading); font-size: 20px; font-weight: 500; line-height: 1.5; }
h4 { font-family: var(--font-body); font-size: 16px; font-weight: 600; line-height: 1.7; }
.source { font-family: var(--font-mono); font-size: 13px; color: var(--stone); opacity: 0.8; }
.reading-text { font-family: var(--font-reading); font-size: 18px; line-height: 1.8; max-width: 680px; }
.muted { color: var(--stone); }
.container { max-width: 1280px; margin: 0 auto; padding: 0 48px; }
.container-sm { max-width: 480px; margin: 0 auto; padding: 0 20px; }
.container-md { max-width: 960px; margin: 0 auto; padding: 0 48px; }
input[type="text"], input[type="email"], input[type="password"], input[type="number"], select, textarea { width: 100%; padding: 12px 16px; font-family: var(--font-body); font-size: 15px; border: 1px solid var(--border); border-radius: var(--radius-sm); background: var(--warm-white); color: var(--ink); outline: none; }
input:focus, select:focus, textarea:focus { border-color: var(--gold); box-shadow: 0 0 0 2px rgba(184,134,11,0.12); }
.field { margin-bottom: 16px; }
.field label { display: block; font-size: 13px; font-weight: 500; margin-bottom: 6px; color: var(--charcoal); }
.separator { display: flex; align-items: center; gap: 16px; margin: 24px 0; color: var(--stone); font-size: 13px; }
.separator::before, .separator::after { content: ""; flex: 1; height: 1px; background: var(--border); }
.progress-bar { height: 4px; background: var(--sand); border-radius: 2px; overflow: hidden; }
.progress-bar .fill { height: 100%; background: var(--gold); border-radius: 2px; transition: width 0.3s ease; }
.accordion-item { border: 1px solid var(--border); border-radius: var(--radius-lg); margin-bottom: 8px; background: var(--warm-white); overflow: hidden; }
.accordion-header { padding: 16px 24px; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-family: var(--font-heading); font-size: 18px; font-weight: 500; }
.accordion-header:hover { background: var(--sand); }
.accordion-header .arrow { transition: transform 0.2s; font-size: 14px; color: var(--stone); }
.accordion-item.open .accordion-header .arrow { transform: rotate(180deg); }
.accordion-body { padding: 0 24px 24px; display: none; }
.accordion-item.open .accordion-body { display: block; }
.accordion-item.locked .accordion-header:hover { background: var(--gold-bg); }
.tabs { display: flex; border-bottom: 1px solid var(--border); gap: 0; overflow-x: auto; }
.tab { padding: 12px 24px; cursor: pointer; font-size: 15px; font-weight: 500; color: var(--stone); border-bottom: 2px solid transparent; transition: all 0.15s; white-space: nowrap; }
.tab:hover { color: var(--charcoal); }
.tab.active { color: var(--gold); border-bottom-color: var(--gold); }
.tab-panel { display: none; }
.tab-panel.active { display: block; }
.topbar { display: flex; align-items: center; justify-content: space-between; padding: 16px 48px; border-bottom: 1px solid var(--border); background: var(--warm-white); position: sticky; top: 0; z-index: 100; }
.topbar-left { display: flex; align-items: center; gap: 12px; }
.topbar-right { display: flex; align-items: center; gap: 12px; }
.app-layout { display: flex; min-height: 100vh; }
.sidebar { width: 240px; background: var(--warm-white); border-right: 1px solid var(--border); padding: 24px 0; flex-shrink: 0; position: sticky; top: 0; height: 100vh; overflow-y: auto; }
.sidebar-logo { padding: 0 24px 24px; font-family: var(--font-heading); font-size: 20px; font-weight: 600; }
.sidebar-nav { list-style: none; }
.sidebar-nav li { padding: 10px 24px; cursor: pointer; font-size: 15px; color: var(--charcoal); display: flex; align-items: center; gap: 10px; transition: all 0.1s; }
.sidebar-nav li:hover { background: var(--sand); }
.sidebar-nav li.active { color: var(--gold); background: var(--gold-bg); font-weight: 500; }
.sidebar-divider { height: 1px; background: var(--border); margin: 12px 24px; }
.app-main { flex: 1; overflow-y: auto; }
.dev-nav { position: fixed; bottom: 0; left: 0; right: 0; z-index: 9999; background: var(--ink); display: flex; gap: 4px; padding: 8px 12px; align-items: center; justify-content: flex-end; }
.dev-nav .tier-toggle { padding: 5px 12px; font-size: 11px; border-radius: 4px; cursor: pointer; border: none; white-space: nowrap; font-family: var(--font-mono); }
.dev-nav .tier-toggle.free { background: var(--sand); color: var(--ink); }
.dev-nav .tier-toggle.pro { background: var(--gold-soft); color: white; }
@keyframes copulse { 0%, 100% { opacity: 0.3; transform: scale(1); } 50% { opacity: 1; transform: scale(1.4); } }
.co-modal-overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.72); z-index: 2000; align-items: center; justify-content: center; padding: 20px; }
.co-modal-overlay.open { display: flex; }
.co-modal { background: var(--cream); border-radius: var(--radius-lg); max-width: 480px; width: 100%; padding: 32px; position: relative; max-height: 90vh; overflow-y: auto; box-shadow: 0 24px 64px rgba(0,0,0,0.35); }
.co-method-btn { background: var(--warm-white); border: 2px solid var(--border); border-radius: var(--radius-lg); padding: 16px; cursor: pointer; display: flex; align-items: center; gap: 16px; width: 100%; text-align: left; transition: border-color 0.15s, background 0.15s; }
.co-method-btn:hover { border-color: var(--gold); background: var(--gold-bg); }
.co-icon { width: 44px; height: 44px; background: var(--sand); border-radius: var(--radius-sm); display: flex; align-items: center; justify-content: center; font-size: 22px; flex-shrink: 0; }
@keyframes cursor-blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
.qa-cursor { display: inline-block; width: 2px; height: 18px; background: var(--gold); animation: cursor-blink 0.8s infinite; vertical-align: text-bottom; margin-left: 2px; }
.qa-response { font-family: var(--font-reading); font-size: 16px; line-height: 1.8; padding: 16px; background: var(--sand); border-radius: var(--radius-md); margin-top: 12px; min-height: 60px; }
.qa-loading { display: flex; gap: 6px; align-items: center; padding: 16px; }
.qa-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--stone); animation: copulse 1.2s infinite; }
.qa-dot:nth-child(2) { animation-delay: 0.3s; }
.qa-dot:nth-child(3) { animation-delay: 0.6s; }
.mob-overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 1000; }
.mob-overlay.open { display: block; }
.mob-sidebar { position: fixed; left: 0; top: 0; bottom: 0; width: 280px; background: var(--warm-white); z-index: 1001; padding: 24px 0; transform: translateX(-100%); transition: transform 0.25s ease; box-shadow: 4px 0 20px rgba(0,0,0,0.15); }
.mob-sidebar.open { transform: translateX(0); }
.mob-close { position: absolute; top: 16px; right: 16px; background: none; border: none; font-size: 24px; cursor: pointer; color: var(--stone); }
.hamburger { display: none; background: none; border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 6px 10px; cursor: pointer; font-size: 18px; color: var(--charcoal); }
.password-form { display: none; margin-top: 16px; }
.password-form.open { display: block; }
@keyframes slide-down { from { opacity: 0; transform: translateY(-8px); } to { opacity: 1; transform: translateY(0); } }
.pro-banner { animation: slide-down 0.3s ease; }
.sys-table { width: 100%; border-collapse: collapse; font-size: 13px; }
.sys-table th { background: var(--sand); padding: 8px 10px; text-align: left; font-weight: 600; color: var(--charcoal); border-bottom: 1px solid var(--border); }
.sys-table td { padding: 8px 10px; border-bottom: 1px solid var(--border); vertical-align: top; }
.sys-table tr:last-child td { border-bottom: none; }
.sys-table tr:hover td { background: var(--cream); }
.palace-grid { display: grid; grid-template-columns: repeat(4,1fr); grid-template-rows: repeat(4,1fr); gap: 2px; background: var(--border); border-radius: var(--radius-lg); overflow: hidden; }
.palace { background: var(--warm-white); padding: 8px; font-size: 11px; cursor: pointer; min-height: 72px; }
.palace:hover { background: var(--gold-bg); }
.palace.menh { background: var(--gold-bg); border: 2px solid var(--gold); }
.palace-name { font-weight: 600; font-size: 10px; color: var(--stone); display: block; margin-bottom: 2px; }
.palace-stars { font-size: 10px; color: var(--charcoal); line-height: 1.5; }
.palace-center { background: var(--sand); display: flex; align-items: center; justify-content: center; text-align: center; padding: 12px; }
.hd-center { display: flex; align-items: center; gap: 8px; padding: 6px 10px; border-radius: var(--radius-sm); font-size: 13px; margin-bottom: 4px; }
.hd-center.defined { background: var(--ink); color: var(--warm-white); }
.hd-center.undefined { background: var(--sand); color: var(--stone); border: 1px solid var(--border); }
.hd-dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }
.hd-center.defined .hd-dot { background: var(--gold-soft); }
.hd-center.undefined .hd-dot { background: var(--border); }
@media (max-width: 768px) {
  .container { padding: 0 20px; } .container-md { padding: 0 20px; } .topbar { padding: 12px 20px; }
  .sidebar { display: none; } .hamburger { display: flex; } h1 { font-size: 28px; } h2 { font-size: 20px; }
  .two-col, .three-col { flex-direction: column !important; } .app-main > .two-col > div { padding: 20px !important; }
  .co-modal { padding: 20px; } .dev-nav { padding: 6px 8px; }
}
@media (max-width: 480px) { .card { padding: 16px; } .btn-lg { padding: 14px 20px; font-size: 15px; } }
</style>
</head>
<body>

<!-- S1 LANDING -->
<div id="s1" class="screen active">
  <header style="display:flex;align-items:center;justify-content:space-between;padding:16px 48px;position:absolute;top:0;left:0;right:0;z-index:10;background:rgba(247,243,237,0.95);backdrop-filter:blur(8px);border-bottom:1px solid var(--border);">
    <div style="font-family:var(--font-heading);font-size:20px;font-weight:600;">360Human</div>
    <div style="display:flex;gap:12px;">
      <button class="btn btn-ghost btn-sm" onclick="showScreen('s2');switchTab2('login')">Đăng nhập</button>
      <button class="btn btn-gold btn-sm" onclick="showScreen('s2');switchTab2('register')">Đăng ký miễn phí</button>
    </div>
  </header>
  <section style="min-height:90vh;display:flex;align-items:center;padding:120px 48px 64px;">
    <div style="max-width:1280px;margin:0 auto;display:flex;gap:64px;align-items:center;width:100%;" class="two-col">
      <div style="flex:1;display:flex;align-items:center;justify-content:center;">
        <svg viewBox="0 0 320 320" style="width:100%;max-width:320px;">
          <circle cx="160" cy="160" r="140" fill="none" stroke="var(--border)" stroke-width="1"/>
          <circle cx="160" cy="160" r="100" fill="none" stroke="var(--sand)" stroke-width="1"/>
          <circle cx="160" cy="160" r="60" fill="var(--sand)" stroke="var(--border)" stroke-width="1"/>
          <circle cx="160" cy="160" r="20" fill="var(--ink)"/>
          <circle cx="160" cy="20" r="10" fill="var(--ink)"/>
          <circle cx="294" cy="105" r="10" fill="var(--gold-bg)" stroke="var(--gold)" stroke-width="2"/>
          <circle cx="247" cy="275" r="10" fill="var(--gold-bg)" stroke="var(--gold)" stroke-width="2"/>
          <circle cx="73" cy="275" r="10" fill="var(--gold-bg)" stroke="var(--gold)" stroke-width="2"/>
          <circle cx="26" cy="105" r="10" fill="var(--gold-bg)" stroke="var(--gold)" stroke-width="2"/>
          <line x1="160" y1="30" x2="160" y2="140" stroke="var(--ink)" stroke-width="1.5"/>
          <line x1="285" y1="112" x2="215" y2="152" stroke="var(--ink)" stroke-width="1.5"/>
          <line x1="240" y1="267" x2="196" y2="212" stroke="var(--ink)" stroke-width="1.5"/>
          <line x1="80" y1="267" x2="124" y2="212" stroke="var(--ink)" stroke-width="1.5"/>
          <line x1="35" y1="112" x2="105" y2="152" stroke="var(--ink)" stroke-width="1.5"/>
          <text x="160" y="12" text-anchor="middle" style="font-size:11px;fill:var(--stone);font-family:sans-serif;">Tử Vi</text>
          <text x="310" y="102" style="font-size:11px;fill:var(--stone);font-family:sans-serif;">BaZi</text>
          <text x="248" y="295" text-anchor="middle" style="font-size:11px;fill:var(--stone);font-family:sans-serif;">HD</text>
          <text x="72" y="295" text-anchor="end" style="font-size:11px;fill:var(--stone);font-family:sans-serif;">Số học</text>
          <text x="8" y="102" style="font-size:11px;fill:var(--stone);font-family:sans-serif;">Vedic</text>
        </svg>
      </div>
      <div style="flex:1;">
        <div style="display:inline-flex;align-items:center;gap:8px;background:var(--sand);padding:6px 16px;border-radius:var(--radius-full);margin-bottom:20px;">
          <span style="font-size:12px;font-family:var(--font-mono);color:var(--stone);">5 hệ thống x 10 chủ đề x 4 lăng kính</span>
        </div>
        <h1 style="margin-bottom:16px;">Hiểu mình sâu hơn,<br>sống đúng hơn</h1>
        <p style="font-size:18px;color:var(--charcoal);margin-bottom:32px;max-width:480px;line-height:1.8;">Phân tích 360° từ Tử Vi, BaZi, Human Design, Số học và Vedic. Một bức tranh toàn diện — không phải tử vi chung chung.</p>
        <div style="display:flex;gap:16px;align-items:center;flex-wrap:wrap;">
          <button class="btn btn-gold btn-lg" onclick="showScreen('s2')">Khám phá bản thân</button>
          <a href="#how" style="color:var(--stone);font-size:15px;">Tìm hiểu thêm ↓</a>
        </div>
        <p style="font-size:13px;color:var(--stone);margin-top:16px;">✓ Miễn phí · Không cần thẻ</p>
      </div>
    </div>
  </section>
  <section style="padding:64px 48px;background:var(--sand);">
    <div style="max-width:1280px;margin:0 auto;">
      <div style="display:flex;gap:24px;" class="three-col">
        <div class="card" style="flex:1;text-align:center;"><div style="font-size:32px;margin-bottom:12px;">⬡</div><h3>5 hệ thống</h3><p class="muted" style="font-size:15px;margin-top:8px;">Tử Vi, BaZi, Human Design, Số học, Vedic — cross-referenced và đối chiếu</p></div>
        <div class="card" style="flex:1;text-align:center;"><div style="font-size:32px;margin-bottom:12px;">◇</div><h3>20.000+ trang tài liệu</h3><p class="muted" style="font-size:15px;margin-top:8px;">Knowledge base nghiên cứu chuyên sâu, không phải copy-paste</p></div>
        <div class="card" style="flex:1;text-align:center;"><div style="font-size:32px;margin-bottom:12px;">○</div><h3>Cá nhân hóa</h3><p class="muted" style="font-size:15px;margin-top:8px;">Mọi thứ tính từ dữ liệu sinh của bạn. Không có hai người giống nhau.</p></div>
      </div>
    </div>
  </section>
  <section id="how" style="padding:96px 48px;">
    <div style="max-width:960px;margin:0 auto;text-align:center;">
      <h2 style="margin-bottom:8px;">Chỉ 4 bước để hiểu mình</h2>
      <p class="muted" style="margin-bottom:48px;">Từ thông tin sinh đến bản đồ cá nhân hoàn chỉnh</p>
      <div style="display:flex;gap:32px;" class="three-col">
        <div style="flex:1;"><div style="font-family:var(--font-heading);font-size:48px;color:var(--gold);margin-bottom:8px;opacity:0.4;">1</div><h4>Nhập thông tin</h4><p class="muted" style="font-size:14px;">Họ tên, ngày giờ, nơi sinh</p></div>
        <div style="flex:1;"><div style="font-family:var(--font-heading);font-size:48px;color:var(--gold);margin-bottom:8px;opacity:0.4;">2</div><h4>Phân tích 360°</h4><p class="muted" style="font-size:14px;">5 hệ thống tính toán song song</p></div>
        <div style="flex:1;"><div style="font-family:var(--font-heading);font-size:48px;color:var(--gold);margin-bottom:8px;opacity:0.4;">3</div><h4>Đọc chi tiết</h4><p class="muted" style="font-size:14px;">10 chủ đề — What, Why, How, What's next</p></div>
        <div style="flex:1;"><div style="font-family:var(--font-heading);font-size:48px;color:var(--gold);margin-bottom:8px;opacity:0.4;">4</div><h4>Hỏi & Hành động</h4><p class="muted" style="font-size:14px;">Đặt câu hỏi cụ thể, nhận kế hoạch hành động</p></div>
      </div>
    </div>
  </section>
  <section style="padding:48px;text-align:center;border-top:1px solid var(--border);background:var(--sand);">
    <h2 style="margin-bottom:8px;">Bắt đầu miễn phí</h2>
    <p class="muted" style="margin-bottom:24px;">Nâng cấp khi bạn muốn đi sâu hơn</p>
    <button class="btn btn-gold btn-lg" onclick="showScreen(\'s7\')">Xem bảng giá</button>
  </section>
  <footer style="padding:32px 48px;text-align:center;border-top:1px solid var(--border);">
    <p class="muted" style="font-size:13px;">360Human © 2026 · Về chúng tôi · Chính sách bảo mật · Liên hệ</p>
  </footer>
</div>

<!-- S2 AUTH -->
<div id="s2" class="screen">
  <div style="min-height:100vh;display:flex;align-items:center;justify-content:center;padding:48px 20px;">
    <div class="container-sm" style="width:100%;">
      <div style="text-align:center;margin-bottom:32px;"><div style="font-family:var(--font-heading);font-size:24px;font-weight:600;cursor:pointer;" onclick="showScreen(\'s1\')">360Human</div></div>
      <div class="tabs" style="margin-bottom:24px;" id="auth-tabs">
        <div class="tab active" id="tab-register" onclick="switchTab2(\'register\')">Đăng ký</div>
        <div class="tab" id="tab-login" onclick="switchTab2(\'login\')">Đăng nhập</div>
      </div>
      <div id="register" style="display:block;">
        <div class="field"><label>Email</label><input type="email" placeholder="email@example.com"></div>
        <div class="field"><label>Mật khẩu</label><input type="password" placeholder="Tối thiểu 8 ký tự"></div>
        <div class="field"><label>Xác nhận mật khẩu</label><input type="password" placeholder="Nhập lại mật khẩu"></div>
        <button class="btn btn-gold btn-full btn-lg" onclick="showScreen(\'s3\')">Tạo tài khoản</button>
        <p class="muted" style="font-size:12px;text-align:center;margin-top:12px;">Bằng cách tạo tài khoản, bạn đồng ý với <a href="#" style="color:var(--gold);">điều khoản</a> của chúng tôi.</p>
      </div>
      <div id="login" style="display:none;">
        <div class="field"><label>Email</label><input type="email" placeholder="email@example.com"></div>
        <div class="field"><label>Mật khẩu</label><input type="password" placeholder="Mật khẩu"><div style="text-align:right;margin-top:6px;"><a href="#" style="font-size:13px;color:var(--gold);" onclick="openForgotPassword()">Quên mật khẩu?</a></div></div>
        <button class="btn btn-gold btn-full btn-lg" onclick="showScreen(\'s4\')">Đăng nhập</button>
      </div>
      <div class="separator">hoặc</div>
      <button class="btn btn-ghost btn-full" style="opacity:0.5;cursor:not-allowed;" disabled>Google Sign-In (Sprint 2)</button>
    </div>
  </div>
</div>

<!-- S3 ONBOARDING -->
<div id="s3" class="screen">
  <div style="min-height:100vh;display:flex;align-items:center;justify-content:center;padding:64px 20px;">
    <div class="container-sm" style="width:100%;">
      <div style="text-align:center;margin-bottom:32px;"><div style="font-family:var(--font-heading);font-size:24px;font-weight:600;">360Human</div><p class="muted" style="margin-top:8px;font-size:15px;">Một vài thông tin để bắt đầu hành trình của bạn</p></div>
      <div class="progress-bar" style="margin-bottom:8px;"><div class="fill" id="onboard-progress" style="width:0%"></div></div>
      <p class="muted" style="font-size:12px;text-align:right;margin-bottom:24px;" id="onboard-step-label">0 / 7 hoàn thành</p>
      <div class="field"><label>Họ và tên khai sinh</label><input type="text" placeholder="Nguyễn Thị Thảo" id="ob-name" oninput="updateProgress()"></div>
      <div class="field"><label>Giới tính</label>
        <div style="display:flex;gap:8px;" id="gender-group">
          <button class="btn btn-ghost" style="flex:1;" onclick="selectGender(this,\'Nam\')">Nam</button>
          <button class="btn btn-ghost" style="flex:1;" onclick="selectGender(this,\'Nữ\')">Nữ</button>
          <button class="btn btn-ghost" style="flex:1;" onclick="selectGender(this,\'Khác\')">Khác</button>
        </div>
      </div>
      <div class="field"><label>Ngày sinh</label>
        <div style="display:flex;gap:8px;">
          <div style="flex:1;"><input type="number" placeholder="DD" min="1" max="31" id="ob-day" oninput="updateProgress()"></div>
          <div style="flex:1;"><input type="number" placeholder="MM" min="1" max="12" id="ob-month" oninput="updateProgress()"></div>
          <div style="flex:2;"><input type="number" placeholder="YYYY" min="1920" max="2010" id="ob-year" oninput="updateProgress()"></div>
        </div>
      </div>
      <div class="field"><label>Giờ sinh <span class="muted">(quan trọng cho Human Design & Vedic)</span></label>
        <input type="text" placeholder="VD: 14:30" id="ob-time" oninput="updateProgress()">
        <label style="display:flex;align-items:center;gap:8px;margin-top:8px;font-size:13px;color:var(--stone);cursor:pointer;"><input type="checkbox" style="width:auto;" id="ob-no-time" onchange="updateProgress()"> Tôi không nhớ giờ sinh</label>
      </div>
      <div class="field"><label>Nơi sinh</label><input type="text" placeholder="VD: TP. Hồ Chí Minh" id="ob-city" oninput="updateProgress()"></div>
      <button class="btn btn-gold btn-full btn-lg" style="margin-top:8px;" onclick="showLoading()">Bắt đầu phân tích →</button>
      <p class="muted" style="font-size:12px;text-align:center;margin-top:12px;">Thông tin của bạn được mã hóa và bảo mật</p>
    </div>
  </div>
  <div id="loading-overlay" style="display:none;position:fixed;inset:0;background:var(--cream);z-index:50;flex-direction:column;align-items:center;justify-content:center;gap:16px;padding:40px;">
    <h2 style="margin-bottom:8px;">Đang tạo bản đồ cá nhân...</h2>
    <p class="muted" style="font-size:14px;margin-bottom:16px;">5 hệ thống đang phân tích dữ liệu sinh của bạn</p>
    <div id="loading-layers" style="width:340px;display:flex;flex-direction:column;gap:10px;"></div>
  </div>
</div>
'''

with open(path, 'w', encoding='utf-8') as f:
    f.write(p1)
print('part1 done', len(p1))
