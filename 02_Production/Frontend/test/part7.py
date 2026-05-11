
path = 'C:/Users/Admin/Desktop/Visionaries_Startup_April/02_Production/Frontend/test/index.html'

p7 = '''
<script>
/* ═══ GLOBAL STATE ═══ */
let appTier = 'FREE'; // 'FREE' | 'PRO'
let _coTimer = null;
let _coPlan = 'pro';

/* ═══ SCREEN NAVIGATION ═══ */
function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  window.scrollTo(0, 0);
}

/* ═══ AUTH TABS ═══ */
function switchTab2(which) {
  document.getElementById('register').style.display = which === 'register' ? 'block' : 'none';
  document.getElementById('login').style.display    = which === 'login'    ? 'block' : 'none';
  document.getElementById('tab-register').classList.toggle('active', which === 'register');
  document.getElementById('tab-login').classList.toggle('active', which === 'login');
}

/* ═══ ONBOARDING ═══ */
function selectGender(btn, val) {
  document.querySelectorAll('#gender-group button').forEach(b => {
    b.classList.remove('btn-gold'); b.classList.add('btn-ghost');
  });
  btn.classList.remove('btn-ghost'); btn.classList.add('btn-gold');
  updateProgress();
}

function updateProgress() {
  const checks = [
    document.getElementById('ob-name')?.value.trim(),
    document.querySelector('#gender-group .btn-gold'),
    document.getElementById('ob-day')?.value.trim(),
    document.getElementById('ob-month')?.value.trim(),
    document.getElementById('ob-year')?.value.trim(),
    document.getElementById('ob-time')?.value.trim() || document.getElementById('ob-no-time')?.checked,
    document.getElementById('ob-city')?.value.trim()
  ];
  const filled = checks.filter(Boolean).length;
  const pct = Math.round((filled / checks.length) * 100);
  document.getElementById('onboard-progress').style.width = pct + '%';
  document.getElementById('onboard-step-label').textContent = filled + ' / ' + checks.length + ' hoàn thành';
}

function showLoading() {
  const overlay = document.getElementById('loading-overlay');
  overlay.style.display = 'flex';
  const systems = [
    { name: 'Số học', icon: '○' },
    { name: 'BaZi', icon: '◇' },
    { name: 'Tử Vi', icon: '⬡' },
    { name: 'Vedic', icon: '☆' },
    { name: 'Human Design', icon: '△' }
  ];
  const container = document.getElementById('loading-layers');
  container.innerHTML = '';
  systems.forEach((sys, i) => {
    const el = document.createElement('div');
    el.style.cssText = 'display:flex;align-items:center;gap:12px;padding:12px 16px;border-radius:8px;background:var(--sand);transition:all 0.5s;';
    el.innerHTML = '<span style="font-size:20px;opacity:0.3;">' + sys.icon + '</span><span style="color:var(--stone);flex:1;">' + sys.name + '</span><div style="width:120px;"><div class="progress-bar"><div class="fill" style="width:0%"></div></div></div>';
    container.appendChild(el);
    setTimeout(() => {
      el.style.background = 'var(--gold-bg)';
      el.querySelector('.fill').style.width = '100%';
      el.querySelector('span').style.opacity = '1';
      el.querySelector('span').style.color = 'var(--gold)';
      el.querySelectorAll('span')[1].style.color = 'var(--ink)';
      el.querySelectorAll('span')[1].style.fontWeight = '500';
    }, (i + 1) * 700);
  });
  setTimeout(() => {
    overlay.style.display = 'none';
    showScreen('s4');
  }, 4200);
}

/* ═══ ACCORDION ═══ */
function toggleAccordion(header) {
  const item = header.parentElement;
  if (item.classList.contains('locked')) return;
  const wasOpen = item.classList.contains('open');
  item.closest('.app-main').querySelectorAll('.accordion-item:not(.locked)').forEach(a => a.classList.remove('open'));
  if (!wasOpen) item.classList.add('open');
}

function handleLockedTopic(item, n) {
  if (item.classList.contains('locked')) { openCheckout('pro'); return; }
  const header = item.querySelector('.accordion-header');
  toggleAccordion(header);
}

/* ═══ S5 SYSTEM TABS ═══ */
function switchS5Tab(tabEl, panelId) {
  document.querySelectorAll('#s5-tabs .tab').forEach(t => t.classList.remove('active'));
  tabEl.classList.add('active');
  document.querySelectorAll('#s5 .tab-panel').forEach(p => p.classList.remove('active'));
  document.getElementById('panel-' + panelId).classList.add('active');
  const names = {'tu-vi':'Tử Vi','bazi':'BaZi','hd':'Human Design','numerology':'Số học','vedic':'Vedic'};
  document.getElementById('s5-breadcrumb').textContent = names[panelId];
}

function goToChart(tab) {
  if (appTier === 'FREE') { openCheckout('pro'); return; }
  showScreen('s5');
  const tabEl = document.querySelector('#s5-tabs [data-tab="' + tab + '"]');
  if (tabEl) switchS5Tab(tabEl, tab);
}

/* ═══ Q&A SIMULATION ═══ */
const qaResponses = {
  default: 'Dựa trên biểu đồ của bạn — với Canh Kim Nhật Chủ trong BaZi và Profile 4/6 trong Human Design — câu hỏi này chạm đến một pattern rất cốt lõi. Kim gặp lửa đôi Ngọ tạo ra áp lực liên tục đòi hỏi sự hoàn hảo trước khi hành động. Profile 4/6 (Opportunist/Role Model) cần cảm thấy an toàn trong nền tảng trước khi mạo hiểm. Kết hợp lại, đây là cơ chế bảo vệ tiến hóa — không phải điểm yếu. Hành động đề xuất: Thực hành "done is better than perfect" bằng cách đặt deadline cứng 72 giờ cho mọi quyết định nhỏ.',
  'trihoai': 'Trì hoãn của bạn không phải lười biếng — đây là cơ chế Kiêu Thần trong BaZi (Can Kiêu tọa Ngọ). Canh Kim khi gặp Hỏa mạnh có xu hướng "chờ điều kiện hoàn hảo" trước khi hành động. Trong Human Design, Will Center không xác định của bạn nghĩa là bạn không có áp lực nội tại tự nhiên — cần tạo ra cấu trúc bên ngoài. Giải pháp: Thay "tôi phải làm thật tốt" bằng "tôi thử xem sao" — giảm áp lực tự áp đặt.',
  'quanhe': 'Với Profile 4/6 và Emotional Authority, bạn cần thời gian cảm xúc để ra quyết định trong quan hệ — đừng ép bản thân quyết định ngay. Người phù hợp nhất là những ai có tư duy rõ ràng (compatible với Life Path 7 của bạn) và cho bạn không gian một mình mà không cảm thấy bị từ chối.',
  'diem-manh': 'Điểm mạnh cốt lõi: Tư duy hệ thống bậc cao (Defined Ajna + Life Path 7), khả năng kết nối ý tưởng từ nhiều lĩnh vực (Profile 4/6 + Expression 3), và bền bỉ phi thường khi cam kết (Canh Kim — kim loại cứng nhất). Đây là tổ hợp hiếm gặp của nhà tư tưởng-truyền đạt.'
};

function getQAResponse(question) {
  const q = question.toLowerCase();
  if (q.includes('trì hoãn') || q.includes('chậm') || q.includes('delay')) return qaResponses['trihoai'];
  if (q.includes('quan hệ') || q.includes('tình cảm') || q.includes('yêu') || q.includes('bạn đời')) return qaResponses['quanhe'];
  if (q.includes('điểm mạnh') || q.includes('tài năng') || q.includes('giỏi')) return qaResponses['diem-manh'];
  return qaResponses.default;
}

function sendQA(inputId) {
  const inputEl = document.getElementById(inputId + '-input');
  const resultEl = document.getElementById(inputId + '-result');
  if (!inputEl || !resultEl) return;
  const question = inputEl.value.trim();
  if (!question) return;
  inputEl.disabled = true;
  resultEl.style.display = 'block';
  resultEl.innerHTML = '<div class="qa-loading"><div class="qa-dot"></div><div class="qa-dot"></div><div class="qa-dot"></div><span class="muted" style="font-size:13px;margin-left:8px;">Đang phân tích...</span></div>';
  setTimeout(() => {
    const resp = getQAResponse(question);
    resultEl.innerHTML = '<div class="qa-response"></div>';
    const textEl = resultEl.querySelector('.qa-response');
    let i = 0;
    function typeChar() {
      if (i < resp.length) {
        textEl.innerHTML = resp.substring(0, i + 1) + '<span class="qa-cursor"></span>';
        i++;
        setTimeout(typeChar, 18);
      } else { textEl.innerHTML = resp; }
    }
    typeChar();
    inputEl.disabled = false;
    inputEl.value = '';
  }, 1500);
}

function fillQA(screenId, text) {
  const el = document.getElementById(screenId + '-qa-input');
  if (el) { el.value = text; el.focus(); }
}

/* ═══ S6 DEEP DIVE ═══ */
const deepDiveResponses = {
  'self-sabotage': 'Đây là pattern Kiêu Thần trong BaZi — khi Canh Kim gần đến đỉnh, Kiêu Thần (Can Thực/Thương) cản trở bằng cách tạo ra nghi ngờ bản thân. Trong Human Design, Will Center không xác định hấp thu năng lượng willpower từ người xung quanh — khi một mình, willpower giảm đột ngột ngay trước finish line. Giải pháp: Tạo "accountability partner" cho giai đoạn nước rút cuối cùng của mọi dự án lớn.',
  'leader': 'Biểu đồ của bạn cho thấy bạn có tố chất lãnh đạo — nhưng theo kiểu của Profile 4/6: dẫn dắt bằng ví dụ và sự tin tưởng, không phải bằng quyền lực. Tham Lang miếu địa (Tử Vi) tạo sức ảnh hưởng tự nhiên. Manifesting Generator (HD) thực ra rất phù hợp làm entrepreneur vì cần làm nhiều thứ song song. Saturn Dasha hiện tại ủng hộ việc xây dựng doanh nghiệp nếu bạn sẵn sàng đi chậm và chắc.',
  'default': 'Dựa trên phân tích tổng hợp từ 5 hệ thống — BaZi, Tử Vi, Human Design, Số học, và Vedic — câu hỏi này liên quan đến một pattern cốt lõi trong biểu đồ của bạn. Canh Kim Nhật Chủ gặp lửa đôi Ngọ tạo ra áp lực liên tục đòi hỏi sự chuyển hóa. Kết hợp với Profile 4/6 trong Human Design và Life Path 7 trong Số học, bạn được thiết kế để trả lời những câu hỏi sâu sắc — nhưng cần thời gian và không gian để tìm thấy câu trả lời thật sự. Hành động cụ thể: Tạo ra một nghi thức suy nghĩ hàng ngày (10–15 phút) — không có điện thoại, không có input bên ngoài. Đây là khi Ajna Center defined của bạn hoạt động tốt nhất.'
};

function s6FillQuestion(btn) {
  document.getElementById('s6-question').value = btn.textContent.trim();
  document.getElementById('s6-question').focus();
}

function s6LoadHistory(n) {
  const questions = ['Tại sao tôi hay trì hoãn?', 'Mối quan hệ nào phù hợp với tôi?'];
  document.getElementById('s6-question').value = questions[n-1];
  sendDeepDive();
}

function s6Reset() {
  document.getElementById('s6-result').style.display = 'none';
  document.getElementById('s6-loading').style.display = 'none';
  document.getElementById('s6-empty').style.display = 'flex';
  document.getElementById('s6-question').value = '';
}

function sendDeepDive() {
  const q = document.getElementById('s6-question').value.trim();
  if (!q) return;
  document.getElementById('s6-empty').style.display = 'none';
  document.getElementById('s6-result').style.display = 'none';
  document.getElementById('s6-loading').style.display = 'block';
  const bars = [1,2,3,4,5];
  bars.forEach((i, idx) => {
    setTimeout(() => {
      const bar = document.getElementById('s6-p' + i);
      const layer = document.getElementById('s6-l' + i);
      if (bar) { bar.style.width = '100%'; bar.style.transition = 'width 0.6s'; }
      if (layer) { layer.style.background = 'var(--gold-bg)'; }
    }, idx * 600);
  });
  setTimeout(() => {
    document.getElementById('s6-loading').style.display = 'none';
    document.getElementById('s6-result').style.display = 'block';
    document.getElementById('s6-result-title').textContent = 'Phân tích: ' + (q.length > 60 ? q.substring(0,60) + '...' : q);
    const qLower = q.toLowerCase();
    let resp = deepDiveResponses.default;
    if (qLower.includes('tự phá hoại') || qLower.includes('gần thành công')) resp = deepDiveResponses['self-sabotage'];
    if (qLower.includes('lãnh đạo') || qLower.includes('entrepreneur') || qLower.includes('business')) resp = deepDiveResponses['leader'];
    document.getElementById('s6-result-body').innerHTML = '<p>' + resp + '</p>';
    bars.forEach(i => {
      const p = document.getElementById('s6-p' + i);
      const l = document.getElementById('s6-l' + i);
      if (p) { p.style.width = '0%'; p.style.transition = 'none'; }
      if (l) { l.style.background = 'var(--sand)'; }
    });
  }, 3200);
}

/* ═══ S9 TIME ORACLE ═══ */
function s9GoLevel(level) {
  if (appTier === 'FREE') { openCheckout('pro'); return; }
}

function s9SelectMonth(m) {
  alert('Tháng ' + m + ': Xem chi tiết tháng này — tính năng drill-down đầy đủ trong production');
}

/* ═══ S10 ACTIONS ═══ */
const actionData = {
  1: { what: 'Canh Kim Nhật Chủ gặp lửa đôi Ngọ — bạn có xu hướng xử lý quá nhiều trong đầu mà không xả ra. Viết nhật ký là cách "thoát nhiệt" cho hệ thống Kim-Hỏa của bạn.', why: 'BaZi — Canh Kim cần Thủy để điều hòa. Viết nhật ký kích hoạt hành Thủy (ngôn từ, suy nghĩ có hệ thống) trong cuộc sống hàng ngày.', system: 'BaZi' },
  2: { what: 'Tham Lang miếu địa tại Cung Mệnh tạo sức hút tự nhiên — người và cơ hội tìm đến bạn liên tục. Nếu không học cách từ chối, bạn sẽ phân tán năng lượng và không đạt được điều nào sâu sắc.', why: 'Tử Vi — Tham Lang là sao đa tài nhưng dễ phân tán. Kỷ luật chọn lọc là cách khai thác Tham Lang ở mức cao nhất.', system: 'Tử Vi' },
  3: { what: 'Manifesting Generator với Emotional Authority cần thời gian cảm xúc để ra quyết định đúng. Sacral response là "cảm giác ruột" — uh-huh (có) hoặc uh-uh (không) — đây là la bàn nội tại chính xác nhất của bạn.', why: 'Human Design — Manifesting Generator phản ứng với Sacral Center. Bỏ qua Sacral = quyết định sai. Emotional Authority yêu cầu thêm thời gian để cảm xúc lắng đọng.', system: 'HD' },
  4: { what: 'Manifesting Generator cần thời gian solo để phân biệt năng lượng nào là của mình vs của người khác. Sau những buổi xã hội, cơ thể bạn cần reset hoàn toàn.', why: 'Human Design — Sacral undefined khuếch đại năng lượng từ môi trường. Thời gian solo là thiết yếu, không phải xa xỉ.', system: 'HD' },
  5: { what: 'Life Path 7 được thiết kế để đi sâu vào một lĩnh vực, không mở rộng liên tục. Mỗi kỹ năng chuyên sâu bạn học tạo ra một "tầng" mới của sự hiểu biết.', why: 'Số học — Life Path 7 (Seeker) phát triển qua chiều sâu và sự nghiên cứu. Khác với Life Path 3 (bề rộng), số 7 cần đào sâu để tỏa sáng.', system: 'Số học' },
  6: { what: 'Soul Urge 9 cho thấy ở cấp độ sâu nhất, bạn muốn cống hiến và để lại di sản có ý nghĩa. Tất cả hành động khác trong pyramid đều dẫn đến điểm này.', why: 'Số học — Soul Urge 9 là số của sự hoàn thành chu kỳ và cống hiến nhân loại. Cần được sống có ý thức để tránh cảm giác rỗng tuếch dù thành công vật chất.', system: 'Số học' },
  7: { what: 'Scorpio Ascendant (Vedic) kết hợp Profile 4/6 (HD) tạo ra người để lại dấu ấn sâu sắc qua sự biến đổi. Di sản của bạn là những người bạn giúp chuyển hóa.', why: 'Vedic + HD — Saturn Dasha (2021–2040) là thời gian lý tưởng để bắt đầu dự án di sản. Saturn thưởng kỷ luật và tầm nhìn dài hạn.', system: 'Tổng hợp' }
};

function s10SelectAction(n) {
  const data = actionData[n];
  if (!data) return;
  document.getElementById('s10-what-text').innerHTML = data.what;
  document.getElementById('s10-why-content').innerHTML =
    '<div style="display:flex;align-items:center;gap:8px;margin-bottom:12px;"><span class="badge-system">' + data.system + '</span><span style="font-size:15px;font-weight:500;">' + data.system + ' Analysis</span></div><p style="font-size:15px;line-height:1.8;">' + data.why + '</p>';
  document.querySelectorAll('[id^=s10-action-]').forEach(el => el.style.border = '');
  const el = document.getElementById('s10-action-' + n);
  if (el) el.style.border = '2px solid var(--gold)';
}

function s10SelectLayer(layer) {
  if (layer !== 'base' && appTier === 'FREE') { openCheckout('pro'); return; }
  document.getElementById('s10-actions-base').style.display = layer === 'base' ? 'block' : 'none';
  document.getElementById('s10-actions-mid').style.display  = layer === 'mid'  ? 'block' : 'none';
  document.getElementById('s10-actions-top').style.display  = layer === 'top'  ? 'block' : 'none';
  ['base','mid','top'].forEach(l => {
    const el = document.getElementById('pyr-' + l);
    if (!el) return;
    if (l === layer) { el.setAttribute('fill', 'var(--gold-bg)'); el.setAttribute('stroke', 'var(--gold)'); }
    else { el.setAttribute('fill', 'none'); el.setAttribute('stroke', 'var(--border)'); }
  });
  document.getElementById('pyr-base').setAttribute('fill', 'var(--gold-bg)');
}

function updateActionProgress(checkbox, n) {
  const checked = document.querySelectorAll('#s10-actions-base input[type=checkbox]:checked').length;
  const total = document.querySelectorAll('#s10-actions-base input[type=checkbox]').length;
  document.getElementById('s10-base-count').textContent = checked + '/' + total;
  document.getElementById('s10-base-progress').style.width = (checked / total * 100) + '%';
}

/* ═══ TIER STATE SYSTEM (FREE | PRO only) ═══ */
function applyTierState(tier) {
  appTier = tier;
  updateTierUI();
}

function updateTierUI() {
  const isPro = appTier === 'PRO';
  const tierLabel = appTier;
  const badgeClass = isPro ? 'badge-pro' : 'badge-free';

  ['s4-tier-badge','s5-tier-badge','s6-tier-badge','s8-tier-badge','s9-tier-badge','s10-tier-badge'].forEach(id => {
    const el = document.getElementById(id);
    if (!el) return;
    el.className = 'badge ' + badgeClass;
    el.textContent = tierLabel;
  });
  const s8badge = document.getElementById('s8-tier-badge');
  if (s8badge) { s8badge.className = 'badge ' + badgeClass; s8badge.textContent = tierLabel; }
  const s8profile = document.getElementById('s8-profile-badge');
  if (s8profile) { s8profile.className = 'badge ' + badgeClass; s8profile.textContent = tierLabel; }
  const s8upgrade = document.getElementById('s8-upgrade-link');
  if (s8upgrade) s8upgrade.style.display = isPro ? 'none' : 'inline';

  // S4: PRO Banner
  document.getElementById('s4-pro-banner').style.display = isPro ? 'block' : 'none';

  // S4: Progress bar
  document.getElementById('s4-progress-fill').style.width = isPro ? '100%' : '20%';
  document.getElementById('s4-progress-label').innerHTML = isPro
    ? '10/10 chủ đề — <span style="color:var(--success);">Đã mở khóa ✓</span>'
    : '2/10 chủ đề — <a href="#" style="color:var(--gold);" onclick="showScreen(\'s7\')">Mở khóa thêm 8 với PRO</a>';

  // S4: PDF export — available in PRO
  const pdfBtn = document.getElementById('s4-pdf-btn');
  if (isPro) {
    pdfBtn.removeAttribute('disabled');
    pdfBtn.style.opacity = '1';
    pdfBtn.style.cursor = 'pointer';
    pdfBtn.textContent = 'Xuất PDF';
    pdfBtn.onclick = () => alert('Đang tạo PDF 36 trang... (production feature)');
  } else {
    pdfBtn.setAttribute('disabled', true);
    pdfBtn.style.opacity = '0.4';
    pdfBtn.style.cursor = 'not-allowed';
    pdfBtn.innerHTML = 'Xuất PDF &#128274;';
  }

  // S4: Unlock topics 3-10
  for (let n = 3; n <= 10; n++) {
    const item = document.getElementById('topic-' + n);
    const lock  = document.getElementById('lock-' + n);
    if (!item) continue;
    if (isPro) { item.classList.remove('locked'); if (lock) lock.style.display = 'none'; }
    else       { item.classList.add('locked');    if (lock) lock.style.display = ''; }
  }

  // S4: Q&A
  document.getElementById('s4-qa-locked').style.display = isPro ? 'none'  : 'block';
  document.getElementById('s4-qa-active').style.display = isPro ? 'block' : 'none';

  // S4: Charts
  document.querySelectorAll('.chart-lock-badge').forEach(el => el.style.display = isPro ? 'none' : '');
  document.querySelectorAll('.chart-open-btn').forEach(el => el.style.display = isPro ? 'inline' : 'none');
  document.getElementById('s4-chart-cta-locked').style.display   = isPro ? 'none'  : 'block';
  document.getElementById('s4-chart-cta-unlocked').style.display = isPro ? 'block' : 'none';

  // S9: Upsell + Layers
  document.getElementById('s9-upsell').style.display   = isPro ? 'none'  : 'flex';
  document.getElementById('s9-layer1').style.display   = isPro ? 'block' : 'none';
  document.getElementById('s9-layer2').style.display   = isPro ? 'block' : 'none';
  const bcLifetime = document.getElementById('bc-lifetime');
  const bcYear     = document.getElementById('bc-year');
  if (bcLifetime) { bcLifetime.style.opacity = isPro ? '1' : '0.4'; bcLifetime.style.cursor = isPro ? 'pointer' : 'not-allowed'; }
  if (bcYear)     { bcYear.style.opacity     = isPro ? '1' : '0.4'; bcYear.style.cursor     = isPro ? 'pointer' : 'not-allowed'; }

  // S10: Pyramid
  document.getElementById('s10-upsell').style.display      = isPro ? 'none'  : 'block';
  document.getElementById('s10-actions-mid').style.display = isPro ? 'block' : 'none';
  document.getElementById('s10-actions-top').style.display = isPro ? 'block' : 'none';
  const pyrMid = document.getElementById('pyr-mid');
  const pyrTop = document.getElementById('pyr-top');
  const pyrMidLabel = document.getElementById('pyr-mid-label');
  const pyrTopLabel = document.getElementById('pyr-top-label');
  if (isPro) {
    if (pyrMid) { pyrMid.setAttribute('fill', 'var(--sand)'); pyrMid.setAttribute('stroke', 'var(--border)'); }
    if (pyrTop) { pyrTop.setAttribute('fill', 'var(--sand)'); pyrTop.setAttribute('stroke', 'var(--border)'); }
    if (pyrMidLabel) pyrMidLabel.textContent = 'Nuôi Dưỡng';
    if (pyrTopLabel) pyrTopLabel.textContent = 'Khai Phóng';
  } else {
    if (pyrMidLabel) pyrMidLabel.textContent = 'Nuôi Dưỡng 🔒';
    if (pyrTopLabel) pyrTopLabel.textContent = 'Khai Phóng 🔒';
  }

  // Dev tier toggle btn
  const btn = document.getElementById('tier-toggle-btn');
  if (btn) {
    btn.textContent = 'Tier: ' + appTier;
    btn.className = 'tier-toggle ' + appTier.toLowerCase();
  }
}

function cycleTier() {
  const tiers = ['FREE','PRO'];
  const next = tiers[(tiers.indexOf(appTier) + 1) % tiers.length];
  applyTierState(next);
}

/* ═══ CHECKOUT ═══ */
function openCheckout(plan) {
  _coPlan = plan || 'pro';
  const price = '199.000đ';
  document.getElementById('co-title').textContent = 'Nâng cấp PRO';
  document.getElementById('co-subtitle').textContent = price + ' · Lifetime · 1 hồ sơ';
  document.getElementById('co-qr-amount').textContent = price;
  document.getElementById('co-card-pay-btn').textContent = 'Thanh toán ' + price;
  const m = document.getElementById('checkout-modal');
  m.classList.add('open');
  document.body.style.overflow = 'hidden';
  _coReset();
}

function closeCheckout() {
  document.getElementById('checkout-modal').classList.remove('open');
  document.body.style.overflow = '';
  if (_coTimer) { clearInterval(_coTimer); _coTimer = null; }
}

function _coReset() {
  ['co-step1','co-step2-vietqr','co-step2-card','co-step3-success','co-step3-failure'].forEach(id => {
    document.getElementById(id).style.display = 'none';
  });
  document.getElementById('co-step1').style.display = 'block';
  document.getElementById('co-indicators').style.display = 'flex';
  _coSetStep(1);
  if (_coTimer) { clearInterval(_coTimer); _coTimer = null; }
}

function _coSetStep(n) {
  [1,2,3].forEach(i => {
    document.getElementById('co-ind-' + i).style.background = i <= n ? 'var(--ink)' : 'var(--border)';
  });
}

function coSelectMethod(method) {
  document.getElementById('co-step1').style.display = 'none';
  _coSetStep(2);
  if (method === 'vietqr') {
    document.getElementById('co-step2-vietqr').style.display = 'block';
    _coStartCountdown();
  } else {
    document.getElementById('co-step2-card').style.display = 'block';
  }
}

function _coStartCountdown() {
  let secs = 15 * 60;
  const el = document.getElementById('co-countdown');
  function tick() {
    secs--;
    if (secs <= 0) {
      clearInterval(_coTimer); _coTimer = null;
      document.getElementById('co-error-msg').textContent = 'QR đã hết hạn. Vui lòng thử lại.';
      _coShowResult('failure'); return;
    }
    const m = Math.floor(secs / 60), s = secs % 60;
    el.textContent = m + ':' + String(s).padStart(2, '0');
  }
  tick();
  _coTimer = setInterval(tick, 1000);
}

function coSubmitCard() {
  const num = document.getElementById('co-card-num').value.replace(/\s/g, '');
  if (num.length < 16) { alert('Vui lòng nhập đầy đủ số thẻ.'); return; }
  coSimulateSuccess();
}

function coSimulateSuccess() {
  if (_coTimer) { clearInterval(_coTimer); _coTimer = null; }
  document.getElementById('co-success-title').textContent = 'Nâng cấp thành công!';
  document.getElementById('co-success-desc').innerHTML = 'Chào mừng bạn đến với <strong>360Human PRO</strong>.';
  _coShowResult('success');
  applyTierState('PRO');
}

function coSimulateFailure() {
  if (_coTimer) { clearInterval(_coTimer); _coTimer = null; }
  document.getElementById('co-error-msg').textContent = 'Giao dịch không thể hoàn thành. Vui lòng thử lại.';
  _coShowResult('failure');
}

function _coShowResult(type) {
  ['co-step2-vietqr','co-step2-card'].forEach(id => { document.getElementById(id).style.display = 'none'; });
  document.getElementById('co-step3-' + type).style.display = 'block';
  document.getElementById('co-indicators').style.display = type === 'success' ? 'none' : 'flex';
  _coSetStep(3);
}

function coRetry() {
  document.getElementById('co-step3-failure').style.display = 'none';
  _coReset();
}

function coFormatCard(input) {
  let v = input.value.replace(/\D/g, '').substring(0, 16);
  input.value = v.replace(/(.{4})/g, '$1 ').trim();
}

function coFormatExpiry(input) {
  let v = input.value.replace(/\D/g, '').substring(0, 4);
  if (v.length > 2) v = v.slice(0,2) + '/' + v.slice(2);
  input.value = v;
}

document.getElementById('checkout-modal').addEventListener('click', function(e) {
  if (e.target === this) closeCheckout();
});

/* ═══ FORGOT PASSWORD ═══ */
function openForgotPassword() {
  const m = document.getElementById('forgot-modal');
  m.style.display = 'flex';
  document.getElementById('forgot-step1').style.display = 'block';
  document.getElementById('forgot-step2').style.display = 'none';
}

function closeForgotPassword() {
  document.getElementById('forgot-modal').style.display = 'none';
}

function sendForgotPassword() {
  const email = document.getElementById('forgot-email').value.trim();
  if (!email) { alert('Vui lòng nhập email.'); return; }
  document.getElementById('forgot-step1').style.display = 'none';
  document.getElementById('forgot-email-display').textContent = email;
  document.getElementById('forgot-step2').style.display = 'block';
}

document.getElementById('forgot-modal').addEventListener('click', function(e) {
  if (e.target === this) closeForgotPassword();
});

/* ═══ PROFILE SETTINGS ═══ */
function toggleBirthEdit() {
  const disp = document.getElementById('birth-display');
  const edit = document.getElementById('birth-edit');
  const isEditing = edit.style.display !== 'none';
  edit.style.display = isEditing ? 'none' : 'block';
  disp.style.display = isEditing ? 'block' : 'none';
}

function togglePasswordForm() {
  document.getElementById('password-form').classList.toggle('open');
}

function confirmDeleteAccount() {
  if (confirm('Bạn có chắc chắn muốn xóa tài khoản? Hành động này không thể hoàn tác.')) {
    alert('Tài khoản đã được gửi yêu cầu xóa. Bạn sẽ nhận email xác nhận.');
  }
}

/* ═══ MOBILE NAV ═══ */
function openMobileNav() {
  document.getElementById('mob-overlay').classList.add('open');
  document.getElementById('mob-sidebar').classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeMobileNav() {
  document.getElementById('mob-overlay').classList.remove('open');
  document.getElementById('mob-sidebar').classList.remove('open');
  document.body.style.overflow = '';
}

/* ═══ INIT ═══ */
updateTierUI();
</script>
</body>
</html>
'''

with open(path, 'a', encoding='utf-8') as f:
    f.write(p7)
print('part7 done', len(p7))
