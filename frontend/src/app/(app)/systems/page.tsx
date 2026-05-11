"use client";

import { useQuery } from "@tanstack/react-query";
import Link from "next/link";
import { profilesApi } from "@/lib/profiles.api";
import { useAuthStore } from "@/stores/auth.store";

const SYSTEMS = [
  { key: "zi_wei", label: "Tử Vi", icon: "⬡", description: "Hệ thống hoàng gia cổ đại Trung Hoa" },
  { key: "bazi", label: "BaZi", icon: "○", description: "Tứ Trụ — Ngũ Hành tương sinh tương khắc" },
  { key: "human_design", label: "Human Design", icon: "◇", description: "Bản thiết kế năng lượng cá nhân" },
  { key: "numerology", label: "Số học", icon: "△", description: "Con số chủ đạo và chu kỳ cuộc đời" },
  { key: "vedic", label: "Vedic", icon: "☆", description: "Chiêm tinh Vệ Đà cổ đại Ấn Độ" },
];

const FREE_SYSTEMS = ["zi_wei", "numerology"];

export default function SystemsPage() {
  const { isAuthenticated } = useAuthStore();
  const tier = useAuthStore((s) => s.user?.tier ?? "free");
  const isPro = tier === "pro";

  const { data: profiles } = useQuery({
    queryKey: ["profiles"],
    queryFn: () => profilesApi.list().then((r) => r.data),
    enabled: isAuthenticated,
  });

  const profileId = profiles?.[0]?.id ?? "";

  return (
    <div style={{ padding: "32px 48px" }}>
      <h1 className="text-2xl font-semibold mb-2">Biểu đồ hệ thống</h1>
      <p className="text-stone mb-8">5 hệ thống phân tích bản mệnh từ nhiều góc nhìn</p>

      <div className="grid grid-cols-1 gap-4 max-w-[680px]">
        {SYSTEMS.map((sys) => {
          const isLocked = !isPro && !FREE_SYSTEMS.includes(sys.key);
          return (
            <Link
              key={sys.key}
              href={isLocked ? "/pricing" : `/system/${sys.key}?profile=${profileId}`}
              className={`flex items-center gap-4 p-5 bg-warm-white border rounded-xl no-underline transition-colors ${
                isLocked
                  ? "border-border opacity-60 hover:opacity-80"
                  : "border-border hover:border-gold"
              }`}
            >
              <span className="text-2xl w-10 text-center">{sys.icon}</span>
              <div className="flex-1">
                <div className="flex items-center gap-2">
                  <strong className="text-ink">{sys.label}</strong>
                  {isLocked && <span className="text-xs text-stone">🔒 PRO</span>}
                  {!isLocked && FREE_SYSTEMS.includes(sys.key) && !isPro && (
                    <span className="text-xs text-sage">FREE</span>
                  )}
                </div>
                <p className="text-stone text-sm mt-0.5">{sys.description}</p>
              </div>
              <span className="text-stone text-sm">→</span>
            </Link>
          );
        })}
      </div>
    </div>
  );
}
