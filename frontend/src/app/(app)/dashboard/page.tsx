"use client";

import { Suspense, useEffect, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { useQuery } from "@tanstack/react-query";
import Link from "next/link";
import { authApi } from "@/lib/auth.api";
import { profilesApi, type Profile } from "@/lib/profiles.api";
import { useAuthStore } from "@/stores/auth.store";

const TOPICS = [
  { key: "overview", label: "1. Tổng quan bản thân", free: true },
  { key: "purpose", label: "2. Sứ mệnh & mục đích sống", free: true },
  { key: "love", label: "3. Tình cảm & các mối quan hệ", free: false },
  { key: "career", label: "4. Sự nghiệp & nghề nghiệp", free: false },
  { key: "health", label: "5. Tài chính & tiền bạc", free: false },
  { key: "relationships", label: "6. Sức khỏe & năng lượng", free: false },
  { key: "strengths", label: "7. Gia đình & nguồn gốc", free: false },
  { key: "challenges", label: "8. Điểm mạnh & tài năng", free: false },
  { key: "timing", label: "9. Thách thức & bóng tối", free: false },
  { key: "spirituality", label: "10. Thời điểm & chu kỳ", free: false },
];

const SYSTEMS = [
  { key: "zi_wei", icon: "⬡", label: "Tử Vi", free: true },
  { key: "numerology", icon: "○", label: "Số học", free: true },
  { key: "bazi", icon: "◇", label: "BaZi", free: false },
  { key: "human_design", icon: "△", label: "Human Design", free: false },
  { key: "vedic", icon: "☆", label: "Vedic", free: false },
];

export default function DashboardPage() {
  return (
    <Suspense fallback={<div className="p-12 text-stone">Đang tải...</div>}>
      <DashboardContent />
    </Suspense>
  );
}

function DashboardContent() {
  const router = useRouter();
  const params = useSearchParams();
  const profileIdParam = params.get("profile");
  const [openTopic, setOpenTopic] = useState<string | null>("overview");

  const { setUser, logout, isAuthenticated } = useAuthStore();

  const { data: user, isError: userError } = useQuery({
    queryKey: ["me"],
    queryFn: () => authApi.me().then((r) => r.data),
    enabled: isAuthenticated,
  });

  const { data: profiles } = useQuery({
    queryKey: ["profiles"],
    queryFn: () => profilesApi.list().then((r) => r.data),
    enabled: isAuthenticated,
  });

  useEffect(() => { if (user) setUser(user); }, [user, setUser]);
  useEffect(() => {
    if (userError) { logout(); router.push("/login"); }
  }, [userError, logout, router]);

  const activeProfile: Profile | undefined =
    profiles?.find((p) => p.id === profileIdParam) ?? profiles?.[0];

  const tier = user?.tier ?? "free";
  const isPro = tier === "pro";
  const freeTopicCount = TOPICS.filter((t) => t.free).length;
  const totalTopics = TOPICS.length;

  if (profiles !== undefined && profiles.length === 0) {
    router.push("/onboarding");
    return null;
  }

  return (
    <div>
      {/* Progress Bar */}
      <div className="px-12 py-3 bg-sand flex items-center gap-4">
        <div className="flex-1 h-1 bg-border rounded-sm overflow-hidden">
          <div
            className="h-full bg-gold rounded-sm transition-all"
            style={{ width: `${isPro ? 100 : (freeTopicCount / totalTopics) * 100}%` }}
          />
        </div>
        <span className="text-[13px] text-stone whitespace-nowrap">
          {isPro ? totalTopics : freeTopicCount}/{totalTopics} chủ đề
          {!isPro && (
            <> — <Link href="/pricing" className="text-gold no-underline hover:underline">Mở khóa thêm {totalTopics - freeTopicCount} với PRO</Link></>
          )}
        </span>
      </div>

      {/* 2-Column Layout */}
      <div className="flex">
        {/* LEFT: Topics (2/3) */}
        <div className="flex-[2] p-8 pl-12 border-r border-border">
          <h2 className="mb-6">Luận giải theo chủ đề</h2>

          {/* Accordion Topics */}
          <div className="flex flex-col gap-2">
            {TOPICS.map((topic) => {
              const isLocked = !isPro && !topic.free;
              const isOpen = openTopic === topic.key && !isLocked;

              return (
                <div key={topic.key} className={`border border-border rounded-xl bg-warm-white overflow-hidden ${isLocked ? "opacity-50" : ""}`}>
                  <div
                    className={`px-6 py-4 flex justify-between items-center font-[family-name:var(--font-display)] text-lg font-medium ${
                      isLocked ? "cursor-default" : "cursor-pointer hover:bg-sand"
                    }`}
                    onClick={() => !isLocked && setOpenTopic(isOpen ? null : topic.key)}
                  >
                    <span>
                      {topic.label}
                      {isLocked && " \uD83D\uDD12"}
                    </span>
                    {isLocked ? (
                      <span className="inline-flex px-3 py-0.5 text-[11px] font-semibold rounded-full bg-gold-bg text-gold border border-gold">PRO</span>
                    ) : (
                      <span className={`text-sm text-stone transition-transform ${isOpen ? "rotate-180" : ""}`}>&#x25BE;</span>
                    )}
                  </div>
                  {isOpen && (
                    <div className="px-6 pb-6">
                      <TopicContent
                        topicKey={topic.key}
                        profileId={activeProfile?.id ?? ""}
                      />
                    </div>
                  )}
                </div>
              );
            })}
          </div>

          {/* Q&A */}
          <div className="mt-8 pt-6 border-t border-border">
            <h3 className="mb-4">Hỏi đáp</h3>
            <div className="flex gap-2">
              <input
                type="text"
                placeholder="Hỏi về luận giải của bạn..."
                className="flex-1 px-4 py-3 text-[15px] border border-border rounded-md bg-warm-white text-ink outline-none opacity-40"
                disabled={!isPro}
              />
              <button
                className="px-4 py-3 text-sm bg-gold text-white rounded-md opacity-40 cursor-not-allowed"
                disabled
              >
                Gửi
              </button>
            </div>
            {!isPro && (
              <p className="text-stone text-[13px] mt-2">
                <Link href="/pricing" className="text-gold no-underline hover:underline">Nâng cấp PRO</Link> để sử dụng tính năng hỏi đáp
              </p>
            )}
          </div>
        </div>

        {/* RIGHT: Systems (1/3) */}
        <div className="flex-1 p-8 pr-12">
          <h3 className="mb-4">Biểu đồ hệ thống</h3>
          <p className="text-stone text-[13px] mb-6">Charts = WHY — dữ liệu đằng sau luận giải</p>

          <div className="flex flex-col gap-2">
            {SYSTEMS.map((sys) => {
              const isLocked = !isPro && !sys.free;
              return (
                <Link
                  key={sys.key}
                  href={isLocked ? "/pricing" : `/system/${sys.key}?profile=${activeProfile?.id ?? ""}`}
                  className={`flex items-center gap-2 p-4 bg-warm-white border border-border rounded-xl no-underline text-ink ${
                    isLocked ? "opacity-50" : "hover:border-gold hover:shadow-sm"
                  } transition-all`}
                >
                  <span>{sys.icon}</span>
                  <span className="text-[15px]">{sys.label}</span>
                  {isLocked && (
                    <span className="ml-auto inline-flex px-2 py-0.5 text-[10px] font-semibold rounded-full bg-gold-bg text-gold border border-gold">PRO</span>
                  )}
                </Link>
              );
            })}
          </div>

          <Link
            href="/pricing"
            className="block w-full mt-6 py-3 text-center bg-gold text-white rounded-md font-medium no-underline hover:bg-gold-soft transition-colors"
          >
            {isPro ? "Đã mở khóa" : "Mở khóa biểu đồ"}
          </Link>

          <div className="mt-8 pt-6 border-t border-border">
            <Link
              href={`/system/zi_wei?profile=${activeProfile?.id ?? ""}`}
              className="block w-full py-2 text-center text-sm border border-border rounded-md text-stone no-underline hover:bg-sand transition-colors"
            >
              Xem luận giải chi tiết theo hệ thống →
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

/* Inline topic content with lazy loading */
function TopicContent({ topicKey, profileId }: { topicKey: string; profileId: string }) {
  const { data, isLoading, isError } = useQuery({
    queryKey: ["topic", topicKey, profileId],
    queryFn: () =>
      import("@/lib/profiles.api").then((m) =>
        m.interpretApi.topic(topicKey, profileId).then((r) => r.data)
      ),
    enabled: !!profileId,
    staleTime: 5 * 60 * 1000,
  });

  if (isLoading) {
    return (
      <div className="space-y-3">
        {[...Array(4)].map((_, i) => (
          <div key={i} className="h-4 bg-sand rounded animate-pulse" style={{ width: `${85 - i * 10}%` }} />
        ))}
      </div>
    );
  }

  if (isError || !data?.interpretation) {
    return <p className="text-ember text-sm">Không thể tải nội dung. Vui lòng thử lại.</p>;
  }

  return (
    <div className="font-[family-name:var(--font-reading)] text-lg leading-relaxed max-w-[680px]">
      {data.interpretation.split("\n\n").map((paragraph: string, i: number) => (
        <p key={i} className="mb-4">{paragraph}</p>
      ))}
      <div className="font-[family-name:var(--font-mono)] text-[13px] text-stone opacity-80 mt-4">
        {data.word_count} từ · nguồn: tổng hợp 5 hệ thống
      </div>
    </div>
  );
}
