"use client";

import Link from "next/link";

interface TopicCardProps {
  domain: string;
  label: string;
  profileId: string;
  isLocked: boolean;
}

const TOPIC_ICONS: Record<string, string> = {
  overview:      "🌐",
  love:          "♡",
  career:        "◈",
  health:        "◍",
  relationships: "◎",
  purpose:       "✦",
  strengths:     "◆",
  challenges:    "◇",
  timing:        "◷",
  spirituality:  "✧",
};

export function TopicCard({ domain, label, profileId, isLocked }: TopicCardProps) {
  const href = isLocked
    ? "/pricing"
    : `/topic/${domain}?profile=${profileId}`;

  return (
    <Link
      href={href}
      className={`flex flex-col items-center gap-2 p-4 rounded-xl border text-center transition-all ${
        isLocked
          ? "border-[#E7E0D6] bg-[#F7F3ED] opacity-60"
          : "border-[#E7E0D6] bg-[#FFFDF9] hover:border-[#B8860B] hover:shadow-sm"
      }`}
    >
      <span className="text-xl">{TOPIC_ICONS[domain] ?? "·"}</span>
      <p className="text-sm font-medium text-[#1C1917]">{label}</p>
      {isLocked && <p className="text-xs text-[#78716C]">🔒 PRO</p>}
    </Link>
  );
}
