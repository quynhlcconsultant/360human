"use client";

import { use } from "react";
import { useSearchParams } from "next/navigation";
import { useQuery } from "@tanstack/react-query";
import Link from "next/link";
import { interpretApi } from "@/lib/profiles.api";
import { useAuthStore } from "@/stores/auth.store";

const TOPIC_LABELS: Record<string, string> = {
  overview: "Tổng Quan Bản Mệnh",
  love: "Tình Yêu & Hôn Nhân",
  career: "Sự Nghiệp & Tài Chính",
  health: "Sức Khỏe & Năng Lượng",
  relationships: "Các Mối Quan Hệ",
  purpose: "Sứ Mệnh & Mục Đích",
  strengths: "Điểm Mạnh & Tài Năng",
  challenges: "Thách Thức & Bài Học",
  timing: "Vận Hạn & Thời Điểm",
  spirituality: "Tâm Linh & Phát Triển",
};

const FREE_TOPICS = ["overview", "purpose"];

export default function TopicReadingPage({
  params,
}: {
  params: Promise<{ domain: string }>;
}) {
  const { domain } = use(params);
  const searchParams = useSearchParams();
  const profileId = searchParams.get("profile") ?? "";
  const { isAuthenticated } = useAuthStore();
  const tier = useAuthStore((s) => s.user?.tier ?? "free");
  const isPro = tier === "pro";

  const isLocked = !isPro && !FREE_TOPICS.includes(domain);

  const { data, isLoading, isError } = useQuery({
    queryKey: ["topic", domain, profileId],
    queryFn: () => interpretApi.topic(domain, profileId).then((r) => r.data),
    enabled: isAuthenticated && !!profileId && !isLocked,
    staleTime: 1000 * 60 * 30,
  });

  return (
    <div>
      <div className="px-12 py-3 border-b border-border bg-warm-white flex items-center gap-2 text-sm">
        <Link href="/dashboard" className="text-stone no-underline hover:text-charcoal">← Dashboard</Link>
        <span className="text-border">›</span>
        <span className="font-medium text-ink">{TOPIC_LABELS[domain] ?? domain}</span>
      </div>

      <div className="p-8 px-12 max-w-[680px]">
        {isLocked ? (
          <div className="text-center py-16">
            <div className="text-5xl mb-4 opacity-50">{"\uD83D\uDD12"}</div>
            <h3 className="mb-2">{TOPIC_LABELS[domain]} chỉ dành cho PRO</h3>
            <p className="text-stone mb-6">Nâng cấp để mở khóa toàn bộ 10 chủ đề</p>
            <Link
              href="/pricing"
              className="inline-flex px-6 py-3 bg-gold text-white rounded-md font-medium no-underline hover:bg-gold-soft transition-colors"
            >
              Nâng cấp PRO
            </Link>
          </div>
        ) : (
          <>
            {isLoading && (
              <div className="space-y-4">
                {[...Array(6)].map((_, i) => (
                  <div key={i} className="h-4 bg-sand rounded animate-pulse" style={{ width: `${85 - i * 8}%` }} />
                ))}
              </div>
            )}

            {isError && (
              <div className="bg-ember-bg border border-ember rounded-xl p-4 text-ember">
                Không thể tải nội dung. Vui lòng thử lại.
              </div>
            )}

            {data && (
              <article>
                <div className="font-[family-name:var(--font-reading)] text-lg leading-relaxed">
                  {data.interpretation.split("\n\n").map((para: string, i: number) => (
                    <p key={i} className="mb-4">{para}</p>
                  ))}
                </div>
                <div className="font-[family-name:var(--font-mono)] text-[13px] text-stone opacity-80 mt-6 pt-4 border-t border-border">
                  {data.word_count} từ · Tổng hợp từ 5 hệ thống
                </div>
              </article>
            )}
          </>
        )}
      </div>
    </div>
  );
}
