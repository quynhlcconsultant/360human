"use client";

import { useQuery } from "@tanstack/react-query";
import Link from "next/link";
import { profilesApi } from "@/lib/profiles.api";
import { useAuthStore } from "@/stores/auth.store";

const TOPICS = [
  { key: "overview", label: "Tổng Quan Bản Mệnh", number: "01" },
  { key: "purpose", label: "Sứ Mệnh & Mục Đích", number: "02" },
  { key: "love", label: "Tình Yêu & Hôn Nhân", number: "03" },
  { key: "career", label: "Sự Nghiệp & Tài Chính", number: "04" },
  { key: "health", label: "Sức Khỏe & Năng Lượng", number: "05" },
  { key: "relationships", label: "Các Mối Quan Hệ", number: "06" },
  { key: "strengths", label: "Điểm Mạnh & Tài Năng", number: "07" },
  { key: "challenges", label: "Thách Thức & Bài Học", number: "08" },
  { key: "timing", label: "Vận Hạn & Thời Điểm", number: "09" },
  { key: "spirituality", label: "Tâm Linh & Phát Triển", number: "10" },
];

const FREE_TOPICS = ["overview", "purpose"];

export default function TopicsPage() {
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
      <h1 className="text-2xl font-semibold mb-2">Phân tích sâu</h1>
      <p className="text-stone mb-8">10 chủ đề luận giải tổng hợp từ 5 hệ thống</p>

      <div className="flex flex-col gap-3 max-w-[680px]">
        {TOPICS.map((topic) => {
          const isLocked = !isPro && !FREE_TOPICS.includes(topic.key);
          return (
            <Link
              key={topic.key}
              href={isLocked ? "/pricing" : `/topic/${topic.key}?profile=${profileId}`}
              className={`flex items-center gap-4 p-4 bg-warm-white border rounded-xl no-underline transition-colors ${
                isLocked
                  ? "border-border opacity-60 hover:opacity-80"
                  : "border-border hover:border-gold"
              }`}
            >
              <span className="text-[13px] font-mono text-stone w-8">{topic.number}</span>
              <div className="flex-1">
                <div className="flex items-center gap-2">
                  <strong className="text-ink">{topic.label}</strong>
                  {isLocked && <span className="text-xs text-stone">🔒 PRO</span>}
                </div>
              </div>
              <span className="text-stone text-sm">→</span>
            </Link>
          );
        })}
      </div>
    </div>
  );
}
