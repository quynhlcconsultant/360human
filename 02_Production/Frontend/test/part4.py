
path = 'C:/Users/Admin/Desktop/Visionaries_Startup_April/02_Production/Frontend/test/index.html'

p4 = '''
<!-- S6 DEEP DIVE -->
<div id="s6" class="screen">
  <div class="app-layout">
    <nav class="sidebar">
      <div class="sidebar-logo">360Human</div>
      <ul class="sidebar-nav">
        <li onclick="showScreen('s4')">&#9689; Tổng Quan</li>
        <li onclick="showScreen('s5')">&#11041; Biểu đồ hệ thống</li>
        <li class="active" onclick="showScreen('s6')">&#9678; Phân tích sâu</li>
        <li onclick="showScreen('s9')">&#9719; Lịch Vận</li>
        <li onclick="showScreen('s10')">&#9651; Hành động</li>
      </ul>
      <div class="sidebar-divider"></div>
      <ul class="sidebar-nav">
        <li onclick="showScreen('s7')">&#10022; Nâng cấp</li>
        <li onclick="showScreen('s8')">&#9881; Cài đặt</li>
      </ul>
    </nav>
    <div class="app-main">
      <div class="topbar">
        <div class="topbar-left">
          <button class="hamburger" onclick="openMobileNav()">&#9776;</button>
          <a href="#" style="color:var(--stone);font-size:14px;" onclick="showScreen('s4')">&#8592; Tổng Quan</a>
          <span style="color:var(--border);">&#8250;</span>
          <span style="font-weight:500;">Phân tích sâu</span>
        </div>
        <div class="topbar-right"><span class="badge badge-pro" id="s6-tier-badge">PRO</span></div>
      </div>
      <div style="display:flex;gap:0;" class="two-col">
        <div style="flex:1;padding:32px 32px 80px 48px;border-right:1px solid var(--border);">
          <h2 style="margin-bottom:8px;">Đặt câu hỏi cụ thể</h2>
          <p class="muted" style="font-size:14px;margin-bottom:24px;">Mô tả tình huống thực tế của bạn — AI sẽ phân tích từ nhiều hệ thống</p>
          <div style="margin-bottom:16px;">
            <textarea id="s6-question" rows="4" placeholder="VD: Tôi đang phân vân giữa việc ở lại công ty hiện tại hay mở business riêng. Theo biểu đồ của tôi, thời điểm nào và hướng đi nào phù hợp hơn?" style="resize:vertical;"></textarea>
          </div>
          <button class="btn btn-gold btn-full" onclick="sendDeepDive()">Phân tích →</button>
          <div style="margin-top:32px;">
            <h4 style="margin-bottom:16px;color:var(--stone);font-size:14px;text-transform:uppercase;letter-spacing:0.5px;">Câu hỏi gợi ý</h4>
            <div style="display:flex;flex-direction:column;gap:8px;" id="s6-suggestions">
              <button class="btn btn-ghost" style="text-align:left;padding:12px 16px;font-size:14px;justify-content:flex-start;" onclick="s6FillQuestion(this)">Tại sao tôi hay tự phá hoại bản thân khi gần thành công?</button>
              <button class="btn btn-ghost" style="text-align:left;padding:12px 16px;font-size:14px;justify-content:flex-start;" onclick="s6FillQuestion(this)">Đâu là mối quan hệ cảm xúc/nghề nghiệp phù hợp nhất với tôi?</button>
              <button class="btn btn-ghost" style="text-align:left;padding:12px 16px;font-size:14px;justify-content:flex-start;" onclick="s6FillQuestion(this)">Năm 2026-2027 tôi nên ưu tiên điều gì?</button>
              <button class="btn btn-ghost" style="text-align:left;padding:12px 16px;font-size:14px;justify-content:flex-start;" onclick="s6FillQuestion(this)">Tôi có phù hợp để làm lãnh đạo/entrepreneur không?</button>
              <button class="btn btn-ghost" style="text-align:left;padding:12px 16px;font-size:14px;justify-content:flex-start;" onclick="s6FillQuestion(this)">Tại sao tôi có pattern lặp đi lặp lại trong các mối quan hệ?</button>
            </div>
          </div>
          <div style="margin-top:32px;padding-top:24px;border-top:1px solid var(--border);">
            <h4 style="margin-bottom:16px;color:var(--stone);font-size:14px;">Lịch sử phân tích</h4>
            <div style="display:flex;flex-direction:column;gap:8px;">
              <div style="padding:12px;background:var(--sand);border-radius:var(--radius-md);cursor:pointer;" onclick="s6LoadHistory(1)"><p style="font-size:13px;font-weight:500;">Tại sao tôi hay trì hoãn?</p><p class="muted" style="font-size:11px;margin-top:2px;">20/03/2026 · 4 hệ thống</p></div>
              <div style="padding:12px;background:var(--sand);border-radius:var(--radius-md);cursor:pointer;" onclick="s6LoadHistory(2)"><p style="font-size:13px;font-weight:500;">Mối quan hệ nào phù hợp với tôi?</p><p class="muted" style="font-size:11px;margin-top:2px;">18/03/2026 · 5 hệ thống</p></div>
            </div>
          </div>
        </div>
        <div style="flex:1.2;padding:32px 48px 32px 32px;" id="s6-result-panel">
          <div id="s6-empty" style="height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;padding:48px;text-align:center;opacity:0.4;">
            <div style="font-size:48px;">&#9678;</div>
            <h3>Chọn câu hỏi hoặc nhập câu hỏi của bạn</h3>
            <p class="muted" style="font-size:14px;">AI sẽ phân tích từ 5 hệ thống và đưa ra góc nhìn tổng hợp</p>
          </div>
          <div id="s6-loading" style="display:none;padding:32px 0;">
            <div style="display:flex;flex-direction:column;gap:10px;margin-bottom:24px;">
              <div style="display:flex;align-items:center;gap:12px;padding:12px 16px;background:var(--sand);border-radius:var(--radius-md);" id="s6-l1"><span style="font-size:16px;opacity:0.3;">&#11041;</span><span class="muted">Tử Vi đang phân tích...</span><div class="progress-bar" style="flex:1;"><div class="fill" style="width:0%" id="s6-p1"></div></div></div>
              <div style="display:flex;align-items:center;gap:12px;padding:12px 16px;background:var(--sand);border-radius:var(--radius-md);" id="s6-l2"><span style="font-size:16px;opacity:0.3;">&#9671;</span><span class="muted">BaZi đang phân tích...</span><div class="progress-bar" style="flex:1;"><div class="fill" style="width:0%" id="s6-p2"></div></div></div>
              <div style="display:flex;align-items:center;gap:12px;padding:12px 16px;background:var(--sand);border-radius:var(--radius-md);" id="s6-l3"><span style="font-size:16px;opacity:0.3;">&#9651;</span><span class="muted">Human Design đang phân tích...</span><div class="progress-bar" style="flex:1;"><div class="fill" style="width:0%" id="s6-p3"></div></div></div>
              <div style="display:flex;align-items:center;gap:12px;padding:12px 16px;background:var(--sand);border-radius:var(--radius-md);" id="s6-l4"><span style="font-size:16px;opacity:0.3;">&#9675;</span><span class="muted">Số học đang phân tích...</span><div class="progress-bar" style="flex:1;"><div class="fill" style="width:0%" id="s6-p4"></div></div></div>
              <div style="display:flex;align-items:center;gap:12px;padding:12px 16px;background:var(--sand);border-radius:var(--radius-md);" id="s6-l5"><span style="font-size:16px;opacity:0.3;">&#9734;</span><span class="muted">Vedic đang phân tích...</span><div class="progress-bar" style="flex:1;"><div class="fill" style="width:0%" id="s6-p5"></div></div></div>
            </div>
          </div>
          <div id="s6-result" style="display:none;">
            <div style="display:flex;align-items:start;justify-content:space-between;margin-bottom:20px;">
              <div><h3 style="margin-bottom:4px;" id="s6-result-title">Phân tích</h3><div style="display:flex;gap:6px;flex-wrap:wrap;" id="s6-result-sources"><span class="badge-system">Tử Vi</span><span class="badge-system">BaZi</span><span class="badge-system">Human Design</span><span class="badge-system">Số học</span></div></div>
              <button class="btn btn-ghost btn-sm" onclick="s6Reset()">Hỏi câu khác</button>
            </div>
            <div id="s6-result-body" class="reading-text" style="font-size:16px;line-height:1.9;"></div>
            <div style="margin-top:24px;padding:16px;background:var(--sand);border-radius:var(--radius-lg);">
              <h4 style="margin-bottom:12px;">Hành động đề xuất từ phân tích này</h4>
              <div style="display:flex;flex-direction:column;gap:8px;" id="s6-actions">
                <div style="display:flex;justify-content:space-between;align-items:start;padding:10px;background:var(--warm-white);border-radius:var(--radius-sm);"><div><strong style="font-size:14px;">Áp dụng quy tắc 2 phút</strong><br><span class="muted" style="font-size:13px;">Nếu mất ít hơn 2 phút — làm ngay</span></div><span class="badge-system">BaZi</span></div>
                <div style="display:flex;justify-content:space-between;align-items:start;padding:10px;background:var(--warm-white);border-radius:var(--radius-sm);"><div><strong style="font-size:14px;">Thực hành Sacral response hàng ngày</strong><br><span class="muted" style="font-size:13px;">Hỏi bản thân "Uh-huh hay Uh-uh?" trước mỗi task</span></div><span class="badge-system">HD</span></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- S7 PRICING (2 tiers only) -->
<div id="s7" class="screen">
  <div style="min-height:100vh;padding:80px 48px 120px;">
    <div style="text-align:center;margin-bottom:16px;">
      <a href="#" style="color:var(--stone);font-size:14px;" onclick="showScreen('s4')">&#8592; Quay lại</a>
    </div>
    <div class="container-md" style="width:100%;">
      <div style="text-align:center;margin-bottom:48px;">
        <h1 style="margin-bottom:12px;">Mở khóa hành trình của bạn</h1>
        <p class="muted" style="font-size:18px;">Một lần mua — lifetime access. Không subscription.</p>
      </div>
      <div style="display:flex;gap:24px;justify-content:center;margin-bottom:48px;flex-wrap:wrap;">
        <!-- FREE -->
        <div class="card" style="flex:1;min-width:280px;max-width:360px;">
          <span class="badge badge-free" style="margin-bottom:16px;">FREE</span>
          <div style="font-family:var(--font-heading);font-size:36px;font-weight:700;margin-bottom:4px;">0đ</div>
          <p class="muted" style="margin-bottom:24px;font-size:14px;">Khám phá bản thân</p>
          <ul style="list-style:none;display:flex;flex-direction:column;gap:10px;font-size:14px;margin-bottom:28px;">
            <li>&#10003; 2 chủ đề luận giải (~2.000 từ)</li>
            <li>&#10003; 2 hành động nền móng</li>
            <li>&#10003; Tháng hiện tại (Lịch Vận)</li>
            <li style="color:var(--stone);">&#10007; 8 chủ đề còn lại</li>
            <li style="color:var(--stone);">&#10007; 5 biểu đồ hệ thống</li>
            <li style="color:var(--stone);">&#10007; Hỏi đáp AI</li>
            <li style="color:var(--stone);">&#10007; Phân tích sâu</li>
            <li style="color:var(--stone);">&#10007; Xuất PDF</li>
          </ul>
          <div style="text-align:center;color:var(--stone);font-size:13px;padding:12px;background:var(--sand);border-radius:var(--radius-md);">Gói hiện tại &#10003;</div>
        </div>

        <!-- PRO -->
        <div class="card" style="flex:1;min-width:280px;max-width:360px;border:2px solid var(--gold);position:relative;">
          <div style="position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:var(--gold);color:white;padding:4px 20px;border-radius:var(--radius-full);font-size:12px;font-weight:600;white-space:nowrap;">Phổ biến nhất</div>
          <span class="badge badge-pro" style="margin-bottom:16px;">PRO</span>
          <div style="font-family:var(--font-heading);font-size:36px;font-weight:700;margin-bottom:4px;">199.000đ</div>
          <p class="muted" style="margin-bottom:24px;font-size:14px;">Hiểu sâu &amp; hành động</p>
          <ul style="list-style:none;display:flex;flex-direction:column;gap:10px;font-size:14px;margin-bottom:28px;">
            <li>&#10003; <strong>10 chủ đề</strong> luận giải (~10.000 từ)</li>
            <li>&#10003; <strong>5 biểu đồ</strong> hệ thống chi tiết</li>
            <li>&#10003; <strong>Hỏi đáp AI</strong> không giới hạn</li>
            <li>&#10003; <strong>Phân tích sâu</strong> tình huống cụ thể</li>
            <li>&#10003; <strong>Cả 3 tầng</strong> hành động</li>
            <li>&#10003; <strong>Lifetime</strong> Lịch Vận</li>
            <li>&#10003; <strong>Xuất PDF</strong> 36 trang</li>
          </ul>
          <button class="btn btn-gold btn-full btn-lg" onclick="openCheckout('pro')">Nâng cấp PRO</button>
        </div>
      </div>
      <div style="text-align:center;">
        <p class="muted" style="font-size:13px;max-width:520px;margin:0 auto 8px;">Mỗi gói áp dụng cho 1 hồ sơ. Thêm hồ sơ mới với cùng mức giá tại <a href="#" style="color:var(--gold);" onclick="showScreen('s8')">Cài đặt</a>.</p>
        <p class="muted" style="font-size:13px;">Câu hỏi? <a href="mailto:support@360human.ai" style="color:var(--gold);">Liên hệ support →</a></p>
      </div>
    </div>
  </div>
</div>

<!-- S8 PROFILE + SETTINGS -->
<div id="s8" class="screen">
  <div class="app-layout">
    <nav class="sidebar">
      <div class="sidebar-logo">360Human</div>
      <ul class="sidebar-nav">
        <li onclick="showScreen('s4')">&#9689; Tổng Quan</li>
        <li onclick="showScreen('s5')">&#11041; Biểu đồ hệ thống</li>
        <li onclick="showScreen('s6')">&#9678; Phân tích sâu</li>
        <li onclick="showScreen('s9')">&#9719; Lịch Vận</li>
        <li onclick="showScreen('s10')">&#9651; Hành động</li>
      </ul>
      <div class="sidebar-divider"></div>
      <ul class="sidebar-nav">
        <li onclick="showScreen('s7')">&#10022; Nâng cấp</li>
        <li class="active" onclick="showScreen('s8')">&#9881; Cài đặt</li>
      </ul>
    </nav>
    <div class="app-main">
      <div class="topbar">
        <div class="topbar-left">
          <button class="hamburger" onclick="openMobileNav()">&#9776;</button>
          <a href="#" style="color:var(--stone);" onclick="showScreen('s4')">&#8592; Tổng Quan</a>
        </div>
      </div>
      <div class="container-md" style="padding-top:32px;padding-bottom:80px;">
        <div class="card" style="margin-bottom:24px;display:flex;gap:24px;align-items:center;">
          <div style="width:64px;height:64px;border-radius:50%;background:var(--gold-bg);display:flex;align-items:center;justify-content:center;font-family:var(--font-heading);font-size:24px;color:var(--gold);font-weight:600;flex-shrink:0;">TN</div>
          <div style="flex:1;">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:4px;flex-wrap:wrap;">
              <strong style="font-size:18px;">Thảo Nguyễn</strong>
              <span class="badge badge-free" id="s8-tier-badge">FREE</span>
              <a href="#" style="font-size:13px;color:var(--gold);" onclick="openCheckout('pro');return false;" id="s8-upgrade-link">Nâng cấp PRO</a>
            </div>
            <p class="muted" style="font-size:14px;">thao.nguyen@email.com</p>
          </div>
        </div>
        <div class="card" style="margin-bottom:24px;">
          <div style="display:flex;justify-content:space-between;align-items:start;margin-bottom:12px;"><h4>Dữ liệu sinh</h4><button class="btn btn-ghost btn-sm" onclick="toggleBirthEdit()">Chỉnh sửa</button></div>
          <div id="birth-display"><p style="font-size:15px;">15/06/1997 · 14:30 · TP. Hồ Chí Minh</p><p class="muted" style="font-size:13px;margin-top:4px;">Thay đổi dữ liệu sinh sẽ tính toán lại toàn bộ biểu đồ</p></div>
          <div id="birth-edit" style="display:none;margin-top:12px;">
            <div style="display:flex;gap:8px;margin-bottom:8px;"><input type="number" placeholder="DD" value="15" style="width:70px;"><input type="number" placeholder="MM" value="06" style="width:70px;"><input type="number" placeholder="YYYY" value="1997" style="flex:1;"></div>
            <div style="display:flex;gap:8px;margin-bottom:12px;"><input type="text" placeholder="HH:MM" value="14:30" style="flex:1;"><input type="text" placeholder="Thành phố" value="TP. Hồ Chí Minh" style="flex:2;"></div>
            <div style="display:flex;gap:8px;"><button class="btn btn-gold btn-sm" onclick="toggleBirthEdit()">Lưu thay đổi</button><button class="btn btn-ghost btn-sm" onclick="toggleBirthEdit()">Hủy</button></div>
          </div>
        </div>
        <div class="card" style="margin-bottom:24px;">
          <h4 style="margin-bottom:16px;">Hồ sơ</h4>
          <div style="display:flex;flex-direction:column;gap:8px;margin-bottom:12px;">
            <div style="display:flex;align-items:center;gap:12px;padding:12px;background:var(--gold-bg);border-radius:var(--radius-sm);border:1px solid var(--gold);">
              <span>&#9689;</span>
              <div style="flex:1;"><strong>Thảo Nguyễn</strong><p class="muted" style="font-size:12px;">15/06/1997 · TP. HCM</p></div>
              <span class="badge badge-free" id="s8-profile-badge">FREE</span>
            </div>
          </div>
          <button class="btn btn-ghost btn-sm" onclick="alert('Thêm hồ sơ mới: 199.000đ/hồ sơ (PRO)')">+ Thêm hồ sơ mới</button>
          <p class="muted" style="font-size:12px;margin-top:8px;">Mỗi hồ sơ mới — phân tích độc lập với cùng mức giá</p>
        </div>
        <div class="card" style="margin-bottom:24px;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;"><h4>Mật khẩu</h4><button class="btn btn-ghost btn-sm" onclick="togglePasswordForm()">Đổi mật khẩu</button></div>
          <div class="password-form" id="password-form">
            <div class="field" style="margin-top:16px;"><label>Mật khẩu hiện tại</label><input type="password" placeholder="••••••••"></div>
            <div class="field"><label>Mật khẩu mới</label><input type="password" placeholder="Tối thiểu 8 ký tự"></div>
            <div class="field"><label>Xác nhận mật khẩu mới</label><input type="password" placeholder="Nhập lại mật khẩu mới"></div>
            <div style="display:flex;gap:8px;"><button class="btn btn-gold btn-sm" onclick="togglePasswordForm();alert('Mật khẩu đã được cập nhật!')">Lưu mật khẩu</button><button class="btn btn-ghost btn-sm" onclick="togglePasswordForm()">Hủy</button></div>
          </div>
        </div>
        <div class="card" style="margin-bottom:24px;">
          <h4 style="margin-bottom:16px;">Thông báo</h4>
          <div style="display:flex;flex-direction:column;gap:12px;">
            <label style="display:flex;align-items:center;justify-content:space-between;cursor:pointer;"><span style="font-size:15px;">Lịch Vận hàng tháng</span><input type="checkbox" checked style="width:auto;"></label>
            <label style="display:flex;align-items:center;justify-content:space-between;cursor:pointer;"><span style="font-size:15px;">Nhắc nhở hành động hàng tuần</span><input type="checkbox" style="width:auto;"></label>
          </div>
        </div>
        <div class="card" style="border-color:var(--error);background:var(--error-bg);">
          <h4 style="color:var(--error);margin-bottom:8px;">Vùng nguy hiểm</h4>
          <p class="muted" style="font-size:13px;margin-bottom:12px;">Hành động này không thể hoàn tác</p>
          <button class="btn btn-destructive btn-sm" onclick="confirmDeleteAccount()">Xóa tài khoản</button>
        </div>
      </div>
    </div>
  </div>
</div>
'''

with open(path, 'a', encoding='utf-8') as f:
    f.write(p4)
print('part4 done', len(p4))
