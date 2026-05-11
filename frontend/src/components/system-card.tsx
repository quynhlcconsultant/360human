"use client";

import Link from "next/link";

interface SystemCardProps {
  framework: string;
  label: string;
  profileId: string;
  isLocked: boolean;
}

const SYSTEM_ICONS: Record<string, string> = {
  zi_wei:       "☯",
  bazi:         "🪬",
  human_design: "◉",
  vedic:        "🌙",
  numerology:   "∞",
};

export function SystemCard({ framework, label, profileId, isLocked }: SystemCardProps) {
  const href = isLocked
    ? "/pricing"
    : `/system/${framework}?profile=${profileId}`;

  return (
    <Link
      href={href}
      className={`flex items-center gap-3 p-4 rounded-xl border transition-all group ${
        isLocked
          ? "border-[#E7E0D6] bg-[#F7F3ED] opacity-60 cursor-pointer"
          : "border-[#E7E0D6] bg-[#FFFDF9] hover:border-[#B8860B] hover:shadow-sm"
      }`}
    >
      <span className="text-2xl">{SYSTEM_ICONS[framework] ?? "✦"}</span>
      <div className="flex-1 min-w-0">
        <p className="font-medium text-[#1C1917] truncate">{label}</p>
        <p className="text-xs text-[#78716C]">
          {isLocked ? "🔒 PRO" : "Xem luận giải →"}
        </p>
      </div>
    </Link>
  );
}
