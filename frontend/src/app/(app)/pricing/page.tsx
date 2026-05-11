"use client";

import Link from "next/link";
import { useAuthStore } from "@/stores/auth.store";

export default function PricingPage() {
  const tier = useAuthStore((s) => s.user?.tier ?? "free");
  const isPro = tier === "pro";

  return (
    <div className="min-h-[calc(100vh-65px)] py-24 px-12">
      <div className="max-w-[960px] mx-auto">
        <div className="text-center mb-12">
          <h1 className="mb-3">Mở khóa toàn bộ hành trình của bạn</h1>
          <p className="text-stone text-lg">Một lần mua — trọn đời sử dụng</p>
        </div>

        <div className="flex gap-6 justify-center mb-12">
          {/* FREE */}
          <div className="flex-1 max-w-[380px] bg-warm-white border border-border rounded-xl shadow-sm p-6">
            <span className="inline-flex px-3 py-1 text-xs font-semibold rounded-full bg-sand text-charcoal border border-border mb-4">
              FREE
            </span>
            <div className="font-[family-name:var(--font-display)] text-[32px] font-bold mb-1">0₫</div>
            <p className="text-stone mb-6">Phù hợp với bạn muốn khám phá</p>
            <ul className="list-none flex flex-col gap-2 text-[15px] mb-6">
              <li>✓ 2 chủ đề luận giải</li>
              <li>✓ 2 hệ thống miễn phí</li>
              <li>✓ 1 hồ sơ</li>
              <li className="text-stone">✗ Biểu đồ hệ thống</li>
              <li className="text-stone">✗ Hỏi đáp</li>
              <li className="text-stone">✗ Export PDF</li>
            </ul>
            <div className="text-center text-stone text-sm py-3">
              {tier === "free" ? "Gói hiện tại ✓" : "—"}
            </div>
          </div>

          {/* PRO */}
          <div className="flex-1 max-w-[380px] bg-warm-white border-2 border-gold rounded-xl shadow-md p-6 relative">
            <div className="absolute -top-3 left-1/2 -translate-x-1/2 bg-gold text-white px-4 py-1 rounded-full text-xs font-semibold">
              Phổ biến nhất
            </div>
            <span className="inline-flex px-3 py-1 text-xs font-semibold rounded-full bg-gold-bg text-gold border border-gold mb-4">
              PRO
            </span>
            <div className="font-[family-name:var(--font-display)] text-[32px] font-bold mb-1">199.000₫</div>
            <p className="text-stone mb-6">Phù hợp với bạn muốn hiểu sâu bản thân</p>
            <ul className="list-none flex flex-col gap-2 text-[15px] mb-6">
              <li>✓ <strong>10 chủ đề</strong> luận giải</li>
              <li>✓ <strong>Cả 5 hệ thống</strong> biểu đồ</li>
              <li>✓ <strong>3 hồ sơ</strong></li>
              <li>✓ Hỏi đáp <strong>không giới hạn</strong></li>
              <li>✓ <strong>Export PDF</strong></li>
              <li>✓ <strong>Trọn đời</strong> sử dụng</li>
            </ul>
            {isPro ? (
              <div className="text-center py-3 rounded-md bg-sage-bg text-sage text-sm font-medium">
                Gói hiện tại ✓
              </div>
            ) : (
              <Link
                href="/checkout?tier=pro"
                className="block w-full text-center py-4 rounded-md bg-gold text-white font-medium text-base no-underline hover:bg-gold-soft transition-colors"
              >
                Nâng cấp PRO
              </Link>
            )}
          </div>
        </div>

        <div className="text-center">
          <p className="text-stone text-[13px] max-w-[480px] mx-auto">
            Mỗi gói áp dụng cho 1 hồ sơ. Thêm hồ sơ mới với cùng mức giá tại{" "}
            <Link href="/settings" className="text-gold no-underline hover:underline">Cài đặt</Link>.
          </p>
        </div>

        <div className="text-center mt-12">
          <Link href="/dashboard" className="inline-flex items-center px-4 py-2 text-sm border border-border rounded-md text-charcoal no-underline hover:bg-sand transition-colors">
            ← Quay lại Dashboard
          </Link>
        </div>
      </div>
    </div>
  );
}
