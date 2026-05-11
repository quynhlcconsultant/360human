"use client";

import { use } from "react";
import { useSearchParams } from "next/navigation";
import { useQuery } from "@tanstack/react-query";
import Link from "next/link";
import { interpretApi } from "@/lib/profiles.api";
import { useAuthStore } from "@/stores/auth.store";

const SYSTEMS = [
  { key: "zi_wei", label: "Tử Vi" },
  { key: "bazi", label: "BaZi" },
  { key: "human_design", label: "Human Design" },
  { key: "numerology", label: "Số học" },
  { key: "vedic", label: "Vedic" },
];

const FREE_SYSTEMS = ["zi_wei", "numerology"];

export default function SystemReadingPage({
  params,
}: {
  params: Promise<{ framework: string }>;
}) {
  const { framework } = use(params);
  const searchParams = useSearchParams();
  const profileId = searchParams.get("profile") ?? "";
  const { isAuthenticated } = useAuthStore();
  const tier = useAuthStore((s) => s.user?.tier ?? "free");
  const isPro = tier === "pro";

  const isLocked = !isPro && !FREE_SYSTEMS.includes(framework);

  const { data, isLoading, isError } = useQuery({
    queryKey: ["system", framework, profileId],
    queryFn: () => interpretApi.system(framework, profileId).then((r) => r.data),
    enabled: isAuthenticated && !!profileId && !isLocked,
    staleTime: 1000 * 60 * 30,
  });

  const currentSystem = SYSTEMS.find((s) => s.key === framework);

  return (
    <div>
      {/* Breadcrumb topbar */}
      <div className="px-12 py-3 border-b border-border flex items-center justify-between bg-warm-white">
        <div className="flex items-center gap-2 text-sm">
          <Link href="/dashboard" className="text-stone no-underline hover:text-charcoal">← Dashboard</Link>
          <span className="text-border">›</span>
          <span className="font-medium text-ink">{currentSystem?.label ?? framework}</span>
        </div>
        {isPro && (
          <span className="inline-flex px-3 py-0.5 text-xs font-semibold rounded-full bg-gold-bg text-gold border border-gold">PRO</span>
        )}
      </div>

      {/* System tabs */}
      <div className="flex border-b border-border px-12">
        {SYSTEMS.map((sys) => {
          const sysLocked = !isPro && !FREE_SYSTEMS.includes(sys.key);
          return (
            <Link
              key={sys.key}
              href={sysLocked ? "/pricing" : `/system/${sys.key}?profile=${profileId}`}
              className={`px-6 py-3 text-[15px] font-medium border-b-2 no-underline transition-colors ${
                sys.key === framework
                  ? "text-gold border-gold"
                  : sysLocked
                    ? "text-stone/50 border-transparent cursor-default"
                    : "text-stone border-transparent hover:text-charcoal"
              }`}
            >
              {sys.label} {sysLocked && "\uD83D\uDD12"}
            </Link>
          );
        })}
      </div>

      {/* Content */}
      <div className="p-8 px-12">
        {isLocked ? (
          <div className="text-center py-16">
            <div className="text-5xl mb-4 opacity-50">\uD83D\uDD12</div>
            <h3 className="mb-2">{currentSystem?.label} chỉ dành cho PRO</h3>
            <p className="text-stone mb-6">Nâng cấp để mở khóa toàn bộ 5 hệ thống</p>
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
              <div className="max-w-[680px] space-y-4">
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
              <div className="max-w-[680px]">
                <div className="font-[family-name:var(--font-reading)] text-lg leading-relaxed">
                  {data.interpretation.split("\n\n").map((para: string, i: number) => (
                    <p key={i} className="mb-4">{para}</p>
                  ))}
                </div>
                <div className="font-[family-name:var(--font-mono)] text-[13px] text-stone opacity-80 mt-6 pt-4 border-t border-border">
                  {data.word_count} từ · nguồn: {currentSystem?.label}
                </div>
              </div>
            )}
          </>
        )}
      </div>
    </div>
  );
}
