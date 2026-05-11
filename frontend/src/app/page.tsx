import Link from "next/link";

export default function HomePage() {
  return (
    <div className="min-h-screen bg-cream">
      {/* Header */}
      <header className="flex items-center justify-between px-12 py-4 absolute top-0 left-0 right-0 z-10">
        <div className="font-[family-name:var(--font-display)] text-xl font-semibold">360Human</div>
        <div className="flex gap-3">
          <Link
            href="/login"
            className="inline-flex items-center justify-center px-4 py-2 text-sm font-medium border border-border rounded-md text-charcoal hover:bg-sand transition-colors no-underline"
          >
            Đăng nhập
          </Link>
          <Link
            href="/register"
            className="inline-flex items-center justify-center px-4 py-2 text-sm font-medium bg-gold text-white rounded-md hover:bg-gold-soft transition-colors no-underline"
          >
            Đăng ký
          </Link>
        </div>
      </header>

      {/* Hero */}
      <section className="min-h-[90vh] flex items-center px-12 pt-[120px] pb-16">
        <div className="max-w-[1280px] mx-auto flex gap-16 items-center w-full">
          {/* Wheel Visual */}
          <div className="flex-1 flex items-center justify-center">
            <div className="w-[300px] h-[300px] relative">
              <svg viewBox="0 0 300 200" className="w-full">
                <path d="M 20 150 Q 75 50 150 100 Q 225 150 280 60" stroke="var(--color-gold)" strokeWidth="2" fill="none" strokeDasharray="4,4"/>
                <circle cx="150" cy="100" r="30" fill="none" stroke="var(--color-gold)" strokeWidth="2"/>
                <circle cx="150" cy="100" r="15" fill="var(--color-gold-bg)" stroke="var(--color-gold)" strokeWidth="1"/>
                <line x1="150" y1="70" x2="150" y2="40" stroke="var(--color-gold)" strokeWidth="1"/>
                <line x1="180" y1="100" x2="210" y2="100" stroke="var(--color-gold)" strokeWidth="1"/>
                <line x1="150" y1="130" x2="150" y2="160" stroke="var(--color-gold)" strokeWidth="1"/>
                <line x1="120" y1="100" x2="90" y2="100" stroke="var(--color-gold)" strokeWidth="1"/>
                <line x1="172" y1="78" x2="195" y2="55" stroke="var(--color-gold)" strokeWidth="1"/>
                <text x="150" y="38" textAnchor="middle" className="text-[9px] fill-stone font-[family-name:var(--font-mono)]">Tử Vi</text>
                <text x="218" y="104" className="text-[9px] fill-stone font-[family-name:var(--font-mono)]">BaZi</text>
                <text x="150" y="175" textAnchor="middle" className="text-[9px] fill-stone font-[family-name:var(--font-mono)]">Số học</text>
                <text x="68" y="104" textAnchor="end" className="text-[9px] fill-stone font-[family-name:var(--font-mono)]">Vedic</text>
                <text x="200" y="52" className="text-[9px] fill-stone font-[family-name:var(--font-mono)]">HD</text>
              </svg>
            </div>
          </div>
          {/* Text */}
          <div className="flex-1">
            <h1 className="mb-4">Hiểu mình sâu hơn,<br/>sống đúng hơn</h1>
            <p className="text-lg text-charcoal mb-8 max-w-[480px] leading-relaxed">
              5 hệ thống phân tích — một bức tranh toàn diện về con người bạn. Không phải tử vi chung chung. Đây là bản đồ riêng của bạn.
            </p>
            <div className="flex gap-4 items-center">
              <Link
                href="/register"
                className="inline-flex items-center justify-center px-8 py-4 text-base font-medium bg-gold text-white rounded-md hover:bg-gold-soft transition-colors no-underline"
              >
                Khám phá bản thân
              </Link>
              <a href="#how" className="text-stone text-[15px] no-underline hover:text-charcoal transition-colors">Tìm hiểu thêm ↓</a>
            </div>
          </div>
        </div>
      </section>

      {/* Value Props */}
      <section className="py-16 px-12 bg-sand">
        <div className="max-w-[1280px] mx-auto">
          <div className="flex gap-6">
            <div className="flex-1 bg-warm-white border border-border rounded-xl shadow-sm p-6 text-center">
              <div className="text-[32px] mb-3">⬡</div>
              <h3>5 hệ thống</h3>
              <p className="text-stone text-[15px] mt-2">Tử Vi, BaZi, Human Design, Số học, Vedic — cross-referenced</p>
            </div>
            <div className="flex-1 bg-warm-white border border-border rounded-xl shadow-sm p-6 text-center">
              <div className="text-[32px] mb-3">◇</div>
              <h3>20.000+ trang tài liệu</h3>
              <p className="text-stone text-[15px] mt-2">Knowledge base nghiên cứu chuyên sâu, không phải copy-paste</p>
            </div>
            <div className="flex-1 bg-warm-white border border-border rounded-xl shadow-sm p-6 text-center">
              <div className="text-[32px] mb-3">○</div>
              <h3>Cá nhân hóa cho riêng bạn</h3>
              <p className="text-stone text-[15px] mt-2">Không phải tử vi chung. Mọi thứ tính từ dữ liệu sinh của bạn</p>
            </div>
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section id="how" className="py-24 px-12">
        <div className="max-w-[960px] mx-auto text-center">
          <h2 className="mb-12">Bạn chỉ cần 4 bước</h2>
          <div className="flex gap-8">
            {[
              { num: "1", title: "Nhập thông tin", desc: "Họ tên, ngày giờ, nơi sinh" },
              { num: "2", title: "Phân tích", desc: "5 hệ thống tính toán biểu đồ" },
              { num: "3", title: "Đọc chi tiết", desc: "10 chủ đề phân tích chuyên sâu" },
              { num: "4", title: "Hỏi & Đáp", desc: "Đặt câu hỏi, nhận trả lời cá nhân" },
            ].map((step) => (
              <div key={step.num} className="flex-1">
                <div className="font-[family-name:var(--font-display)] text-[40px] text-gold mb-2">{step.num}</div>
                <h4 className="font-semibold text-base">{step.title}</h4>
                <p className="text-stone text-sm">{step.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Pricing Teaser */}
      <section className="py-12 text-center border-t border-border">
        <p className="text-stone">Bắt đầu miễn phí — Không cần thẻ</p>
        <Link
          href="/pricing"
          className="inline-flex items-center justify-center px-6 py-3 mt-4 font-medium bg-gold text-white rounded-md hover:bg-gold-soft transition-colors no-underline"
        >
          Xem bảng giá
        </Link>
      </section>

      {/* Footer */}
      <footer className="py-8 px-12 text-center border-t border-border">
        <p className="text-stone text-[13px]">Về chúng tôi · Chính sách · Liên hệ</p>
      </footer>
    </div>
  );
}
