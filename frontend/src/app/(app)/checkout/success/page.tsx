"use client";

import Link from "next/link";
import { useEffect } from "react";
import { useQueryClient } from "@tanstack/react-query";

export default function CheckoutSuccessPage() {
  const queryClient = useQueryClient();

  // Invalidate user cache so dashboard reflects new tier immediately
  useEffect(() => {
    queryClient.invalidateQueries({ queryKey: ["me"] });
  }, [queryClient]);

  return (
    <main className="min-h-screen bg-[#F7F3ED] flex items-center justify-center px-6">
      <div className="bg-[#FFFDF9] border border-[#6B8F71] rounded-2xl p-10 max-w-md w-full text-center shadow-sm">
        <div className="text-6xl mb-4">🎉</div>
        <h1
          className="text-2xl font-bold text-[#1C1917] mb-3"
          style={{ fontFamily: "var(--font-display)" }}
        >
          Chào mừng đến với PRO!
        </h1>
        <p className="text-[#78716C] mb-8">
          Tài khoản của bạn đã được nâng cấp. Toàn bộ 5 hệ thống và 10 chủ đề
          đã sẵn sàng cho bạn khám phá.
        </p>

        <div className="space-y-3">
          <Link
            href="/dashboard"
            className="block w-full py-3 bg-[#B8860B] text-white rounded-xl font-semibold hover:bg-[#D4A843] transition-colors"
          >
            Khám phá Dashboard →
          </Link>
          <Link
            href="/profile"
            className="block w-full py-3 border border-[#E7E0D6] text-[#78716C] rounded-xl text-sm hover:border-[#B8860B] transition-colors"
          >
            Xem hồ sơ tài khoản
          </Link>
        </div>
      </div>
    </main>
  );
}
