"use client";

import { useRouter } from "next/navigation";

interface TierGateProps {
  children: React.ReactNode;
  isLocked: boolean;
  message?: string;
}

export function TierGate({ children, isLocked, message }: TierGateProps) {
  const router = useRouter();

  if (!isLocked) return <>{children}</>;

  return (
    <div className="relative">
      {/* Blurred preview */}
      <div className="select-none pointer-events-none" style={{ filter: "blur(6px)", opacity: 0.4 }}>
        {children}
      </div>

      {/* Overlay CTA */}
      <div className="absolute inset-0 flex flex-col items-center justify-center bg-gradient-to-t from-[#F7F3ED] via-[#F7F3ED]/80 to-transparent rounded-xl p-6 text-center">
        <div className="text-2xl mb-3">🔒</div>
        <p className="font-semibold text-[#1C1917] mb-1">{message ?? "Nội dung PRO"}</p>
        <p className="text-sm text-[#78716C] mb-4">Nâng cấp để đọc phân tích đầy đủ</p>
        <button
          onClick={() => router.push("/pricing")}
          className="px-6 py-2.5 bg-[#B8860B] text-white rounded-lg font-medium hover:bg-[#D4A843] transition-colors"
        >
          Nâng cấp PRO — 199.000₫
        </button>
      </div>
    </div>
  );
}
