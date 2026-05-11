
path = 'C:/Users/Admin/Desktop/Visionaries_Startup_April/02_Production/Frontend/test/index.html'

p6 = '''
<!-- CHECKOUT MODAL -->
<div id="checkout-modal" class="co-modal-overlay">
  <div class="co-modal">
    <div style="display:flex;justify-content:space-between;align-items:start;margin-bottom:24px;">
      <div>
        <h3 style="font-family:var(--font-heading);" id="co-title">Nâng cấp PRO</h3>
        <p class="muted" style="font-size:14px;margin-top:4px;" id="co-subtitle">199.000đ · Lifetime · 1 hồ sơ</p>
      </div>
      <button onclick="closeCheckout()" style="background:none;border:none;font-size:28px;line-height:1;cursor:pointer;color:var(--stone);padding:0 4px;">&#215;</button>
    </div>
    <div id="co-step1">
      <p style="font-size:15px;font-weight:500;margin-bottom:16px;">Chọn phương thức thanh toán:</p>
      <div style="display:flex;flex-direction:column;gap:12px;">
        <button class="co-method-btn" onclick="coSelectMethod('vietqr')"><div class="co-icon">&#127974;</div><div><strong style="font-size:15px;">VietQR</strong><p class="muted" style="font-size:13px;margin-top:2px;">Chuyển khoản tức thì — hỗ trợ mọi ngân hàng</p></div></button>
        <button class="co-method-btn" onclick="coSelectMethod('card')"><div class="co-icon">&#128179;</div><div><strong style="font-size:15px;">Thẻ ngân hàng</strong><p class="muted" style="font-size:13px;margin-top:2px;">Visa · Mastercard · JCB · Napas</p></div></button>
      </div>
      <p class="muted" style="font-size:12px;text-align:center;margin-top:20px;">&#128274; Thanh toán an toàn · Không lưu thông tin thẻ</p>
    </div>
    <div id="co-step2-vietqr" style="display:none;text-align:center;">
      <div style="background:var(--warm-white);border:1px solid var(--border);border-radius:var(--radius-lg);width:200px;height:200px;margin:0 auto 16px;display:flex;align-items:center;justify-content:center;">
        <svg viewBox="0 0 100 100" width="168" height="168" xmlns="http://www.w3.org/2000/svg">
          <rect x="8" y="8" width="28" height="28" fill="none" stroke="var(--ink)" stroke-width="3"/><rect x="13" y="13" width="18" height="18" fill="var(--ink)"/>
          <rect x="64" y="8" width="28" height="28" fill="none" stroke="var(--ink)" stroke-width="3"/><rect x="69" y="13" width="18" height="18" fill="var(--ink)"/>
          <rect x="8" y="64" width="28" height="28" fill="none" stroke="var(--ink)" stroke-width="3"/><rect x="13" y="69" width="18" height="18" fill="var(--ink)"/>
          <rect x="42" y="8" width="5" height="5" fill="var(--ink)"/><rect x="50" y="8" width="5" height="5" fill="var(--ink)"/>
          <rect x="42" y="16" width="5" height="10" fill="var(--ink)"/><rect x="50" y="20" width="5" height="5" fill="var(--ink)"/>
          <rect x="8" y="42" width="10" height="5" fill="var(--ink)"/><rect x="22" y="42" width="10" height="5" fill="var(--ink)"/>
          <rect x="42" y="36" width="10" height="5" fill="var(--ink)"/><rect x="56" y="36" width="10" height="5" fill="var(--ink)"/>
          <rect x="42" y="44" width="5" height="5" fill="var(--ink)"/><rect x="50" y="42" width="10" height="5" fill="var(--ink)"/>
          <rect x="64" y="44" width="10" height="5" fill="var(--ink)"/><rect x="78" y="44" width="14" height="5" fill="var(--ink)"/>
          <rect x="42" y="52" width="10" height="5" fill="var(--ink)"/><rect x="56" y="52" width="5" height="5" fill="var(--ink)"/>
          <rect x="64" y="56" width="10" height="5" fill="var(--ink)"/><rect x="78" y="56" width="5" height="5" fill="var(--ink)"/>
          <rect x="42" y="64" width="5" height="5" fill="var(--ink)"/><rect x="50" y="64" width="10" height="5" fill="var(--ink)"/>
          <rect x="64" y="64" width="5" height="5" fill="var(--ink)"/><rect x="72" y="70" width="5" height="10" fill="var(--ink)"/>
          <rect x="80" y="64" width="12" height="5" fill="var(--ink)"/><rect x="42" y="72" width="5" height="10" fill="var(--ink)"/>
          <rect x="50" y="78" width="10" height="5" fill="var(--ink)"/><rect x="64" y="78" width="5" height="14" fill="var(--ink)"/>
          <rect x="80" y="78" width="12" height="14" fill="var(--ink)"/>
        </svg>
      </div>
      <p style="font-weight:600;font-size:20px;margin-bottom:4px;" id="co-qr-amount">199.000đ</p>
      <p class="muted" style="font-size:13px;margin-bottom:4px;">Vietcombank · 1023 4567 8901</p>
      <p class="muted" style="font-size:13px;margin-bottom:20px;">Nội dung: <strong>360H TN</strong></p>
      <div style="display:flex;align-items:center;justify-content:center;gap:8px;margin-bottom:8px;">
        <div style="width:9px;height:9px;border-radius:50%;background:var(--stone);animation:copulse 1.4s infinite;"></div>
        <div style="width:9px;height:9px;border-radius:50%;background:var(--stone);animation:copulse 1.4s 0.45s infinite;"></div>
        <div style="width:9px;height:9px;border-radius:50%;background:var(--stone);animation:copulse 1.4s 0.9s infinite;"></div>
        <span class="muted" style="font-size:14px;margin-left:6px;">Đang chờ xác nhận...</span>
      </div>
      <p class="muted" style="font-size:12px;margin-bottom:20px;">QR hết hạn sau <strong id="co-countdown">15:00</strong></p>
      <div style="display:flex;gap:8px;justify-content:center;flex-wrap:wrap;">
        <button class="btn btn-ghost btn-sm" onclick="coSimulateSuccess()">&#10003; Mô phỏng: Thành công</button>
        <button class="btn btn-ghost btn-sm" onclick="coSimulateFailure()">&#10007; Mô phỏng: Thất bại</button>
      </div>
    </div>
    <div id="co-step2-card" style="display:none;">
      <div style="margin-bottom:16px;"><label style="display:block;font-size:13px;font-weight:500;margin-bottom:6px;">Số thẻ</label><input type="text" placeholder="1234 5678 9012 3456" maxlength="19" oninput="coFormatCard(this)" id="co-card-num"></div>
      <div style="margin-bottom:16px;"><label style="display:block;font-size:13px;font-weight:500;margin-bottom:6px;">Tên chủ thẻ</label><input type="text" placeholder="NGUYEN VAN A" style="text-transform:uppercase;"></div>
      <div style="display:flex;gap:12px;margin-bottom:24px;">
        <div style="flex:1;"><label style="display:block;font-size:13px;font-weight:500;margin-bottom:6px;">Hết hạn</label><input type="text" placeholder="MM/YY" maxlength="5" oninput="coFormatExpiry(this)"></div>
        <div style="flex:1;"><label style="display:block;font-size:13px;font-weight:500;margin-bottom:6px;">CVV</label><input type="password" placeholder="•••" maxlength="3"></div>
      </div>
      <button class="btn btn-gold btn-full btn-lg" id="co-card-pay-btn" onclick="coSubmitCard()">Thanh toán 199.000đ</button>
      <p class="muted" style="font-size:12px;text-align:center;margin-top:12px;">&#128274; Thanh toán bảo mật · SSL 256-bit</p>
    </div>
    <div id="co-step3-success" style="display:none;text-align:center;padding:8px 0;">
      <div style="width:72px;height:72px;border-radius:50%;background:var(--success-bg);display:flex;align-items:center;justify-content:center;margin:0 auto 20px;font-size:32px;color:var(--success);">&#10003;</div>
      <h3 style="font-family:var(--font-heading);margin-bottom:8px;" id="co-success-title">Nâng cấp thành công!</h3>
      <p class="muted" style="margin-bottom:6px;" id="co-success-desc">Chào mừng bạn đến với <strong>360Human PRO</strong>.</p>
      <p class="muted" style="font-size:13px;margin-bottom:28px;">Mã giao dịch: <code style="font-family:var(--font-mono);">#360H-20260321-4822</code></p>
      <button class="btn btn-gold btn-full btn-lg" onclick="closeCheckout();showScreen('s4')">Bắt đầu khám phá →</button>
    </div>
    <div id="co-step3-failure" style="display:none;text-align:center;padding:8px 0;">
      <div style="width:72px;height:72px;border-radius:50%;background:var(--error-bg);display:flex;align-items:center;justify-content:center;margin:0 auto 20px;font-size:32px;color:var(--error);">&#10007;</div>
      <h3 style="font-family:var(--font-heading);margin-bottom:8px;">Thanh toán thất bại</h3>
      <p class="muted" style="margin-bottom:28px;" id="co-error-msg">Giao dịch không thể hoàn thành. Vui lòng thử lại.</p>
      <button class="btn btn-gold btn-full" style="margin-bottom:12px;" onclick="coRetry()">Thử lại</button>
      <p style="font-size:13px;color:var(--stone);">Cần hỗ trợ? <a href="mailto:support@360human.ai" style="color:var(--gold);">Liên hệ →</a></p>
    </div>
    <div id="co-indicators" style="display:flex;justify-content:center;gap:7px;margin-top:24px;">
      <div id="co-ind-1" style="width:8px;height:8px;border-radius:50%;background:var(--ink);transition:background 0.2s;"></div>
      <div id="co-ind-2" style="width:8px;height:8px;border-radius:50%;background:var(--border);transition:background 0.2s;"></div>
      <div id="co-ind-3" style="width:8px;height:8px;border-radius:50%;background:var(--border);transition:background 0.2s;"></div>
    </div>
  </div>
</div>

<!-- FORGOT PASSWORD MODAL -->
<div id="forgot-modal" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,0.6);z-index:3000;align-items:center;justify-content:center;padding:20px;">
  <div class="co-modal" style="max-width:420px;">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:24px;">
      <h3 style="font-family:var(--font-heading);">Quên mật khẩu</h3>
      <button onclick="closeForgotPassword()" style="background:none;border:none;font-size:28px;cursor:pointer;color:var(--stone);">&#215;</button>
    </div>
    <div id="forgot-step1">
      <p class="muted" style="font-size:14px;margin-bottom:20px;">Nhập email của bạn. Chúng tôi sẽ gửi link đặt lại mật khẩu.</p>
      <div class="field"><label>Email</label><input type="email" id="forgot-email" placeholder="email@example.com"></div>
      <button class="btn btn-gold btn-full" onclick="sendForgotPassword()">Gửi link đặt lại</button>
    </div>
    <div id="forgot-step2" style="display:none;text-align:center;padding:16px 0;">
      <div style="font-size:48px;margin-bottom:16px;">&#128236;</div>
      <h3 style="margin-bottom:8px;">Kiểm tra email của bạn</h3>
      <p class="muted" style="font-size:14px;margin-bottom:24px;">Chúng tôi đã gửi link đặt lại mật khẩu đến <strong id="forgot-email-display"></strong></p>
      <button class="btn btn-ghost btn-full" onclick="closeForgotPassword()">Đóng</button>
    </div>
  </div>
</div>

<!-- MOBILE NAV OVERLAY -->
<div class="mob-overlay" id="mob-overlay" onclick="closeMobileNav()"></div>
<div class="mob-sidebar" id="mob-sidebar">
  <button class="mob-close" onclick="closeMobileNav()">&#215;</button>
  <div style="padding:24px 24px 0;">
    <div style="font-family:var(--font-heading);font-size:20px;font-weight:600;margin-bottom:24px;">360Human</div>
    <ul style="list-style:none;">
      <li style="padding:12px 0;cursor:pointer;font-size:16px;border-bottom:1px solid var(--border);" onclick="showScreen('s4');closeMobileNav()">&#9689; Tổng Quan</li>
      <li style="padding:12px 0;cursor:pointer;font-size:16px;border-bottom:1px solid var(--border);" onclick="showScreen('s5');closeMobileNav()">&#11041; Biểu đồ hệ thống</li>
      <li style="padding:12px 0;cursor:pointer;font-size:16px;border-bottom:1px solid var(--border);" onclick="showScreen('s6');closeMobileNav()">&#9678; Phân tích sâu</li>
      <li style="padding:12px 0;cursor:pointer;font-size:16px;border-bottom:1px solid var(--border);" onclick="showScreen('s9');closeMobileNav()">&#9719; Lịch Vận</li>
      <li style="padding:12px 0;cursor:pointer;font-size:16px;border-bottom:1px solid var(--border);" onclick="showScreen('s10');closeMobileNav()">&#9651; Hành động</li>
      <li style="padding:12px 0;cursor:pointer;font-size:16px;border-bottom:1px solid var(--border);" onclick="showScreen('s7');closeMobileNav()">&#10022; Nâng cấp</li>
      <li style="padding:12px 0;cursor:pointer;font-size:16px;" onclick="showScreen('s8');closeMobileNav()">&#9881; Cài đặt</li>
    </ul>
  </div>
</div>
'''

with open(path, 'a', encoding='utf-8') as f:
    f.write(p6)
print('part6 done', len(p6))
