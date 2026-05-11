"use client";

import { Suspense, useState } from "react";
import { useSearchParams } from "next/navigation";
import { useAuthStore } from "@/stores/auth.store";
import Link from "next/link";

const DAYS = ["T2", "T3", "T4", "T5", "T6", "T7", "CN"];

function getCalendarDays(year: number, month: number) {
  const firstDay = new Date(year, month, 1).getDay();
  const daysInMonth = new Date(year, month + 1, 0).getDate();
  const startOffset = firstDay === 0 ? 6 : firstDay - 1;
  const weeks: (number | null)[][] = [];
  let currentWeek: (number | null)[] = Array(startOffset).fill(null);
  for (let d = 1; d <= daysInMonth; d++) {
    currentWeek.push(d);
    if (currentWeek.length === 7) {
      weeks.push(currentWeek);
      currentWeek = [];
    }
  }
  if (currentWeek.length > 0) {
    while (currentWeek.length < 7) currentWeek.push(null);
    weeks.push(currentWeek);
  }
  return weeks;
}

const MONTH_NAMES = [
  "Tháng 1", "Tháng 2", "Tháng 3", "Tháng 4", "Tháng 5", "Tháng 6",
  "Tháng 7", "Tháng 8", "Tháng 9", "Tháng 10", "Tháng 11", "Tháng 12",
];

export default function TimeOraclePage() {
  return (
    <Suspense fallback={<div className="p-12 text-stone">Đang tải...</div>}>
      <TimeOracleContent />
    </Suspense>
  );
}

function TimeOracleContent() {
  const searchParams = useSearchParams();
  const profileId = searchParams.get("profile") ?? "";
  const tier = useAuthStore((s) => s.user?.tier ?? "free");
  const isPro = tier === "pro";

  const today = new Date();
  const [year, setYear] = useState(today.getFullYear());
  const [month, setMonth] = useState(today.getMonth());
  const [selectedWeek, setSelectedWeek] = useState<number | null>(null);

  const weeks = getCalendarDays(year, month);
  const todayDate = today.getDate();
  const isCurrentMonth = year === today.getFullYear() && month === today.getMonth();

  const prevMonth = () => {
    if (month === 0) { setYear(year - 1); setMonth(11); }
    else setMonth(month - 1);
    setSelectedWeek(null);
  };
  const nextMonth = () => {
    if (month === 11) { setYear(year + 1); setMonth(0); }
    else setMonth(month + 1);
    setSelectedWeek(null);
  };

  return (
    <div style={{ padding: "32px 48px" }}>
      {/* Breadcrumb layers */}
      <div className="text-sm mb-6 flex items-center gap-2">
        <span className={isPro ? "cursor-pointer text-gold font-medium" : "opacity-50 cursor-not-allowed text-stone"}>
          Cuộc đời {!isPro && "🔒"}
        </span>
        <span className="text-border">›</span>
        <span className={isPro ? "cursor-pointer text-gold font-medium" : "opacity-50 cursor-not-allowed text-stone"}>
          {year} {!isPro && "🔒"}
        </span>
        <span className="text-border">›</span>
        <span className="font-semibold text-ink">{MONTH_NAMES[month]}</span>
      </div>

      {/* Upsell banner for FREE */}
      {!isPro && (
        <div className="bg-gold-bg border border-gold rounded-lg p-4 px-6 mb-8 flex justify-between items-center">
          <span className="text-[15px]">Mở khóa Lifetime & Yearly với PRO</span>
          <Link
            href="/pricing"
            className="px-4 py-2 bg-gold text-white rounded-md text-sm font-medium no-underline hover:bg-gold-soft transition-colors"
          >
            Nâng cấp
          </Link>
        </div>
      )}

      {/* 2-column: Summary + Calendar */}
      <div className="flex gap-8">
        {/* Left: Monthly summary */}
        <div className="flex-1">
          <div className="flex items-center gap-4 mb-4">
            <button onClick={prevMonth} className="text-stone hover:text-charcoal cursor-pointer bg-transparent border-none text-base">
              ← {month === 0 ? "T12" : `T${month}`}
            </button>
            <h2 className="text-xl font-semibold">{MONTH_NAMES[month]}, {year}</h2>
            <button onClick={nextMonth} className="text-stone hover:text-charcoal cursor-pointer bg-transparent border-none text-base">
              {month === 11 ? "T1" : `T${month + 2}`} →
            </button>
          </div>

          <div className="bg-warm-white border border-border rounded-xl p-5">
            <h3 className="font-[family-name:var(--font-display)] mb-3">Tháng của sự tập trung nội tâm</h3>
            <div className="flex flex-col gap-2">
              <div className="flex justify-between">
                <span className="text-stone">Năng lượng</span>
                <span>●●●○○</span>
              </div>
              <div className="flex justify-between">
                <span className="text-stone">Trọng tâm</span>
                <span>Sự nghiệp</span>
              </div>
              <div className="flex justify-between">
                <span className="text-stone">Lưu ý</span>
                <span className="text-[#D44]">Tuần 3</span>
              </div>
            </div>
          </div>
        </div>

        {/* Right: Calendar */}
        <div style={{ flex: 1.5 }}>
          <table className="w-full border-collapse text-center">
            <thead>
              <tr className="text-stone text-[13px]">
                {DAYS.map((d) => (
                  <td key={d} className="py-2 px-2">{d}</td>
                ))}
              </tr>
            </thead>
            <tbody>
              {weeks.map((week, wi) => {
                const isWarningWeek = wi === 2;
                const isFirstWeek = wi === 0;
                return (
                  <tr
                    key={wi}
                    className={`cursor-pointer transition-colors ${
                      selectedWeek === wi
                        ? "bg-gold-bg"
                        : isWarningWeek
                          ? "bg-[#FFF0F0]"
                          : isFirstWeek
                            ? "bg-gold-bg"
                            : "hover:bg-sand"
                    }`}
                    onClick={() => setSelectedWeek(wi)}
                  >
                    {week.map((day, di) => (
                      <td
                        key={di}
                        className={`py-3 px-2 ${
                          day && isCurrentMonth && day === todayDate
                            ? "font-semibold text-gold"
                            : ""
                        }`}
                      >
                        {day ?? ""}
                      </td>
                    ))}
                  </tr>
                );
              })}
            </tbody>
          </table>

          {/* Weekly panel */}
          <div className="bg-warm-white border border-border rounded-xl p-4 mt-4">
            <div className="text-[13px] text-stone mb-2">
              {selectedWeek !== null && weeks[selectedWeek]
                ? (() => {
                    const w = weeks[selectedWeek];
                    const first = w.find((d) => d !== null);
                    const last = [...w].reverse().find((d) => d !== null);
                    return `Tuần ${String(first).padStart(2, "0")}/${String(month + 1).padStart(2, "0")} — ${String(last).padStart(2, "0")}/${String(month + 1).padStart(2, "0")}/${year}`;
                  })()
                : `Chọn một tuần để xem chi tiết`}
            </div>
            <p className="text-[15px] mb-2">
              Tuần cần <strong className="text-[#D44]">cẩn trọng</strong> trong giao tiếp. Năng lượng hướng nội — tốt cho suy ngẫm, không tốt cho quyết định lớn.
            </p>
            <div className="flex gap-1.5">
              <span className="inline-flex px-2 py-0.5 text-xs rounded bg-sand text-stone border border-border">Nội tâm</span>
              <span className="inline-flex px-2 py-0.5 text-xs rounded bg-sand text-stone border border-border">Giao tiếp</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
