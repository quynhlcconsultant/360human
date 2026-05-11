
path = 'C:/Users/Admin/Desktop/Visionaries_Startup_April/02_Production/Frontend/test/index.html'

p5 = '''
<!-- S9 LICH VAN (TIME ORACLE) -->
<div id="s9" class="screen">
  <div class="app-layout">
    <nav class="sidebar">
      <div class="sidebar-logo">360Human</div>
      <ul class="sidebar-nav">
        <li onclick="showScreen('s4')">&#9689; Tổng Quan</li>
        <li onclick="showScreen('s5')">&#11041; Biểu đồ hệ thống</li>
        <li onclick="showScreen('s6')">&#9678; Phân tích sâu</li>
        <li class="active" onclick="showScreen('s9')">&#9719; Lịch Vận</li>
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
          <span style="font-weight:500;">Lịch Vận</span>
          <span class="badge badge-free" id="s9-tier-badge">FREE</span>
        </div>
      </div>
      <div id="s9-upsell" style="background:var(--gold-bg);border-bottom:1px solid var(--gold);padding:12px 48px;display:flex;justify-content:space-between;align-items:center;">
        <span style="font-size:14px;">Mở khóa Cuộc đời &amp; Năm với PRO</span>
        <button class="btn btn-gold btn-sm" onclick="openCheckout('pro')">Nâng cấp</button>
      </div>
      <div style="padding:32px 48px 80px;">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:24px;">
          <span class="muted" style="font-size:14px;cursor:pointer;" id="bc-lifetime" onclick="s9GoLevel('lifetime')">Cuộc đời</span>
          <span class="muted">›</span>
          <span class="muted" style="font-size:14px;cursor:pointer;" id="bc-year" onclick="s9GoLevel('year')">2026</span>
          <span class="muted">›</span>
          <strong style="font-size:14px;" id="bc-month">Tháng 3</strong>
        </div>
        <!-- Layer 1: Lifetime (PRO only) -->
        <div id="s9-layer1" style="display:none;margin-bottom:32px;">
          <h3 style="margin-bottom:16px;">Bản đồ cuộc đời</h3>
          <div style="position:relative;height:80px;background:var(--sand);border-radius:var(--radius-lg);overflow:hidden;margin-bottom:12px;">
            <div style="position:absolute;left:0;top:0;bottom:0;width:35%;background:var(--border);display:flex;align-items:center;justify-content:center;font-size:12px;color:var(--stone);">Tuổi trẻ (0–27)</div>
            <div style="position:absolute;left:35%;top:0;bottom:0;width:35%;background:var(--gold-bg);border-left:2px solid var(--gold);border-right:2px solid var(--gold);display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:500;">Trưởng thành (27–54) ★</div>
            <div style="position:absolute;right:0;top:0;bottom:0;width:30%;background:var(--border);display:flex;align-items:center;justify-content:center;font-size:12px;color:var(--stone);">Viên mãn (54+)</div>
            <div style="position:absolute;left:37%;top:0;bottom:0;width:2px;background:var(--gold);"></div>
            <div style="position:absolute;left:37%;top:-8px;transform:translateX(-50%);font-size:10px;background:var(--gold);color:white;padding:2px 6px;border-radius:var(--radius-full);">2026</div>
          </div>
          <div class="card" style="padding:16px;">
            <h4 style="margin-bottom:8px;">Giai đoạn Trưởng thành (27–54)</h4>
            <p style="font-size:15px;line-height:1.8;">Đây là giai đoạn xây dựng di sản. Saturn Return đầu tiên của bạn (28–29 tuổi) đã qua — giờ là lúc những nền móng bạn xây được thể hiện thực sự. Đại Vận Đinh Dậu đang chạy — mỗi năm trong 2024–2033 là một gạch nền quan trọng.</p>
            <div class="source" style="margin-top:8px;">nguồn: BaZi (Đại Vận Đinh Dậu) · Vedic (Saturn Dasha)</div>
          </div>
        </div>
        <!-- Layer 2: Year (PRO only) -->
        <div id="s9-layer2" style="display:none;margin-bottom:32px;">
          <div style="display:flex;align-items:center;gap:16px;margin-bottom:16px;">
            <span style="cursor:pointer;color:var(--stone);" onclick="alert('2025')">&#8592; 2025</span>
            <h3>Năm 2026</h3>
            <span style="cursor:pointer;color:var(--stone);" onclick="alert('2027')">2027 &#8594;</span>
          </div>
          <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:16px;">
            <div class="card" style="padding:12px;text-align:center;cursor:pointer;" onclick="s9SelectMonth('T1')"><p style="font-size:13px;font-weight:500;">T1</p><p class="muted" style="font-size:11px;">&#9675;&#9675;&#9675;&#9675;&#9675;</p></div>
            <div class="card" style="padding:12px;text-align:center;cursor:pointer;" onclick="s9SelectMonth('T2')"><p style="font-size:13px;font-weight:500;">T2</p><p class="muted" style="font-size:11px;">&#9679;&#9679;&#9675;&#9675;&#9675;</p></div>
            <div class="card" style="padding:12px;text-align:center;cursor:pointer;border:2px solid var(--gold);background:var(--gold-bg);" onclick="s9SelectMonth('T3')"><p style="font-size:13px;font-weight:600;color:var(--gold);">T3 ★</p><p class="muted" style="font-size:11px;">&#9679;&#9679;&#9679;&#9675;&#9675;</p></div>
            <div class="card" style="padding:12px;text-align:center;cursor:pointer;" onclick="s9SelectMonth('T4')"><p style="font-size:13px;font-weight:500;">T4</p><p class="muted" style="font-size:11px;">&#9679;&#9679;&#9679;&#9679;&#9675;</p></div>
            <div class="card" style="padding:12px;text-align:center;cursor:pointer;" onclick="s9SelectMonth('T5')"><p style="font-size:13px;font-weight:500;">T5</p><p class="muted" style="font-size:11px;">&#9679;&#9679;&#9679;&#9679;&#9679;</p></div>
            <div class="card" style="padding:12px;text-align:center;cursor:pointer;" onclick="s9SelectMonth('T6')"><p style="font-size:13px;font-weight:500;">T6</p><p class="muted" style="font-size:11px;">&#9679;&#9679;&#9679;&#9675;&#9675;</p></div>
            <div class="card" style="padding:12px;text-align:center;cursor:pointer;" onclick="s9SelectMonth('T7')"><p style="font-size:13px;font-weight:500;">T7</p><p class="muted" style="font-size:11px;">&#9679;&#9679;&#9675;&#9675;&#9675;</p></div>
            <div class="card" style="padding:12px;text-align:center;cursor:pointer;" onclick="s9SelectMonth('T8')"><p style="font-size:13px;font-weight:500;">T8</p><p class="muted" style="font-size:11px;">&#9679;&#9679;&#9679;&#9679;&#9675;</p></div>
            <div class="card" style="padding:12px;text-align:center;cursor:pointer;" onclick="s9SelectMonth('T9')"><p style="font-size:13px;font-weight:500;">T9</p><p class="muted" style="font-size:11px;">&#9679;&#9679;&#9679;&#9675;&#9675;</p></div>
            <div class="card" style="padding:12px;text-align:center;cursor:pointer;" onclick="s9SelectMonth('T10')"><p style="font-size:13px;font-weight:500;">T10</p><p class="muted" style="font-size:11px;">&#9679;&#9679;&#9675;&#9675;&#9675;</p></div>
            <div class="card" style="padding:12px;text-align:center;cursor:pointer;" onclick="s9SelectMonth('T11')"><p style="font-size:13px;font-weight:500;">T11</p><p class="muted" style="font-size:11px;">&#9679;&#9679;&#9679;&#9679;&#9675;</p></div>
            <div class="card" style="padding:12px;text-align:center;cursor:pointer;" onclick="s9SelectMonth('T12')"><p style="font-size:13px;font-weight:500;">T12</p><p class="muted" style="font-size:11px;">&#9679;&#9679;&#9679;&#9679;&#9679;</p></div>
          </div>
          <p class="muted" style="font-size:12px;">&#9679; = mức năng lượng · ★ = tháng hiện tại</p>
        </div>
        <!-- Layer 3: Monthly (FREE sees this) -->
        <div style="display:flex;gap:32px;" class="two-col">
          <div style="flex:1;">
            <div style="display:flex;align-items:center;gap:16px;margin-bottom:16px;">
              <span style="cursor:pointer;color:var(--stone);" onclick="alert('Tháng 2')">&#8592; T2</span>
              <h2>Tháng 3, 2026</h2>
              <span style="cursor:pointer;color:var(--stone);" onclick="alert('Tháng 4')">T4 &#8594;</span>
            </div>
            <div class="card">
              <h3 style="font-family:var(--font-heading);margin-bottom:16px;">Tháng của sự tập trung nội tâm</h3>
              <div style="display:flex;flex-direction:column;gap:10px;">
                <div style="display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid var(--border);"><span class="muted" style="font-size:14px;">Năng lượng</span><span style="font-size:16px;">&#9679;&#9679;&#9679;&#9675;&#9675;</span></div>
                <div style="display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid var(--border);"><span class="muted" style="font-size:14px;">Trọng tâm</span><span style="font-size:14px;font-weight:500;">Sự nghiệp &amp; Sáng tạo</span></div>
                <div style="display:flex;justify-content:space-between;align-items:center;padding:8px 0;"><span class="muted" style="font-size:14px;">Tuần cần chú ý</span><span style="font-size:14px;font-weight:500;color:var(--ember);">Tuần 3 (10–16)</span></div>
              </div>
              <div style="margin-top:16px;padding-top:16px;border-top:1px solid var(--border);">
                <p style="font-size:15px;line-height:1.8;">Đây là tháng Personal Year 9 gặp Monthly 3 — năng lượng của sự hoàn thành và kết thúc chu kỳ. Những gì bạn đã bắt đầu từ 2017 đang đến điểm thu hoạch. Tháng 3 với số 3 mang năng lượng sáng tạo và giao tiếp — hãy ưu tiên viết, nói chuyện, và chia sẻ ý tưởng.</p>
              </div>
            </div>
          </div>
          <div style="flex:1.5;">
            <table style="width:100%;border-collapse:collapse;text-align:center;">
              <thead><tr style="color:var(--stone);font-size:13px;">
                <td style="padding:8px;">T2</td><td style="padding:8px;">T3</td><td style="padding:8px;">T4</td>
                <td style="padding:8px;">T5</td><td style="padding:8px;">T6</td><td style="padding:8px;">T7</td><td style="padding:8px;">CN</td>
              </tr></thead>
              <tbody>
                <tr><td colspan="5" style="padding:4px;"></td><td style="padding:12px;cursor:pointer;" class="cal-day">1</td><td style="padding:12px;cursor:pointer;" class="cal-day">2</td></tr>
                <tr style="background:var(--gold-bg);">
                  <td style="padding:12px;cursor:pointer;" class="cal-day">3</td><td style="padding:12px;cursor:pointer;" class="cal-day">4</td><td style="padding:12px;cursor:pointer;" class="cal-day">5</td><td style="padding:12px;cursor:pointer;" class="cal-day">6</td><td style="padding:12px;cursor:pointer;" class="cal-day">7</td><td style="padding:12px;cursor:pointer;" class="cal-day">8</td><td style="padding:12px;cursor:pointer;" class="cal-day">9</td>
                </tr>
                <tr style="background:var(--ember-bg);">
                  <td style="padding:12px;cursor:pointer;" class="cal-day">10</td><td style="padding:12px;cursor:pointer;" class="cal-day">11</td><td style="padding:12px;cursor:pointer;" class="cal-day">12</td><td style="padding:12px;cursor:pointer;" class="cal-day">13</td><td style="padding:12px;cursor:pointer;" class="cal-day">14</td><td style="padding:12px;cursor:pointer;" class="cal-day">15</td><td style="padding:12px;cursor:pointer;" class="cal-day">16</td>
                </tr>
                <tr>
                  <td style="padding:12px;font-weight:700;color:var(--gold);cursor:pointer;" class="cal-day">17</td><td style="padding:12px;cursor:pointer;" class="cal-day">18</td><td style="padding:12px;cursor:pointer;" class="cal-day">19</td><td style="padding:12px;cursor:pointer;" class="cal-day">20</td><td style="padding:12px;cursor:pointer;" class="cal-day">21</td><td style="padding:12px;cursor:pointer;" class="cal-day">22</td><td style="padding:12px;cursor:pointer;" class="cal-day">23</td>
                </tr>
                <tr>
                  <td style="padding:12px;cursor:pointer;" class="cal-day">24</td><td style="padding:12px;cursor:pointer;" class="cal-day">25</td><td style="padding:12px;cursor:pointer;" class="cal-day">26</td><td style="padding:12px;cursor:pointer;" class="cal-day">27</td><td style="padding:12px;cursor:pointer;" class="cal-day">28</td><td style="padding:12px;cursor:pointer;" class="cal-day">29</td><td style="padding:12px;cursor:pointer;" class="cal-day">30</td>
                </tr>
              </tbody>
            </table>
            <div class="card" style="margin-top:16px;">
              <div class="source" style="margin-bottom:8px;">Tuần 17–23/03/2026</div>
              <p style="font-size:15px;margin-bottom:8px;">Năng lượng tập trung cao — lý tưởng cho quyết định quan trọng. <span style="color:var(--gold);">★ Ngày 21 đặc biệt thuận lợi</span> cho khởi động và ký kết.</p>
              <div style="display:flex;gap:6px;flex-wrap:wrap;"><span class="badge-system">Tập trung</span><span class="badge-system">Sáng tạo</span><span class="badge-system">Kết nối</span></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- S10 ACTIONS -->
<div id="s10" class="screen">
  <div class="app-layout">
    <nav class="sidebar">
      <div class="sidebar-logo">360Human</div>
      <ul class="sidebar-nav">
        <li onclick="showScreen('s4')">&#9689; Tổng Quan</li>
        <li onclick="showScreen('s5')">&#11041; Biểu đồ hệ thống</li>
        <li onclick="showScreen('s6')">&#9678; Phân tích sâu</li>
        <li onclick="showScreen('s9')">&#9719; Lịch Vận</li>
        <li class="active" onclick="showScreen('s10')">&#9651; Hành động</li>
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
          <span style="font-weight:500;">Hành động</span>
          <span class="badge badge-free" id="s10-tier-badge">FREE</span>
        </div>
      </div>
      <div style="display:flex;gap:0;" class="two-col">
        <div style="flex:1;padding:32px 32px 80px 48px;border-right:1px solid var(--border);">
          <div style="text-align:center;margin-bottom:24px;">
            <svg viewBox="0 0 300 200" style="width:260px;" id="s10-pyramid">
              <polygon points="150,20 260,180 40,180" fill="none" stroke="var(--border)" stroke-width="2"/>
              <line x1="90" y1="120" x2="210" y2="120" stroke="var(--border)" stroke-width="1.5"/>
              <line x1="115" y1="70" x2="185" y2="70" stroke="var(--border)" stroke-width="1.5"/>
              <polygon points="40,180 260,180 210,120 90,120" fill="var(--gold-bg)" fill-opacity="0.7" stroke="var(--gold)" stroke-width="2" id="pyr-base" style="cursor:pointer;" onclick="s10SelectLayer('base')"/>
              <polygon points="90,120 210,120 185,70 115,70" fill="none" stroke="var(--border)" stroke-width="1.5" id="pyr-mid" style="cursor:pointer;" onclick="s10SelectLayer('mid')"/>
              <polygon points="115,70 185,70 150,20" fill="none" stroke="var(--border)" stroke-width="1.5" id="pyr-top" style="cursor:pointer;" onclick="s10SelectLayer('top')"/>
              <text x="150" y="43" text-anchor="middle" style="font-size:10px;fill:var(--stone);" id="pyr-top-label">Khai Phóng &#128274;</text>
              <text x="150" y="100" text-anchor="middle" style="font-size:10px;fill:var(--stone);" id="pyr-mid-label">Nuôi Dưỡng &#128274;</text>
              <text x="150" y="160" text-anchor="middle" style="font-size:12px;fill:var(--gold);font-weight:600;" id="pyr-base-label">Nền Móng ★</text>
            </svg>
          </div>
          <div id="s10-actions-base">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;"><h3>Nền Móng</h3><span style="font-size:13px;color:var(--stone);" id="s10-base-count">0/2</span></div>
            <div class="progress-bar" style="margin-bottom:16px;width:160px;"><div class="fill" style="width:0%" id="s10-base-progress"></div></div>
            <div style="display:flex;flex-direction:column;gap:12px;">
              <div class="card" style="padding:16px;cursor:pointer;" onclick="s10SelectAction(1)" id="s10-action-1">
                <div style="display:flex;align-items:start;gap:12px;"><input type="checkbox" style="width:auto;margin-top:4px;" onchange="updateActionProgress(this,1)"><div style="flex:1;"><strong style="font-size:14px;">1. Dành 10 phút mỗi sáng viết nhật ký</strong><p class="muted" style="font-size:13px;margin-top:4px;">Quan sát mâu thuẫn nội tại — viết ra, không phán xét</p></div><span class="badge-system">BaZi</span></div>
              </div>
              <div class="card" style="padding:16px;cursor:pointer;" onclick="s10SelectAction(2)" id="s10-action-2">
                <div style="display:flex;align-items:start;gap:12px;"><input type="checkbox" style="width:auto;margin-top:4px;" onchange="updateActionProgress(this,2)"><div style="flex:1;"><strong style="font-size:14px;">2. Nói "không" ít nhất 1 lần/tuần</strong><p class="muted" style="font-size:13px;margin-top:4px;">Tham Lang dễ thu hút — nhưng cần chọn lọc</p></div><span class="badge-system">Tử Vi</span></div>
              </div>
            </div>
          </div>
          <div id="s10-actions-mid" style="display:none;margin-top:24px;">
            <h3 style="margin-bottom:8px;">Nuôi Dưỡng</h3>
            <div class="progress-bar" style="margin-bottom:16px;width:160px;"><div class="fill" style="width:33%"></div></div>
            <div style="display:flex;flex-direction:column;gap:12px;">
              <div class="card" style="padding:16px;cursor:pointer;" onclick="s10SelectAction(3)"><div style="display:flex;align-items:start;gap:12px;"><input type="checkbox" checked style="width:auto;margin-top:4px;"><div style="flex:1;"><strong style="font-size:14px;">3. Thực hành Sacral response</strong><p class="muted" style="font-size:13px;margin-top:4px;">Trước mỗi cam kết lớn, hỏi bản thân: Uh-huh hay Uh-uh?</p></div><span class="badge-system">HD</span></div></div>
              <div class="card" style="padding:16px;cursor:pointer;" onclick="s10SelectAction(4)"><div style="display:flex;align-items:start;gap:12px;"><input type="checkbox" style="width:auto;margin-top:4px;"><div style="flex:1;"><strong style="font-size:14px;">4. Xây dựng "năng lượng solo" hàng tuần</strong><p class="muted" style="font-size:13px;margin-top:4px;">Ít nhất 2 giờ/tuần hoàn toàn một mình, không điện thoại</p></div><span class="badge-system">HD</span></div></div>
              <div class="card" style="padding:16px;cursor:pointer;" onclick="s10SelectAction(5)"><div style="display:flex;align-items:start;gap:12px;"><input type="checkbox" style="width:auto;margin-top:4px;"><div style="flex:1;"><strong style="font-size:14px;">5. Học một kỹ năng chuyên sâu mỗi quý</strong><p class="muted" style="font-size:13px;margin-top:4px;">Life Path 7 phát triển qua chiều sâu, không qua chiều rộng</p></div><span class="badge-system">Số học</span></div></div>
            </div>
          </div>
          <div id="s10-actions-top" style="display:none;margin-top:24px;">
            <h3 style="margin-bottom:8px;">Khai Phóng</h3>
            <div class="progress-bar" style="margin-bottom:16px;width:160px;"><div class="fill" style="width:0%"></div></div>
            <div style="display:flex;flex-direction:column;gap:12px;">
              <div class="card" style="padding:16px;cursor:pointer;border:2px solid var(--ink);" onclick="s10SelectAction(6)"><div style="display:flex;align-items:start;gap:12px;"><input type="checkbox" style="width:auto;margin-top:4px;"><div style="flex:1;"><strong style="font-size:14px;">6. Định nghĩa lại thành công theo điều kiện của bạn</strong><p class="muted" style="font-size:13px;margin-top:4px;">Viết một tuyên ngôn cá nhân — không so sánh với người khác</p></div><span class="badge-system">Tổng hợp</span></div></div>
              <div class="card" style="padding:16px;cursor:pointer;" onclick="s10SelectAction(7)"><div style="display:flex;align-items:start;gap:12px;"><input type="checkbox" style="width:auto;margin-top:4px;"><div style="flex:1;"><strong style="font-size:14px;">7. Tạo ra một thứ để lại di sản</strong><p class="muted" style="font-size:13px;margin-top:4px;">Soul Urge 9 cần cống hiến — bắt đầu một dự án có ý nghĩa</p></div><span class="badge-system">Số học</span></div></div>
            </div>
          </div>
          <div id="s10-upsell" style="margin-top:24px;padding:16px;background:var(--sand);border-radius:var(--radius-lg);text-align:center;">
            <p class="muted" style="font-size:14px;">Mở khóa Nuôi Dưỡng &amp; Khai Phóng với <a href="#" style="color:var(--gold);" onclick="openCheckout('pro');return false;">PRO</a></p>
          </div>
        </div>
        <div style="flex:1;padding:32px 48px 32px 32px;" id="s10-detail">
          <div class="card" style="margin-bottom:16px;">
            <h4 style="margin-bottom:12px;color:var(--stone);">WHAT — Từ đặc điểm nào?</h4>
            <p style="font-size:15px;line-height:1.8;" id="s10-what-text">Chọn một hành động để xem giải thích chi tiết →</p>
          </div>
          <div class="card">
            <h4 style="margin-bottom:12px;color:var(--stone);">WHY — Từ hệ thống nào?</h4>
            <div id="s10-why-content"><p style="font-size:15px;line-height:1.8;color:var(--stone);">Chọn một hành động để xem nguồn gốc từ hệ thống nào →</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- DEV NAV BAR (tier toggle only) -->
<div class="dev-nav">
  <button class="tier-toggle free" id="tier-toggle-btn" onclick="cycleTier()">Tier: FREE</button>
</div>
'''

with open(path, 'a', encoding='utf-8') as f:
    f.write(p5)
print('part5 done', len(p5))
