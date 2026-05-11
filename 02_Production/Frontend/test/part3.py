
path = 'C:/Users/Admin/Desktop/Visionaries_Startup_April/02_Production/Frontend/test/index.html'

p3 = '''
<!-- S5 SYSTEM READING -->
<div id="s5" class="screen">
  <div class="app-layout">
    <nav class="sidebar">
      <div class="sidebar-logo">360Human</div>
      <ul class="sidebar-nav">
        <li onclick="showScreen('s4')">&#9689; Tổng Quan</li>
        <li class="active" onclick="showScreen('s5')">&#11041; Biểu đồ hệ thống</li>
        <li onclick="showScreen('s6')">&#9678; Phân tích sâu</li>
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
          <span style="font-weight:500;" id="s5-breadcrumb">Tử Vi</span>
        </div>
        <div class="topbar-right"><span class="badge badge-pro" id="s5-tier-badge">PRO</span></div>
      </div>
      <div class="tabs" style="padding:0 48px;" id="s5-tabs">
        <div class="tab active" onclick="switchS5Tab(this,'tu-vi')" data-tab="tu-vi">Tử Vi</div>
        <div class="tab" onclick="switchS5Tab(this,'bazi')" data-tab="bazi">BaZi</div>
        <div class="tab" onclick="switchS5Tab(this,'hd')" data-tab="hd">Human Design</div>
        <div class="tab" onclick="switchS5Tab(this,'numerology')" data-tab="numerology">Số học</div>
        <div class="tab" onclick="switchS5Tab(this,'vedic')" data-tab="vedic">Vedic</div>
      </div>

      <!-- TỬ VI TAB -->
      <div class="tab-panel active" id="panel-tu-vi">
        <div style="display:flex;gap:0;" class="two-col">
          <div style="flex:1;padding:32px 32px 32px 48px;border-right:1px solid var(--border);">
            <h3 style="margin-bottom:16px;">Lá số Tử Vi — Thảo Nguyễn</h3>
            <!-- 4x4 palace grid -->
            <div class="palace-grid" style="max-width:420px;">
              <!-- Row 1: Tỵ, Ngọ, Mùi, Thân -->
              <div class="palace">
                <span class="palace-name">Tỵ — Nô Bộc</span>
                <div class="palace-stars">Thiên Tướng<br>Thiên Việt</div>
              </div>
              <div class="palace" style="background:var(--gold-bg);border:2px solid var(--gold);">
                <span class="palace-name" style="color:var(--gold);">Ngọ — Quan Lộc ★</span>
                <div class="palace-stars" style="color:var(--gold);">Tử Vi ★<br>Thiên Phủ<br><em style="font-size:9px;">Hóa Quyền</em></div>
              </div>
              <div class="palace">
                <span class="palace-name">Mùi — Điền Trạch</span>
                <div class="palace-stars">Vũ Khúc<br>Thiên Tướng</div>
              </div>
              <div class="palace">
                <span class="palace-name">Thân — Phúc Đức</span>
                <div class="palace-stars">Thái Âm ★<br><em style="font-size:9px;">Hóa Lộc</em><br>Thiên Đồng</div>
              </div>
              <!-- Row 2: Thìn, [CENTER 2x2], Dậu -->
              <div class="palace">
                <span class="palace-name">Thìn — Thiên Di</span>
                <div class="palace-stars">Thái Dương (miếu)<br><em style="font-size:9px;">Hóa Khoa</em></div>
              </div>
              <div class="palace-center" style="grid-column:span 2;grid-row:span 2;">
                <div>
                  <div style="font-family:var(--font-heading);font-size:15px;font-weight:600;margin-bottom:4px;">Thảo Nguyễn</div>
                  <div class="source" style="font-size:11px;">15.06.1997</div>
                  <div class="source" style="font-size:11px;">Canh Kim · Mệnh Tuất</div>
                  <div style="margin-top:8px;font-size:11px;color:var(--charcoal);">Mệnh Chủ: Văn Khúc</div>
                  <div style="font-size:11px;color:var(--charcoal);">Thân Cung: Thân</div>
                  <div style="font-size:11px;color:var(--charcoal);">Hành năm: Kim</div>
                </div>
              </div>
              <div class="palace">
                <span class="palace-name">Dậu — Phụ Mẫu</span>
                <div class="palace-stars">Thiên Phủ</div>
              </div>
              <!-- Row 3: Mão, [continues center], Tuất -->
              <div class="palace">
                <span class="palace-name">Mão — Tật Ách</span>
                <div class="palace-stars">Thiên Lương<br>Thiên Giải</div>
              </div>
              <div class="palace menh">
                <span class="palace-name" style="color:var(--gold);">Tuất — ★ Mệnh</span>
                <div class="palace-stars" style="color:var(--gold);">Tham Lang (miếu) ★<br>Cự Môn</div>
              </div>
              <!-- Row 4: Dần, Sửu, Tý, Hợi -->
              <div class="palace">
                <span class="palace-name">Dần — Tài Bạch</span>
                <div class="palace-stars">Phá Quân<br>Liêm Trinh</div>
              </div>
              <div class="palace">
                <span class="palace-name">Sửu — Tử Tức</span>
                <div class="palace-stars">Cự Môn<br><em style="font-size:9px;">Hóa Kị</em><br>Thiên Cơ</div>
              </div>
              <div class="palace">
                <span class="palace-name">Tý — Phu Thê</span>
                <div class="palace-stars">Thiên Cơ<br>Thiên Khôi</div>
              </div>
              <div class="palace">
                <span class="palace-name">Hợi — Huynh Đệ</span>
                <div class="palace-stars">Thiên Đồng<br>Văn Xương</div>
              </div>
            </div>
            <p class="source" style="margin-top:10px;">Click cung để xem chi tiết · ★ = cung đặc biệt</p>

            <!-- Tứ Hóa table -->
            <div style="margin-top:20px;">
              <h4 style="margin-bottom:10px;">Tứ Hóa — Biến hóa năm Canh</h4>
              <table class="sys-table">
                <thead><tr><th>Biến hóa</th><th>Sao</th><th>Ý nghĩa</th></tr></thead>
                <tbody>
                  <tr><td><span style="color:var(--sage);font-weight:600;">Hóa Lộc</span></td><td>Thái Âm</td><td>Tài lộc, nữ tính flourish</td></tr>
                  <tr><td><span style="color:var(--gold);font-weight:600;">Hóa Quyền</span></td><td>Tử Vi</td><td>Quyền lực, chủ động</td></tr>
                  <tr><td><span style="color:var(--charcoal);font-weight:600;">Hóa Khoa</span></td><td>Thái Dương</td><td>Danh tiếng, học vấn</td></tr>
                  <tr><td><span style="color:var(--ember);font-weight:600;">Hóa Kị</span></td><td>Cự Môn</td><td>Khẩu thiệt, giao tiếp cẩn thận</td></tr>
                </tbody>
              </table>
            </div>
          </div>
          <div style="flex:1;padding:32px 48px 32px 32px;">
            <h3 style="margin-bottom:16px;">Tham Lang miếu địa tại Cung Mệnh</h3>
            <div class="reading-text">
              <p style="margin-bottom:16px;">Tham Lang là ngôi sao của sức hút, đa tài, và tham vọng. Khi ở miếu địa (vị trí mạnh nhất), sức ảnh hưởng tự nhiên — không cần cố gắng. Tham Lang miếu tại Tuất tạo ra người có vẻ ngoài thu hút, giỏi giao tiếp, và có khả năng tạo ra kết nối bền chặt.</p>
              <p style="margin-bottom:16px;">Nhưng Tham Lang miếu địa cũng mang nghĩa: bạn dễ phân tán năng lượng vào quá nhiều hướng. Sức hút lớn = nhiều cơ hội = khó chọn lọc. Bài học quan trọng nhất của Tham Lang là học cách từ chối đúng thứ để tập trung vào đúng thứ.</p>
              <p style="margin-bottom:16px;">Cung Quan Lộc có Tử Vi sao với Hóa Quyền — đây là dấu ấn của người lãnh đạo và tạo ra hệ thống. Sự nghiệp phát triển mạnh nhất khi bạn ở vị trí chủ động, không phụ thuộc vào ai.</p>
              <div class="source">nguồn: Tử Vi — Cung Mệnh tại Tuất · Tứ Hóa năm Canh</div>
            </div>
            <div style="margin-top:24px;padding-top:24px;border-top:1px solid var(--border);">
              <h4 style="margin-bottom:12px;">Hỏi về Tử Vi</h4>
              <div style="display:flex;gap:8px;">
                <input type="text" id="s5-tuvi-input" placeholder="VD: Tham Lang nghĩa là gì với sự nghiệp?" style="flex:1;" onkeydown="if(event.key==='Enter')sendQA('s5-tuvi')">
                <button class="btn btn-gold btn-sm" onclick="sendQA('s5-tuvi')">Gửi</button>
              </div>
              <div id="s5-tuvi-result" style="display:none;"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- BAZI TAB -->
      <div class="tab-panel" id="panel-bazi">
        <div style="display:flex;gap:0;" class="two-col">
          <div style="flex:1;padding:32px 32px 32px 48px;border-right:1px solid var(--border);">
            <h3 style="margin-bottom:16px;">Tứ Trụ — BaZi</h3>
            <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;max-width:400px;margin-bottom:16px;">
              <div style="text-align:center;"><p class="muted" style="font-size:12px;margin-bottom:8px;">Giờ</p>
                <div class="card" style="padding:12px;">
                  <div style="font-size:18px;font-weight:600;font-family:var(--font-heading);">Nhâm</div>
                  <div class="source">Ngọ</div>
                  <div style="font-size:10px;color:var(--stone);margin-top:4px;">Thực Thần</div>
                </div>
              </div>
              <div style="text-align:center;"><p class="muted" style="font-size:12px;margin-bottom:8px;">Ngày ★</p>
                <div class="card" style="padding:12px;border:2px solid var(--gold);">
                  <div style="font-size:18px;font-weight:600;font-family:var(--font-heading);color:var(--gold);">Canh</div>
                  <div class="source" style="color:var(--gold);">Ngọ ★</div>
                  <div style="font-size:10px;color:var(--gold);margin-top:4px;">Nhật Chủ</div>
                </div>
              </div>
              <div style="text-align:center;"><p class="muted" style="font-size:12px;margin-bottom:8px;">Tháng</p>
                <div class="card" style="padding:12px;">
                  <div style="font-size:18px;font-weight:600;font-family:var(--font-heading);">Đinh</div>
                  <div class="source">Mùi</div>
                  <div style="font-size:10px;color:var(--stone);margin-top:4px;">Chính Quan</div>
                </div>
              </div>
              <div style="text-align:center;"><p class="muted" style="font-size:12px;margin-bottom:8px;">Năm</p>
                <div class="card" style="padding:12px;">
                  <div style="font-size:18px;font-weight:600;font-family:var(--font-heading);">Đinh</div>
                  <div class="source">Sửu</div>
                  <div style="font-size:10px;color:var(--stone);margin-top:4px;">Chính Quan</div>
                </div>
              </div>
            </div>
            <div style="padding:12px;background:var(--sand);border-radius:var(--radius-md);margin-bottom:16px;">
              <p style="font-size:13px;"><strong>Nhật Chủ:</strong> Canh Kim · <strong>Dụng Thần:</strong> Thủy · <strong>Kỵ Thần:</strong> Hỏa</p>
            </div>

            <!-- Thập Thần table -->
            <h4 style="margin-bottom:10px;">Thập Thần trong Tứ Trụ</h4>
            <table class="sys-table" style="margin-bottom:16px;">
              <thead><tr><th>Trụ</th><th>Can Chi</th><th>Thập Thần</th></tr></thead>
              <tbody>
                <tr><td>Giờ</td><td>Nhâm-Ngọ</td><td>Thực Thần</td></tr>
                <tr><td style="color:var(--gold);font-weight:600;">Ngày ★</td><td style="color:var(--gold);">Canh-Ngọ</td><td style="color:var(--gold);">Nhật Chủ</td></tr>
                <tr><td>Tháng</td><td>Đinh-Mùi</td><td>Chính Quan</td></tr>
                <tr><td>Năm</td><td>Đinh-Sửu</td><td>Chính Quan</td></tr>
              </tbody>
            </table>

            <!-- Đại Vận table -->
            <h4 style="margin-bottom:10px;">Đại Vận</h4>
            <table class="sys-table" style="margin-bottom:16px;">
              <thead><tr><th>#</th><th>Can Chi</th><th>Năm</th><th>Tuổi</th><th>Đặc trưng</th></tr></thead>
              <tbody>
                <tr><td>1</td><td>Bính Ngọ</td><td>2007–2016</td><td>10–19</td><td>Phát triển tư duy</td></tr>
                <tr><td>2</td><td>Ất Tỵ</td><td>2017–2026</td><td>20–29</td><td>Học hỏi, thử nghiệm</td></tr>
                <tr style="background:var(--gold-bg);"><td style="color:var(--gold);font-weight:600;">3 ★</td><td style="color:var(--gold);">Đinh Dậu</td><td>2024–2033</td><td>27–36</td><td style="color:var(--gold);">★ Hiện tại: tích lũy</td></tr>
                <tr><td>4</td><td>Mậu Tuất</td><td>2034–2043</td><td>37–46</td><td>Xây dựng vị thế</td></tr>
                <tr><td>5</td><td>Kỷ Hợi</td><td>2044–2053</td><td>47–56</td><td>Thu hoạch thành quả</td></tr>
              </tbody>
            </table>

            <!-- Thần Sát -->
            <h4 style="margin-bottom:8px;">Thần Sát &amp; Xung Hình</h4>
            <div style="display:flex;flex-wrap:wrap;gap:6px;margin-bottom:8px;">
              <span class="badge-system">Thiên Đức (Mùi)</span>
              <span class="badge-system">Nguyệt Đức (Sửu)</span>
              <span class="badge-system">Thiên Ất Quý Nhân (Sửu, Mùi)</span>
              <span class="badge-system" style="color:var(--ember);">Không Vong (Thìn, Tỵ)</span>
            </div>
            <p style="font-size:12px;color:var(--stone);">Xung: Ngọ-Ngọ tự hình (2 Ngọ trong trụ ngày-giờ)</p>
          </div>
          <div style="flex:1;padding:32px 48px 32px 32px;">
            <h3 style="margin-bottom:16px;">Canh Kim Nhật Chủ — Kiếm trong lửa</h3>
            <div class="reading-text">
              <p style="margin-bottom:16px;">Canh Kim là kim loại cứng nhất — thanh kiếm, búa rìu. Bạn có bản chất cương nghị, nguyên tắc, và không dễ bị bẻ cong. Khi đã cam kết với điều gì, bạn có thể duy trì đến cùng — đây là điểm mạnh nhưng cũng là nguồn gốc của sự cứng nhắc đôi khi không cần thiết.</p>
              <p style="margin-bottom:16px;">Ngọn lửa đôi Ngọ trong trụ ngày và trụ giờ tạo ra áp lực liên tục. Canh Kim gặp Hỏa = bị tôi luyện. Cuộc đời bạn là quá trình tôi luyện có chủ đích — mỗi khó khăn là một lần nung nóng để tạo ra độ sắc bén cao hơn.</p>
              <p style="margin-bottom:16px;"><strong>Dụng Thần Thủy</strong> — Thủy làm mát Kim, dẫn năng lượng đi đúng hướng. Môi trường và con người mang hành Thủy (người sinh năm Nhâm, Quý, Hợi, Tý) sẽ giúp bạn phát huy tốt nhất. Tránh môi trường Hỏa cường quá mức — áp lực quá lớn mà không có thời gian phục hồi sẽ làm mòn chứ không tôi luyện.</p>
              <p style="margin-bottom:16px;"><strong>Chính Quan đôi</strong> (Đinh tại Tháng và Năm) — bạn sống trong môi trường có nhiều quy tắc và kỳ vọng xã hội. Học cách phân biệt quy tắc nào phục vụ bạn và quy tắc nào chỉ là gánh nặng mang theo từ quá khứ.</p>
              <div class="source">nguồn: BaZi — Tứ Trụ phân tích · Thập Thần · Đại Vận</div>
            </div>
            <div style="margin-top:24px;padding-top:24px;border-top:1px solid var(--border);">
              <h4 style="margin-bottom:12px;">Hỏi về BaZi</h4>
              <div style="display:flex;gap:8px;">
                <input type="text" id="s5-bazi-input" placeholder="VD: Năm 2026 có tốt cho tôi không?" style="flex:1;" onkeydown="if(event.key==='Enter')sendQA('s5-bazi')">
                <button class="btn btn-gold btn-sm" onclick="sendQA('s5-bazi')">Gửi</button>
              </div>
              <div id="s5-bazi-result" style="display:none;"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- HUMAN DESIGN TAB -->
      <div class="tab-panel" id="panel-hd">
        <div style="display:flex;gap:0;" class="two-col">
          <div style="flex:1;padding:32px 32px 32px 48px;border-right:1px solid var(--border);">
            <h3 style="margin-bottom:16px;">Bodygraph — Human Design</h3>
            <!-- Main card -->
            <div class="card" style="padding:16px;margin-bottom:12px;max-width:380px;">
              <table style="width:100%;font-size:13px;">
                <tr><td style="color:var(--stone);padding:4px 0;width:45%;">Type</td><td style="font-weight:600;">Manifesting Generator</td></tr>
                <tr><td style="color:var(--stone);padding:4px 0;">Strategy</td><td>Respond, then initiate</td></tr>
                <tr><td style="color:var(--stone);padding:4px 0;">Authority</td><td>Emotional Solar Plexus</td></tr>
                <tr><td style="color:var(--stone);padding:4px 0;">Profile</td><td style="font-weight:600;">4/6 — Opportunist / Role Model</td></tr>
                <tr><td style="color:var(--stone);padding:4px 0;">Definition</td><td>Split (2 definitions)</td></tr>
                <tr><td style="color:var(--stone);padding:4px 0;">Not-Self Theme</td><td style="color:var(--ember);">Frustration &amp; Anger</td></tr>
                <tr><td style="color:var(--stone);padding:4px 0;">Incarnation Cross</td><td>Right Angle Cross of Explanation</td></tr>
              </table>
            </div>

            <!-- 9 Centers -->
            <h4 style="margin-bottom:10px;">9 Trung tâm năng lượng</h4>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;max-width:380px;margin-bottom:16px;">
              <div class="hd-center defined"><div class="hd-dot"></div>HEAD (Đầu)</div>
              <div class="hd-center defined"><div class="hd-dot"></div>AJNA (Tư duy)</div>
              <div class="hd-center defined"><div class="hd-dot"></div>THROAT (Biểu đạt)</div>
              <div class="hd-center undefined"><div class="hd-dot"></div>G CENTER (Bản sắc)</div>
              <div class="hd-center undefined"><div class="hd-dot"></div>HEART/WILL (Ý chí)</div>
              <div class="hd-center defined"><div class="hd-dot"></div>SOLAR PLEXUS (Cảm xúc)</div>
              <div class="hd-center undefined"><div class="hd-dot"></div>SACRAL (Năng lượng gốc)</div>
              <div class="hd-center undefined"><div class="hd-dot"></div>SPLEEN (Trực giác)</div>
              <div class="hd-center undefined"><div class="hd-dot"></div>ROOT (Áp lực gốc)</div>
            </div>
            <p class="muted" style="font-size:11px;margin-bottom:16px;">&#9632; Defined (tối) = năng lượng ổn định · &#9633; Undefined (nhạt) = năng lượng linh hoạt</p>

            <!-- Active Channels -->
            <h4 style="margin-bottom:10px;">Channels kích hoạt</h4>
            <div style="display:flex;flex-direction:column;gap:6px;max-width:380px;">
              <div style="padding:8px 12px;background:var(--sand);border-radius:var(--radius-sm);font-size:12px;">
                <strong>43-23 Structuring</strong> <span class="muted">(Head→Throat)</span><br>
                <span style="color:var(--charcoal);">Cá tính riêng biệt, insight độc lập</span>
              </div>
              <div style="padding:8px 12px;background:var(--sand);border-radius:var(--radius-sm);font-size:12px;">
                <strong>35-36 Transitoriness</strong> <span class="muted">(Throat→Solar Plexus)</span><br>
                <span style="color:var(--charcoal);">Kinh nghiệm cảm xúc, ham muốn trải nghiệm</span>
              </div>
              <div style="padding:8px 12px;background:var(--sand);border-radius:var(--radius-sm);font-size:12px;">
                <strong>19-49 Synthesis</strong> <span class="muted">(Root→Solar Plexus)</span><br>
                <span style="color:var(--charcoal);">Nhạy cảm với nhu cầu người khác</span>
              </div>
            </div>
          </div>
          <div style="flex:1;padding:32px 48px 32px 32px;">
            <h3 style="margin-bottom:16px;">Manifesting Generator — Người đa năng</h3>
            <div class="reading-text">
              <p style="margin-bottom:16px;">Là Manifesting Generator, bạn được thiết kế để làm nhiều thứ cùng lúc — và làm tốt. Đừng cố gắng đơn giản hóa bản thân để phù hợp với lời khuyên "chỉ tập trung một thứ". Đó là lời khuyên đúng cho nhiều kiểu người, nhưng không phải cho bạn. Bạn được thiết kế để đa nhiệm có chủ đích.</p>
              <p style="margin-bottom:16px;"><strong>Profile 4/6 — Opportunist / Role Model:</strong> Line 4 nghĩa là bạn xây dựng cơ hội qua mạng lưới quan hệ cá nhân gần gũi — không phải qua việc gặp người lạ liên tục, mà qua việc đào sâu vào các mối quan hệ hiện có. Line 6 nghĩa là bạn đang trong giai đoạn "trên mái nhà" (khoảng 28-50 tuổi) — quan sát, học hỏi, trước khi trở thành Role Model thật sự trong nửa sau cuộc đời.</p>
              <p style="margin-bottom:16px;"><strong>Emotional Authority:</strong> Đây là điều quan trọng nhất. Bạn KHÔNG nên ra quyết định trong trạng thái cảm xúc cao — dù là hưng phấn hay lo lắng. Hãy chờ đến khi cảm xúc lắng xuống và bạn cảm thấy rõ ràng. Câu hỏi đúng không phải "Tôi có muốn không?" mà là "Sau 3 ngày, tôi vẫn muốn điều này không?"</p>
              <p style="margin-bottom:16px;">Channel 43-23 (Structuring) cho thấy bạn có những insight rất độc lập, đôi khi khó giải thích ngay lập tức. Đây là dấu hiệu của người tư duy theo cách riêng — hãy tin tưởng vào quá trình đó, ngay cả khi người khác chưa hiểu ngay.</p>
              <div class="source">nguồn: Human Design — Type, Authority, Profile, Centers, Channels</div>
            </div>
            <div style="margin-top:24px;padding-top:24px;border-top:1px solid var(--border);">
              <h4 style="margin-bottom:12px;">Hỏi về Human Design</h4>
              <div style="display:flex;gap:8px;">
                <input type="text" id="s5-hd-input" placeholder="VD: Authority của tôi hoạt động thế nào?" style="flex:1;" onkeydown="if(event.key==='Enter')sendQA('s5-hd')">
                <button class="btn btn-gold btn-sm" onclick="sendQA('s5-hd')">Gửi</button>
              </div>
              <div id="s5-hd-result" style="display:none;"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- NUMEROLOGY TAB -->
      <div class="tab-panel" id="panel-numerology">
        <div style="display:flex;gap:0;" class="two-col">
          <div style="flex:1;padding:32px 32px 32px 48px;border-right:1px solid var(--border);">
            <h3 style="margin-bottom:16px;">Bản đồ số — Số học Pythagorean</h3>

            <!-- Core numbers -->
            <h4 style="margin-bottom:10px;">Số cốt lõi</h4>
            <table class="sys-table" style="max-width:380px;margin-bottom:16px;">
              <thead><tr><th>Số</th><th>Giá trị</th><th>Ý nghĩa</th></tr></thead>
              <tbody>
                <tr style="background:var(--gold-bg);"><td style="color:var(--gold);font-weight:600;">Life Path</td><td style="font-size:18px;font-weight:700;font-family:var(--font-heading);color:var(--gold);">7</td><td>Người Tìm Kiếm</td></tr>
                <tr><td>Expression</td><td style="font-size:16px;font-weight:600;">3</td><td>Người Truyền Đạt</td></tr>
                <tr><td>Soul Urge</td><td style="font-size:16px;font-weight:600;">9</td><td>Người Cống Hiến</td></tr>
                <tr><td>Personality</td><td style="font-size:16px;font-weight:600;">3</td><td>Năng động, sáng tạo</td></tr>
                <tr><td>Birthday</td><td style="font-size:16px;font-weight:600;">6</td><td>15→6 · Hòa hợp</td></tr>
                <tr><td>Maturity</td><td style="font-size:16px;font-weight:600;">1</td><td>7+3=10→1 · Tiên phong</td></tr>
              </tbody>
            </table>

            <!-- 4 Pinnacles -->
            <h4 style="margin-bottom:10px;">4 Đỉnh cao (Pinnacles)</h4>
            <table class="sys-table" style="max-width:380px;margin-bottom:16px;">
              <thead><tr><th>Đỉnh</th><th>Giai đoạn</th><th>Số</th><th>Chủ đề</th></tr></thead>
              <tbody>
                <tr><td>1</td><td>0–26 tuổi</td><td><strong>3</strong></td><td>Sáng tạo, biểu đạt</td></tr>
                <tr style="background:var(--gold-bg);"><td style="color:var(--gold);font-weight:600;">2 ★</td><td style="color:var(--gold);">27–35 tuổi</td><td style="font-weight:700;color:var(--gold);">1</td><td style="color:var(--gold);">★ Hiện tại: khởi đầu độc lập</td></tr>
                <tr><td>3</td><td>36–44 tuổi</td><td><strong>4</strong></td><td>Xây dựng nền tảng</td></tr>
                <tr><td>4</td><td>45+ tuổi</td><td><strong>7</strong></td><td>Chiều sâu &amp; trí tuệ</td></tr>
              </tbody>
            </table>

            <!-- Challenges -->
            <h4 style="margin-bottom:10px;">Thử thách</h4>
            <table class="sys-table" style="max-width:380px;margin-bottom:16px;">
              <thead><tr><th>Thử thách</th><th>Số</th><th>Bài học</th></tr></thead>
              <tbody>
                <tr><td>1 (0–35)</td><td><strong>4</strong></td><td>Kỷ luật, nhẫn nại</td></tr>
                <tr><td>2 (0–35)</td><td><strong>2</strong></td><td>Nhạy cảm quá mức</td></tr>
                <tr><td>3 (36+)</td><td><strong>6</strong></td><td>Trách nhiệm</td></tr>
                <tr style="background:var(--ember-bg);"><td>Chính</td><td style="color:var(--ember);font-weight:600;">2</td><td style="color:var(--ember);">Tin tưởng người khác</td></tr>
              </tbody>
            </table>

            <!-- Personal year/month -->
            <h4 style="margin-bottom:10px;">Chu kỳ cá nhân 2026</h4>
            <div style="display:flex;flex-direction:column;gap:6px;max-width:380px;">
              <div style="display:flex;justify-content:space-between;padding:8px 12px;background:var(--gold-bg);border-radius:var(--radius-sm);">
                <span style="font-size:13px;">Năm cá nhân 2026</span><span style="font-weight:700;color:var(--gold);">9 — Hoàn thành</span>
              </div>
              <div style="display:flex;justify-content:space-between;padding:8px 12px;background:var(--sand);border-radius:var(--radius-sm);">
                <span style="font-size:13px;">Tháng 3/2026</span><span style="font-weight:600;">3 — Sáng tạo</span>
              </div>
              <div style="display:flex;justify-content:space-between;padding:8px 12px;background:var(--sand);border-radius:var(--radius-sm);">
                <span style="font-size:13px;">Tháng 4/2026</span><span style="font-weight:600;">4 — Tập trung</span>
              </div>
            </div>
          </div>
          <div style="flex:1;padding:32px 48px 32px 32px;">
            <h3 style="margin-bottom:16px;">Life Path 7 — Nhà tư tưởng sâu sắc</h3>
            <div class="reading-text">
              <p style="margin-bottom:16px;">Số 7 là số của sự tìm kiếm ý nghĩa, của nghiên cứu và chiều sâu. Bạn không hài lòng với câu trả lời bề mặt — bạn cần hiểu cơ chế vận hành, nguyên nhân gốc rễ, và tầng nghĩa ẩn bên dưới. Đây là điểm mạnh lớn nhưng cũng là nguồn gốc của sự cô đơn khi không tìm được người hiểu cùng tầng sâu.</p>
              <p style="margin-bottom:16px;">Sự kết hợp <strong>7-3</strong> (Life Path-Expression) tạo ra người vừa có chiều sâu nội tâm (7) vừa có khả năng truyền đạt xuất sắc (3). Đây là tổ hợp hiếm gặp của giáo viên, nhà văn, diễn giả, podcaster — người có thể lấy những thứ phức tạp và biến chúng thành dễ hiểu mà không mất đi chiều sâu.</p>
              <p style="margin-bottom:16px;"><strong>Soul Urge 9</strong> cho thấy ở cấp độ linh hồn, bạn muốn cống hiến và để lại di sản — không chỉ thành công cá nhân. Khi công việc chỉ phục vụ lợi ích cá nhân mà không kết nối với điều lớn hơn, bạn sẽ cảm thấy rỗng tuếch dù đang thành công theo mắt người ngoài.</p>
              <p style="margin-bottom:16px;">Đỉnh cao số 1 hiện tại (27-35 tuổi) là giai đoạn khởi đầu độc lập — đây là thời điểm lý tưởng để bắt đầu xây dựng dự án hoặc sự nghiệp mang dấu ấn cá nhân rõ ràng, không phụ thuộc vào thương hiệu của người khác.</p>
              <div class="source">nguồn: Pythagorean Numerology · Số cốt lõi · Đỉnh cao</div>
            </div>
            <div style="margin-top:24px;padding-top:24px;border-top:1px solid var(--border);">
              <h4 style="margin-bottom:12px;">Hỏi về Số học</h4>
              <div style="display:flex;gap:8px;">
                <input type="text" id="s5-num-input" placeholder="VD: Năm cá nhân 2026 ảnh hưởng thế nào?" style="flex:1;" onkeydown="if(event.key==='Enter')sendQA('s5-num')">
                <button class="btn btn-gold btn-sm" onclick="sendQA('s5-num')">Gửi</button>
              </div>
              <div id="s5-num-result" style="display:none;"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- VEDIC TAB -->
      <div class="tab-panel" id="panel-vedic">
        <div style="display:flex;gap:0;" class="two-col">
          <div style="flex:1;padding:32px 32px 32px 48px;border-right:1px solid var(--border);">
            <h3 style="margin-bottom:16px;">Natal Chart — Vedic Astrology (Jyotish)</h3>
            <div class="card" style="padding:14px;border-left:4px solid var(--gold);margin-bottom:12px;max-width:380px;">
              <p style="font-size:12px;color:var(--stone);margin-bottom:4px;">Ascendant (Lagna)</p>
              <p style="font-size:18px;font-weight:600;font-family:var(--font-heading);">Scorpio — Vrishchika</p>
              <p class="muted" style="font-size:13px;margin-top:4px;">Anuradha Nakshatra · Perseverance</p>
            </div>

            <!-- Planet table -->
            <h4 style="margin-bottom:10px;">Vị trí hành tinh</h4>
            <div style="overflow-x:auto;max-width:420px;margin-bottom:16px;">
              <table class="sys-table" style="min-width:380px;">
                <thead><tr><th>Hành tinh</th><th>Rashi</th><th>Nhà</th><th>Nakshatra</th><th>Vị thế</th></tr></thead>
                <tbody>
                  <tr><td>☀️ Mặt Trời</td><td>Gemini (Song Tử)</td><td>8th</td><td>Ardra</td><td style="color:var(--ember);">Debilitated</td></tr>
                  <tr><td>🌙 Mặt Trăng</td><td>Capricorn (Ma Kết)</td><td>3rd</td><td>Shravana</td><td>Neutral</td></tr>
                  <tr><td>♂ Mars</td><td>Scorpio (Thiên Yết)</td><td>1st</td><td>Anuradha</td><td style="color:var(--sage);">Own sign</td></tr>
                  <tr><td>☿ Mercury</td><td>Gemini (Song Tử)</td><td>8th</td><td>Mrigashira</td><td style="color:var(--sage);">Exalted</td></tr>
                  <tr><td>♃ Jupiter</td><td>Capricorn (Ma Kết)</td><td>3rd</td><td>Sravana</td><td style="color:var(--ember);">Debilitated</td></tr>
                  <tr><td>♀ Venus</td><td>Cancer (Cự Giải)</td><td>9th</td><td>Pushya</td><td>Neutral</td></tr>
                  <tr><td>♄ Saturn</td><td>Aries (Bạch Dương)</td><td>6th</td><td>Bharani</td><td style="color:var(--ember);">Debilitated</td></tr>
                  <tr><td>☊ Rahu</td><td>Virgo (Xử Nữ)</td><td>11th</td><td>Hasta</td><td>—</td></tr>
                  <tr><td>☋ Ketu</td><td>Pisces (Song Ngư)</td><td>5th</td><td>Uttara Bhadrapada</td><td>—</td></tr>
                </tbody>
              </table>
            </div>

            <!-- Dasha timeline -->
            <h4 style="margin-bottom:10px;">Dasha hiện tại</h4>
            <div style="display:flex;flex-direction:column;gap:6px;max-width:380px;margin-bottom:16px;">
              <div style="padding:10px 12px;background:var(--gold-bg);border-radius:var(--radius-sm);border-left:3px solid var(--gold);">
                <strong style="font-size:13px;color:var(--gold);">Saturn Mahadasha (2021–2040)</strong>
                <p class="muted" style="font-size:12px;margin-top:2px;">Giai đoạn xây dựng kỷ luật và trách nhiệm</p>
              </div>
              <div style="padding:10px 12px;background:var(--sand);border-radius:var(--radius-sm);">
                <strong style="font-size:13px;">Saturn-Mercury Antardasha (2024–2027)</strong>
                <p class="muted" style="font-size:12px;margin-top:2px;">★ Hiện tại — Tư duy sắc bén, học tập &amp; viết lách</p>
              </div>
              <div style="padding:10px 12px;background:var(--sand);border-radius:var(--radius-sm);">
                <strong style="font-size:13px;">Saturn-Ketu Antardasha (2027–2028)</strong>
                <p class="muted" style="font-size:12px;margin-top:2px;">Chuyển hóa nội tâm, cắt bỏ</p>
              </div>
            </div>

            <!-- Key Yogas -->
            <h4 style="margin-bottom:10px;">Yoga quan trọng</h4>
            <div style="display:flex;flex-direction:column;gap:6px;max-width:380px;">
              <div style="padding:8px 12px;background:var(--sage-bg);border-radius:var(--radius-sm);font-size:12px;"><strong style="color:var(--sage);">Viparita Raja Yoga</strong><br>Saturn in 6th — Thành công từ khó khăn và thử thách</div>
              <div style="padding:8px 12px;background:var(--sage-bg);border-radius:var(--radius-sm);font-size:12px;"><strong style="color:var(--sage);">Budha-Aditya Yoga</strong><br>Sun-Mercury together — Trí tuệ sắc bén, danh tiếng qua tri thức</div>
              <div style="padding:8px 12px;background:var(--sand);border-radius:var(--radius-sm);font-size:12px;"><strong>Shravana Moon</strong><br>Lắng nghe, học hỏi từ mọi nguồn — tài năng nghe sâu</div>
            </div>
          </div>
          <div style="flex:1;padding:32px 48px 32px 32px;">
            <h3 style="margin-bottom:16px;">Scorpio Ascendant — Nhà biến đổi</h3>
            <div class="reading-text">
              <p style="margin-bottom:16px;">Ascendant Scorpio mang đến một con người bí ẩn, sâu sắc, và có sức ảnh hưởng lớn trong im lặng. Bạn không cần nói nhiều để người khác cảm nhận được sự hiện diện. Mars làm chủ Lagna và ở trong Scorpio (own sign) — tạo nên sức mạnh và khả năng phục hồi phi thường. Bạn không dễ bị hạ gục — và khi bị hạ, bạn có khả năng tái sinh như phượng hoàng.</p>
              <p style="margin-bottom:16px;"><strong>Saturn Dasha</strong> kéo dài đến 2040 — đây là giai đoạn Karma được giải quyết qua kỷ luật và trách nhiệm. Saturn trong nhà 6 (Viparita Raja Yoga) thực ra là dấu hiệu tích cực: thành công đến qua việc vượt qua khó khăn, không phải né tránh chúng. Mỗi thử thách trong giai đoạn này là một bài kiểm tra Saturn.</p>
              <p style="margin-bottom:16px;"><strong>Mercury Antardasha hiện tại (đến 2027)</strong> là thời điểm vàng cho việc học tập, nghiên cứu, viết lách, và xây dựng hệ thống tư duy. Budha-Aditya Yoga (Sun-Mercury đồng cung) khuếch đại khả năng trí tuệ và danh tiếng qua tri thức. Đây là lúc tốt nhất để tạo ra intellectual property.</p>
              <p style="margin-bottom:16px;"><strong>Moon Nakshatra Shravana</strong> — "người lắng nghe". Bạn học bằng cách lắng nghe và quan sát thay vì chỉ đọc. Podcast, cuộc trò chuyện sâu, mentorship là những phương thức học tập hiệu quả nhất với bạn.</p>
              <div class="source">nguồn: Vedic Astrology (Jyotish) — Natal Chart · Dasha · Yoga</div>
            </div>
            <div style="margin-top:24px;padding-top:24px;border-top:1px solid var(--border);">
              <h4 style="margin-bottom:12px;">Hỏi về Vedic</h4>
              <div style="display:flex;gap:8px;">
                <input type="text" id="s5-vedic-input" placeholder="VD: Saturn Dasha ảnh hưởng tới tôi thế nào?" style="flex:1;" onkeydown="if(event.key==='Enter')sendQA('s5-vedic')">
                <button class="btn btn-gold btn-sm" onclick="sendQA('s5-vedic')">Gửi</button>
              </div>
              <div id="s5-vedic-result" style="display:none;"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
'''

with open(path, 'a', encoding='utf-8') as f:
    f.write(p3)
print('part3 done', len(p3))
