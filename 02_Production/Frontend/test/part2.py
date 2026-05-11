
path = 'C:/Users/Admin/Desktop/Visionaries_Startup_April/02_Production/Frontend/test/index.html'

p2 = '''
<!-- S4 DASHBOARD -->
<div id="s4" class="screen">
  <div class="app-layout">
    <nav class="sidebar">
      <div class="sidebar-logo">360Human</div>
      <ul class="sidebar-nav">
        <li class="active" onclick="showScreen('s4')">&#9689; Tổng Quan</li>
        <li onclick="showScreen('s5')">&#11041; Biểu đồ hệ thống</li>
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
          <span style="font-weight:500;">Thảo Nguyễn</span>
          <span class="badge badge-free" id="s4-tier-badge">FREE</span>
        </div>
        <div class="topbar-right">
          <button class="btn btn-ghost btn-sm" id="s4-pdf-btn" style="opacity:0.4;cursor:not-allowed;" disabled onclick="alert('Xuất PDF chỉ khả dụng với gói PRO')">Xuất PDF &#128274;</button>
          <button class="btn btn-ghost btn-sm" onclick="showScreen('s8')">&#9881;</button>
        </div>
      </div>
      <div id="s4-pro-banner" class="pro-banner" style="display:none;padding:12px 48px;background:var(--success-bg);border-bottom:1px solid #9dd6b0;">
        <p style="font-size:14px;color:var(--success);text-align:center;">&#10003; <strong>360Human PRO</strong> đã được kích hoạt — Tất cả 10 chủ đề và biểu đồ đã mở khóa</p>
      </div>
      <div style="padding:12px 48px;background:var(--sand);display:flex;align-items:center;gap:16px;">
        <div class="progress-bar" style="flex:1;"><div class="fill" id="s4-progress-fill" style="width:20%"></div></div>
        <span style="font-size:13px;color:var(--stone);" id="s4-progress-label">2/10 chủ đề — <a href="#" style="color:var(--gold);" onclick="showScreen('s7')">Mở khóa thêm 8 với PRO</a></span>
      </div>
      <div style="display:flex;gap:0;" class="two-col">
        <!-- LEFT: Readings -->
        <div style="flex:2;padding:32px 32px 80px 48px;border-right:1px solid var(--border);">
          <h2 style="margin-bottom:6px;">Luận giải theo chủ đề</h2>
          <p class="muted" style="font-size:14px;margin-bottom:24px;">What · Why · How · What's next</p>

          <!-- Topic 1 - Free - ~500 words -->
          <div class="accordion-item open">
            <div class="accordion-header" onclick="toggleAccordion(this)">
              <span>1. Tổng quan bản thân</span><span class="arrow">&#9662;</span>
            </div>
            <div class="accordion-body">
              <div class="reading-text" style="margin-bottom:24px;">
                <h4 style="color:var(--gold);margin-bottom:12px;font-family:var(--font-heading);">Năng lượng cốt lõi</h4>
                <p style="margin-bottom:16px;">Bạn là người mang năng lượng của sự chuyển hóa có chủ đích. Bên ngoài, bạn giữ vẻ điềm tĩnh và kiên định — nhưng bên trong, bạn luôn đang xử lý, phân tích, và tìm cách làm mọi thứ tinh tế hơn, sâu sắc hơn. Đây không phải đặc điểm học được — đây là cấu trúc căn bản của bạn, được xác nhận đồng thời bởi cả năm hệ thống chiêm tinh.</p>
                <p style="margin-bottom:16px;">Sự kết hợp giữa <strong>Canh Kim Nhật Chủ</strong> trong BaZi và <strong>Tham Lang miếu địa tại Cung Mệnh Tuất</strong> trong Tử Vi tạo nên một tổ hợp đặc biệt: nền tảng kim loại cứng rắn, bất khuất, nhưng được bọc bên ngoài bởi sức hút tự nhiên và đa tài của Tham Lang. Bạn là kiếm sắc được giấu trong vỏ lụa — người ta cảm nhận sự hiện diện trước khi hiểu được độ sắc bén bên trong.</p>
                <h4 style="color:var(--gold);margin-bottom:12px;margin-top:20px;font-family:var(--font-heading);">Cơ chế vận hành nội tâm</h4>
                <p style="margin-bottom:16px;">Trong Human Design, bạn là <strong>Manifesting Generator với Emotional Authority</strong> — Profile 4/6 (Người Cơ Hội / Hình Mẫu). Điều này có nghĩa bạn không được thiết kế để đưa ra quyết định tức thì. Bạn cần thời gian cảm xúc — đợi qua một chu kỳ cảm xúc trước khi cam kết với điều gì lớn lao. Những ai biết điều này sẽ hiểu tại sao đôi khi bạn nói "để tôi suy nghĩ thêm" — đó không phải do dự, đó là trí tuệ.</p>
                <p style="margin-bottom:16px;">Defined Head, Ajna và Throat Center tạo nên một người có tư duy rõ ràng, độc lập, và khả năng truyền đạt ý tưởng xuất sắc. Solar Plexus defined — nguồn cảm xúc phong phú và sâu sắc là la bàn quyết định của bạn. Bạn biết khi nào điều gì đó "đúng" vì cơ thể nói với bạn bằng ngôn ngữ cảm xúc.</p>
                <h4 style="color:var(--gold);margin-bottom:12px;margin-top:20px;font-family:var(--font-heading);">Thiết kế để làm gì</h4>
                <p style="margin-bottom:16px;">Life Path 7 trong Số học là con số của người tìm kiếm — không phải tìm kiếm thú vui, mà tìm kiếm ý nghĩa, chân lý, và sự hiểu biết sâu sắc về cách mọi thứ vận hành. Kết hợp với Expression 3 (người truyền đạt), bạn được thiết kế để hiểu sâu và chia sẻ điều đó một cách đẹp đẽ, dễ tiếp cận. Đây là tổ hợp hiếm gặp của nhà nghiên cứu-giáo viên.</p>
                <p style="margin-bottom:16px;">Trong Vedic, Scorpio Ascendant và Saturn Dasha hiện tại (2021–2040) xác nhận: đây là giai đoạn xây dựng thật sự, không phải thời gian thử nghiệm. Mọi nỗ lực kiên nhẫn trong giai đoạn này đều được Saturn ghi nhận và thưởng xứng đáng — nhưng theo con đường chậm và chắc, không phải nhanh và rủi ro.</p>
                <p style="margin-bottom:16px;">Khi tất cả hợp lại: bạn là người được thiết kế để đi sâu vào hệ thống, hiểu cơ chế, và dẫn dắt người khác qua sự hiểu biết đó. Không phải bằng quyền lực, mà bằng sự tín nhiệm được xây dựng qua thời gian và kết quả thực.</p>
                <div class="source">nguồn: BaZi · Tử Vi · Human Design · Số học · Vedic</div>
              </div>
              <div style="border-top:1px solid var(--border);padding-top:16px;">
                <h4 style="margin-bottom:12px;color:var(--stone);">Hành động đề xuất</h4>
                <div style="display:flex;flex-direction:column;gap:8px;">
                  <div style="display:flex;justify-content:space-between;align-items:start;padding:10px 12px;background:var(--sand);border-radius:var(--radius-sm);">
                    <div><strong style="font-size:14px;">1. Dành 10 phút mỗi sáng viết nhật ký</strong><br><span class="muted" style="font-size:13px;">Quan sát mâu thuẫn nội tại — viết ra, không phán xét</span></div>
                    <span class="badge-system">BaZi</span>
                  </div>
                  <div style="display:flex;justify-content:space-between;align-items:start;padding:10px 12px;background:var(--sand);border-radius:var(--radius-sm);">
                    <div><strong style="font-size:14px;">2. Nói "không" ít nhất 1 lần/tuần</strong><br><span class="muted" style="font-size:13px;">Tham Lang miếu địa dễ thu hút — nhưng cần chọn lọc</span></div>
                    <span class="badge-system">Tử Vi</span>
                  </div>
                </div>
                <a href="#" style="font-size:13px;color:var(--gold);display:block;margin-top:12px;" onclick="showScreen('s10')">Xem toàn bộ hành động →</a>
              </div>
            </div>
          </div>

          <!-- Topic 2 - Free - ~500 words -->
          <div class="accordion-item">
            <div class="accordion-header" onclick="toggleAccordion(this)">
              <span>2. Sứ mệnh &amp; mục đích sống</span><span class="arrow">&#9662;</span>
            </div>
            <div class="accordion-body">
              <div class="reading-text">
                <p style="margin-bottom:16px;">Sứ mệnh của bạn không nằm ở một nghề nghiệp cụ thể — nó nằm ở <strong>cách bạn tồn tại trong thế giới</strong>. Bạn được gọi để trở thành người hiểu sâu, kết nối những thứ tưởng chừng không liên quan, và biến sự hiểu biết đó thành ánh sáng cho người khác. Đây là kết luận nhất quán khi nhìn qua cả năm hệ thống.</p>
                <p style="margin-bottom:16px;"><strong>Human Design xác nhận:</strong> Profile 4/6 là một trong những profile được gọi là "hành trình hai nửa cuộc đời". Nửa đầu (đến khoảng 35-40 tuổi) là thời gian thử nghiệm, học hỏi, xây dựng nền tảng mạng lưới. Nửa sau, bạn trở thành hình mẫu — người dẫn đường bằng cách đã sống qua và hiểu thật sự. Manifesting Generator như bạn không theo một con đường thẳng; bạn xây dựng sứ mệnh qua nhiều làn sóng trải nghiệm song song, và đó là điểm mạnh chứ không phải điểm yếu.</p>
                <p style="margin-bottom:16px;"><strong>Số học làm rõ nội dung sứ mệnh:</strong> Life Path 7 + Expression 3 = người tìm kiếm chân lý và có năng lực truyền đạt nó. Soul Urge 9 tiết lộ động lực sâu xa nhất: bạn không thỏa mãn với thành công cá nhân thuần túy — bạn cần cảm giác đóng góp cho điều gì lớn hơn bản thân. Đây là điều giải thích tại sao những công việc "tốt về vật chất nhưng vô nghĩa" sẽ luôn khiến bạn cảm thấy thiếu thiếu.</p>
                <p style="margin-bottom:16px;"><strong>Tử Vi chỉ ra lĩnh vực:</strong> Tham Lang miếu địa tại Cung Mệnh Tuất với Hóa Quyền tại Ngọ (Quan Lộc) — bạn có thiên hướng và sức mạnh tự nhiên trong vai trò lãnh đạo tư tưởng, tư vấn chuyên sâu, hoặc nghiên cứu-giảng dạy. Cung Quan Lộc có Tử Vi sao với Hóa Quyền là dấu hiệu của người tạo ra hệ thống và ảnh hưởng qua quyền lực tri thức.</p>
                <p style="margin-bottom:16px;"><strong>Vedic chỉ ra thời điểm:</strong> Nhà thứ 9 (dharma, triết học, giảng dạy) được Jupiter và Venus chiếu sáng. Saturn Dasha hiện tại là thời gian gieo hạt kiên nhẫn cho sứ mệnh — kết quả rõ ràng sẽ đến sau 2033, nhưng nền móng bạn xây hôm nay quyết định quy mô của những gì sẽ đến.</p>
                <p style="margin-bottom:16px;"><strong>Sống sứ mệnh thực tế:</strong> Đừng chờ "hoàn hảo" để bắt đầu. Mỗi lần bạn chia sẻ một insight thật sự sâu sắc với người khác — dù trong cuộc trò chuyện hàng ngày, bài viết, hay một buổi tư vấn — đó là lúc sứ mệnh đang được sống. Sứ mệnh không bắt đầu bằng một khoảnh khắc kịch tính. Nó bắt đầu bằng những hành động nhỏ, nhất quán, hàng ngày.</p>
                <div class="source">nguồn: Human Design (Profile 4/6) · Số học (Life Path 7 + Soul Urge 9) · Tử Vi (Cung Quan Lộc) · Vedic (9th house)</div>
              </div>
            </div>
          </div>

          <!-- Topics 3-10: locked for FREE -->
          <div class="accordion-item locked" id="topic-3" onclick="handleLockedTopic(this,3)">
            <div class="accordion-header"><span>3. Tình cảm &amp; các mối quan hệ <span id="lock-3" class="badge badge-pro" style="font-size:10px;margin-left:8px;">PRO</span></span><span class="arrow" id="arrow-3">&#9662;</span></div>
            <div class="accordion-body" id="body-3">
              <div class="reading-text" style="margin-bottom:24px;">
                <p style="margin-bottom:16px;">Trong tình cảm, bạn là người cần thời gian để mở lòng — nhưng khi đã mở, bạn đầu tư hoàn toàn và sâu sắc. Profile 4/6 tạo nên một nghịch lý đẹp: bạn cần kết nối sâu sắc nhưng đồng thời cần không gian cá nhân để tái tạo năng lượng. Emotional Authority có nghĩa là bạn không nên đưa ra quyết định tình cảm lớn trong trạng thái xúc động cao — hãy chờ cảm xúc lắng xuống và nghe tiếng nói của sự rõ ràng.</p>
                <p style="margin-bottom:16px;">Kim gặp Thủy trong tứ trụ là tổ hợp lý tưởng cho tình cảm — bạn tương thích nhất với những người có tư duy rõ ràng nhưng cảm xúc phong phú, người cho bạn không gian nhưng không cảm thấy bị bỏ rơi. Cung Phu Thê có Thiên Cơ và Thiên Khôi — đối tác lý tưởng là người thông minh, có đạo đức, và tôn trọng sự độc lập của bạn.</p>
                <p style="margin-bottom:16px;">Soul Urge 9 trong Số học nói rằng ở cấp độ sâu nhất, bạn tìm kiếm một mối quan hệ có ý nghĩa và đóng góp — không chỉ là sự thoải mái. Bạn muốn một đối tác cùng nhau xây dựng điều gì đó lớn hơn cả hai người.</p>
                <div class="source">nguồn: Human Design (Profile 4/6, Emotional Authority) · BaZi (Dụng Thần Thủy) · Tử Vi (Cung Phu Thê) · Số học (Soul Urge 9)</div>
              </div>
            </div>
          </div>

          <div class="accordion-item locked" id="topic-4" onclick="handleLockedTopic(this,4)">
            <div class="accordion-header"><span>4. Sự nghiệp &amp; nghề nghiệp <span id="lock-4" class="badge badge-pro" style="font-size:10px;margin-left:8px;">PRO</span></span><span class="arrow" id="arrow-4">&#9662;</span></div>
            <div class="accordion-body" id="body-4">
              <div class="reading-text" style="margin-bottom:24px;">
                <p style="margin-bottom:16px;">Bạn không sinh ra để làm theo mệnh lệnh — bạn sinh ra để tạo ra hệ thống và dẫn dắt bằng tư duy. Cung Quan Lộc trong Tử Vi có Tử Vi sao với Hóa Quyền — đây là dấu hiệu của người lãnh đạo bằng trí tuệ và uy tín, không phải bằng chức vị. Canh Kim Nhật Chủ làm việc tốt nhất khi có tự chủ cao và mục tiêu rõ ràng.</p>
                <p style="margin-bottom:16px;">Manifesting Generator phù hợp nhất với môi trường đa nhiệm có nhịp độ cao, nơi bạn có thể chuyển đổi giữa nhiều dự án song song. Khác với Generator thuần túy, bạn không chỉ phản ứng với cơ hội — bạn còn có khả năng khởi tạo. Tuy nhiên, chiến lược tốt nhất vẫn là phản ứng với điều gì đó đang xảy ra trong thực tế, không phải cố gắng tạo ra thứ gì từ chân không.</p>
                <p style="margin-bottom:16px;">Các lĩnh vực phù hợp với tổ hợp biểu đồ của bạn: tư vấn chiến lược, nghiên cứu, giảng dạy, thiết kế sản phẩm và hệ thống, content sâu sắc về tâm lý hoặc triết học ứng dụng. Saturn Dasha trong Vedic xác nhận: lĩnh vực bạn đầu tư kiên nhẫn nhất bây giờ sẽ là nền tảng thành công lớn sau 2033.</p>
                <div class="source">nguồn: Tử Vi (Cung Quan Lộc) · BaZi (Canh Kim) · Human Design (MG) · Vedic (Saturn Dasha)</div>
              </div>
            </div>
          </div>

          <div class="accordion-item locked" id="topic-5" onclick="handleLockedTopic(this,5)">
            <div class="accordion-header"><span>5. Tài chính &amp; tiền bạc <span id="lock-5" class="badge badge-pro" style="font-size:10px;margin-left:8px;">PRO</span></span><span class="arrow" id="arrow-5">&#9662;</span></div>
            <div class="accordion-body" id="body-5">
              <div class="reading-text" style="margin-bottom:24px;">
                <p style="margin-bottom:16px;">Với Expression Number 3 và Tham Lang miếu địa, bạn có khả năng tạo ra giá trị từ ý tưởng và sức hút cá nhân — nhưng dễ bị phân tán vào quá nhiều hướng cùng lúc. Tài chính của bạn phản ánh trực tiếp mức độ tập trung: khi bạn chọn 1-2 lĩnh vực chính và kiên định, tiền bắt đầu chảy vào. Khi bạn trải mỏng, mọi thứ đều không phát huy hết tiềm năng.</p>
                <p style="margin-bottom:16px;">Cung Tài Bạch trong Tử Vi có Phá Quân và Liêm Trinh — đây là tổ hợp của sự đột phá tài chính qua những thay đổi lớn và dứt khoát. Bạn không tích lũy tiền theo kiểu nhỏ giọt — bạn thường có những bước nhảy vọt lớn khi đưa ra quyết định táo bạo đúng thời điểm.</p>
                <p style="margin-bottom:16px;">Giai đoạn Đại Vận Đinh Dậu (2024-2033) theo BaZi là thời gian tích lũy và củng cố tài chính qua kỷ luật. Đầu tư vào kiến thức và kỹ năng bây giờ sẽ tạo ra đòn bẩy tài chính lớn trong giai đoạn sau.</p>
                <div class="source">nguồn: Số học (Expression 3) · Tử Vi (Cung Tài Bạch) · BaZi (Đại Vận) · Vedic (2nd house)</div>
              </div>
            </div>
          </div>

          <div class="accordion-item locked" id="topic-6" onclick="handleLockedTopic(this,6)">
            <div class="accordion-header"><span>6. Sức khỏe &amp; năng lượng <span id="lock-6" class="badge badge-pro" style="font-size:10px;margin-left:8px;">PRO</span></span><span class="arrow" id="arrow-6">&#9662;</span></div>
            <div class="accordion-body" id="body-6">
              <div class="reading-text" style="margin-bottom:24px;">
                <p style="margin-bottom:16px;">Trong Human Design, Sacral Center không xác định trong biểu đồ của bạn mang một ý nghĩa quan trọng: bạn hấp thu và khuếch đại năng lượng từ môi trường xung quanh. Khi ở cạnh người energetic, bạn cảm thấy có thể làm mọi thứ — nhưng đó không phải năng lượng bền vững của bản thân. Sau khi tách ra khỏi đám đông, bạn cần thời gian phục hồi dài hơn người thường.</p>
                <p style="margin-bottom:16px;">Canh Kim gặp Hỏa đôi Ngọ trong BaZi tạo ra xu hướng "đốt cháy" năng lượng ở cường độ cao trong thời gian ngắn. Cơ thể bạn hoạt động theo chu kỳ — bùng nổ rồi cần nghỉ sâu. Đừng chống lại chu kỳ tự nhiên này bằng caffeine và ý chí.</p>
                <p style="margin-bottom:16px;">Cung Tật Ách có Thiên Lương và Thiên Giải — dấu hiệu tích cực về sức khỏe tổng thể, đặc biệt là khả năng tự hồi phục khi có không gian và thời gian nghỉ ngơi thích hợp. Ưu tiên giấc ngủ chất lượng và thời gian tĩnh lặng mỗi ngày là đầu tư y tế quan trọng nhất của bạn.</p>
                <div class="source">nguồn: Human Design (Sacral undefined) · BaZi (Kim-Hỏa) · Tử Vi (Cung Tật Ách) · Vedic (6th house)</div>
              </div>
            </div>
          </div>

          <div class="accordion-item locked" id="topic-7" onclick="handleLockedTopic(this,7)">
            <div class="accordion-header"><span>7. Gia đình &amp; nguồn gốc <span id="lock-7" class="badge badge-pro" style="font-size:10px;margin-left:8px;">PRO</span></span><span class="arrow" id="arrow-7">&#9662;</span></div>
            <div class="accordion-body" id="body-7">
              <div class="reading-text" style="margin-bottom:24px;">
                <p style="margin-bottom:16px;">Cung Phụ Mẫu trong Tử Vi có Thiên Phủ — đây là dấu hiệu của người có nền tảng gia đình ổn định và hỗ trợ, dù đôi khi có những kỳ vọng vô hình mà bạn cảm thấy cần đáp ứng. Thiên Phủ là ngôi sao của sự bảo hộ và kho tàng — gia đình bạn có thể là nguồn lực quan trọng hơn bạn nhận ra.</p>
                <p style="margin-bottom:16px;">Profile 4 trong Human Design là "Opportunist" — một trong những nguồn cơ hội lớn nhất của bạn đến từ mạng lưới quan hệ cá nhân gần gũi, bao gồm gia đình. Đây không phải sự phụ thuộc — đây là chiến lược tự nhiên của biểu đồ bạn. Đầu tư vào các mối quan hệ thân thiết là đầu tư vào sứ mệnh của bạn.</p>
                <p style="margin-bottom:16px;">Hành Canh Kim trong BaZi — bạn mang tính cứng rắn và nguyên tắc vào quan hệ gia đình. Học cách mềm mại hơn trong môi trường gia đình — không phải yếu đuối hơn, mà là dùng đúng loại kim loại: không phải búa rìu trong nhà, mà là kim thêu tinh tế.</p>
                <div class="source">nguồn: Tử Vi (Cung Phụ Mẫu) · Human Design (Profile 4) · BaZi (Canh Kim)</div>
              </div>
            </div>
          </div>

          <div class="accordion-item locked" id="topic-8" onclick="handleLockedTopic(this,8)">
            <div class="accordion-header"><span>8. Điểm mạnh &amp; tài năng <span id="lock-8" class="badge badge-pro" style="font-size:10px;margin-left:8px;">PRO</span></span><span class="arrow" id="arrow-8">&#9662;</span></div>
            <div class="accordion-body" id="body-8">
              <div class="reading-text" style="margin-bottom:24px;">
                <p style="margin-bottom:16px;">Điểm mạnh cốt lõi của bạn là tư duy hệ thống bậc cao — khả năng nhìn thấy pattern mà người khác bỏ qua, kết nối các điểm tưởng chừng rời rạc thành một bức tranh mạch lạc. Defined Ajna Center trong Human Design cho thấy bạn có cách nhìn thế giới rất riêng, nhất quán, và không dễ bị lung lay bởi ý kiến số đông — đây là tài sản quý giá trong thế giới đầy nhiễu.</p>
                <p style="margin-bottom:16px;">Tham Lang miếu địa tại Cung Mệnh trao cho bạn sức hút tự nhiên và đa tài — bạn học nhanh, thích nghi tốt, và thường tạo ấn tượng tích cực ngay lần đầu gặp. Đây là tài năng xã hội không phải ai cũng có, đặc biệt mạnh khi kết hợp với chiều sâu tư duy của Life Path 7.</p>
                <p style="margin-bottom:16px;">Channel 43-23 (Structuring) trong Human Design — bạn có khả năng biến những insight cá nhân độc đáo thành ngôn ngữ mà người khác hiểu được. Đây là nền tảng tự nhiên của người sáng tạo nội dung, giảng dạy, hoặc tư vấn chiến lược chuyên sâu.</p>
                <div class="source">nguồn: Human Design (Defined Ajna, Channel 43-23) · Tử Vi (Tham Lang miếu địa) · Số học (Life Path 7)</div>
              </div>
            </div>
          </div>

          <div class="accordion-item locked" id="topic-9" onclick="handleLockedTopic(this,9)">
            <div class="accordion-header"><span>9. Thách thức &amp; bóng tối <span id="lock-9" class="badge badge-pro" style="font-size:10px;margin-left:8px;">PRO</span></span><span class="arrow" id="arrow-9">&#9662;</span></div>
            <div class="accordion-body" id="body-9">
              <div class="reading-text" style="margin-bottom:24px;">
                <p style="margin-bottom:16px;">Thách thức lớn nhất của bạn là chủ nghĩa hoàn hảo ẩn núp dưới danh nghĩa "cần chuẩn bị thêm". Canh Kim Nhật Chủ có xu hướng đặt tiêu chuẩn rất cao — cho bản thân và người khác. Khi tiêu chuẩn đó không đạt được, phản ứng tự nhiên là trì hoãn hoặc thu mình lại. Nhận ra pattern này là bước đầu tiên để vượt qua nó.</p>
                <p style="margin-bottom:16px;">Hóa Kị tại Cung Tử Tức (Cự Môn) trong Tử Vi — cẩn thận với lời nói trong môi trường gần gũi, đặc biệt là giao tiếp với thế hệ trẻ hơn hoặc người bạn dẫn dắt. Lời nói thiếu cân nhắc có thể để lại dấu ấn lâu dài hơn bạn nghĩ.</p>
                <p style="margin-bottom:16px;">Will Center không xác định trong Human Design — bạn không có willpower nội tại ổn định. Khi ở một mình, bạn dễ mất đà. Khi ở cạnh người có Will Center defined mạnh, bạn cảm thấy có thể chinh phục thế giới — nhưng đó không phải năng lượng bền vững. Học cách tạo ra cấu trúc bên ngoài (lịch trình, accountability partner) thay vì phụ thuộc vào willpower.</p>
                <div class="source">nguồn: BaZi (Kiêu Thần) · Tử Vi (Hóa Kị-Cự Môn) · Human Design (Will Center undefined)</div>
              </div>
            </div>
          </div>

          <div class="accordion-item locked" id="topic-10" onclick="handleLockedTopic(this,10)">
            <div class="accordion-header"><span>10. Thời điểm &amp; chu kỳ <span id="lock-10" class="badge badge-pro" style="font-size:10px;margin-left:8px;">PRO</span></span><span class="arrow" id="arrow-10">&#9662;</span></div>
            <div class="accordion-body" id="body-10">
              <div class="reading-text" style="margin-bottom:24px;">
                <p style="margin-bottom:16px;">Bạn đang ở trong Đại Vận Đinh Dậu (2024-2033) — giai đoạn của sự củng cố, tích lũy, và xây dựng nền móng. Đinh Hỏa tác động lên Canh Kim theo kiểu tinh luyện — đây không phải lửa thiêu, đây là lò rèn. Mọi khó khăn và áp lực trong giai đoạn này đều có chức năng: biến quặng thô thành thanh kiếm sắc bén.</p>
                <p style="margin-bottom:16px;">2026 là năm Personal Year 9 trong Số học — năm kết thúc một chu kỳ 9 năm lớn (2018-2026). Những gì không còn phù hợp sẽ tự nhiên rời đi: mối quan hệ không còn phục vụ sự phát triển của bạn, công việc không còn align với sứ mệnh, patterns cũ cần được buông bỏ. Đừng cưỡng lại quá trình này — hãy tạo điều kiện cho sự kết thúc diễn ra với ân sủng.</p>
                <p style="margin-bottom:16px;">Saturn Dasha trong Vedic tiếp tục đến 2040 — xác nhận đây là giai đoạn dài hạn của sự kiên nhẫn và kỷ luật. Antardasha Mercury hiện tại (2024-2027) là thời điểm thuận lợi đặc biệt cho việc học tập, viết lách, giao tiếp, và xây dựng hệ thống tư duy. Đây là thời điểm vàng để đặt nền móng tri thức.</p>
                <div class="source">nguồn: BaZi (Đại Vận Đinh Dậu) · Số học (Personal Year 9) · Vedic (Saturn-Mercury Dasha)</div>
              </div>
            </div>
          </div>

          <!-- Q&A -->
          <div style="margin-top:32px;padding-top:24px;border-top:1px solid var(--border);" id="s4-qa-section">
            <h3 style="margin-bottom:6px;">Hỏi đáp</h3>
            <p class="muted" style="font-size:14px;margin-bottom:16px;">Đặt câu hỏi về luận giải của bạn</p>
            <div id="s4-qa-locked" style="display:block;">
              <div style="display:flex;gap:8px;">
                <input type="text" placeholder="Hỏi về luận giải của bạn..." style="flex:1;opacity:0.4;" disabled>
                <button class="btn btn-gold btn-sm" style="opacity:0.4;cursor:not-allowed;" disabled>Gửi</button>
              </div>
              <p class="muted" style="font-size:13px;margin-top:8px;"><a href="#" style="color:var(--gold);" onclick="showScreen('s7')">Nâng cấp PRO</a> để sử dụng tính năng hỏi đáp</p>
            </div>
            <div id="s4-qa-active" style="display:none;">
              <div style="display:flex;gap:8px;">
                <input type="text" id="s4-qa-input" placeholder="VD: Tại sao tôi hay trì hoãn? Làm sao tôi cải thiện được?" style="flex:1;" onkeydown="if(event.key==='Enter')sendQA('s4')">
                <button class="btn btn-gold btn-sm" onclick="sendQA('s4')">Gửi</button>
              </div>
              <div id="s4-qa-result" style="display:none;"></div>
              <div style="margin-top:12px;display:flex;gap:8px;flex-wrap:wrap;">
                <button class="btn btn-ghost btn-sm" style="font-size:12px;" onclick="fillQA('s4','Tại sao tôi hay trì hoãn?')">Tại sao tôi hay trì hoãn?</button>
                <button class="btn btn-ghost btn-sm" style="font-size:12px;" onclick="fillQA('s4','Mối quan hệ nào phù hợp với tôi?')">Mối quan hệ nào phù hợp?</button>
                <button class="btn btn-ghost btn-sm" style="font-size:12px;" onclick="fillQA('s4','Điểm mạnh lớn nhất của tôi là gì?')">Điểm mạnh lớn nhất?</button>
              </div>
            </div>
          </div>
        </div>

        <!-- RIGHT: Charts -->
        <div style="flex:1;padding:32px 48px 32px 32px;">
          <h3 style="margin-bottom:6px;">Biểu đồ hệ thống</h3>
          <p class="muted" style="font-size:13px;margin-bottom:24px;">WHY — dữ liệu đằng sau luận giải</p>
          <div style="display:flex;flex-direction:column;gap:8px;" id="s4-charts">
            <div class="card" style="padding:16px;cursor:pointer;" id="chart-tuvi" onclick="goToChart('tu-vi')">
              <div style="display:flex;align-items:center;gap:8px;"><span>&#11041;</span><span style="flex:1;">Tử Vi</span><span class="badge badge-pro chart-lock-badge" style="font-size:10px;">PRO</span><span class="chart-open-btn" style="display:none;font-size:12px;color:var(--gold);">Xem →</span></div>
            </div>
            <div class="card" style="padding:16px;cursor:pointer;" id="chart-bazi" onclick="goToChart('bazi')">
              <div style="display:flex;align-items:center;gap:8px;"><span>&#9671;</span><span style="flex:1;">BaZi</span><span class="badge badge-pro chart-lock-badge" style="font-size:10px;">PRO</span><span class="chart-open-btn" style="display:none;font-size:12px;color:var(--gold);">Xem →</span></div>
            </div>
            <div class="card" style="padding:16px;cursor:pointer;" id="chart-hd" onclick="goToChart('hd')">
              <div style="display:flex;align-items:center;gap:8px;"><span>&#9651;</span><span style="flex:1;">Human Design</span><span class="badge badge-pro chart-lock-badge" style="font-size:10px;">PRO</span><span class="chart-open-btn" style="display:none;font-size:12px;color:var(--gold);">Xem →</span></div>
            </div>
            <div class="card" style="padding:16px;cursor:pointer;" id="chart-num" onclick="goToChart('numerology')">
              <div style="display:flex;align-items:center;gap:8px;"><span>&#9675;</span><span style="flex:1;">Số học</span><span class="badge badge-pro chart-lock-badge" style="font-size:10px;">PRO</span><span class="chart-open-btn" style="display:none;font-size:12px;color:var(--gold);">Xem →</span></div>
            </div>
            <div class="card" style="padding:16px;cursor:pointer;" id="chart-vedic" onclick="goToChart('vedic')">
              <div style="display:flex;align-items:center;gap:8px;"><span>&#9734;</span><span style="flex:1;">Vedic</span><span class="badge badge-pro chart-lock-badge" style="font-size:10px;">PRO</span><span class="chart-open-btn" style="display:none;font-size:12px;color:var(--gold);">Xem →</span></div>
            </div>
          </div>
          <div id="s4-chart-cta-locked"><button class="btn btn-gold btn-full" style="margin-top:16px;" onclick="openCheckout('pro')">Mở khóa biểu đồ</button></div>
          <div id="s4-chart-cta-unlocked" style="display:none;"><button class="btn btn-ghost btn-full btn-sm" style="margin-top:16px;" onclick="showScreen('s5')">Xem toàn bộ biểu đồ →</button></div>
          <div style="margin-top:24px;padding:16px;background:var(--sand);border-radius:var(--radius-lg);text-align:center;">
            <p style="font-size:14px;margin-bottom:8px;">Có câu hỏi cụ thể hơn?</p>
            <button class="btn btn-ghost btn-sm" onclick="showScreen('s6')">Phân tích sâu →</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
'''

with open(path, 'a', encoding='utf-8') as f:
    f.write(p2)
print('part2 done', len(p2))
