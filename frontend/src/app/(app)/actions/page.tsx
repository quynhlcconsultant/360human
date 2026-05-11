"use client";

import { useState } from "react";
import { useAuthStore } from "@/stores/auth.store";
import Link from "next/link";

interface ActionItem {
  id: number;
  title: string;
  description: string;
  system: string;
  layer: "foundation" | "nurture" | "unlock";
}

const ACTIONS: ActionItem[] = [
  {
    id: 1,
    title: "Dành 10 phút mỗi sáng viết nhật ký",
    description: "Quan sát mâu thuẫn nội tại — viết ra, không phán xét",
    system: "BaZi",
    layer: "foundation",
  },
  {
    id: 2,
    title: "Nói \"không\" ít nhất 1 lần/tuần",
    description: "Tham Lang dễ thu hút — nhưng cần chọn lọc",
    system: "Tử Vi",
    layer: "foundation",
  },
  {
    id: 3,
    title: "Thực hành thiền định 15 phút mỗi tối",
    description: "Kết nối với bản thể sâu bên trong, lắng nghe trực giác",
    system: "Human Design",
    layer: "nurture",
  },
  {
    id: 4,
    title: "Đặt mục tiêu nhỏ mỗi tuần và review",
    description: "Xây dựng kỷ luật bản thân qua từng bước nhỏ",
    system: "Số học",
    layer: "nurture",
  },
  {
    id: 5,
    title: "Chia sẻ insight cá nhân 1 lần/tháng",
    description: "Biến hiểu biết thành hành động tạo giá trị cho cộng đồng",
    system: "Vedic",
    layer: "unlock",
  },
];

export default function ActionsPage() {
  const tier = useAuthStore((s) => s.user?.tier ?? "free");
  const isPro = tier === "pro";

  const [selectedAction, setSelectedAction] = useState<number>(1);
  const [checked, setChecked] = useState<Set<number>>(new Set());

  const foundationActions = ACTIONS.filter((a) => a.layer === "foundation");
  const nurtureActions = ACTIONS.filter((a) => a.layer === "nurture");
  const unlockActions = ACTIONS.filter((a) => a.layer === "unlock");

  const toggleCheck = (id: number) => {
    setChecked((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  const completedFoundation = foundationActions.filter((a) => checked.has(a.id)).length;
  const progressPercent = (completedFoundation / foundationActions.length) * 100;

  const active = ACTIONS.find((a) => a.id === selectedAction);

  return (
    <div className="flex" style={{ minHeight: "calc(100vh - 65px)" }}>
      {/* LEFT: Pyramid + Actions */}
      <div className="flex-1 border-r border-border" style={{ padding: "32px 32px 32px 48px" }}>
        {/* Pyramid SVG */}
        <div className="text-center mb-8">
          <svg viewBox="0 0 300 200" style={{ width: 280 }}>
            <polygon
              points="150,20 260,180 40,180"
              fill="none"
              stroke="#E0E0E0"
              strokeWidth="2"
            />
            <line x1="90" y1="120" x2="210" y2="120" stroke="#E0E0E0" strokeWidth="1" />
            <line
              x1="115" y1="70" x2="185" y2="70"
              stroke="#E0E0E0" strokeWidth="1"
              strokeDasharray="3,3"
            />
            {/* Labels */}
            <text x="150" y="55" textAnchor="middle" style={{ fontSize: 11, fill: "#888", opacity: isPro ? 1 : 0.4 }}>
              {isPro ? "Khai Phóng" : "Khai Phóng 🔒"}
            </text>
            <text x="150" y="105" textAnchor="middle" style={{ fontSize: 11, fill: "#888", opacity: isPro ? 1 : 0.4 }}>
              {isPro ? "Nuôi Dưỡng" : "Nuôi Dưỡng 🔒"}
            </text>
            <text x="150" y="165" textAnchor="middle" style={{ fontSize: 12, fill: "#B8860B", fontWeight: 600 }}>
              Nền Móng
            </text>
            {/* Highlight base */}
            <polygon
              points="40,180 260,180 210,120 90,120"
              fill="#F5ECD4"
              fillOpacity="0.5"
              stroke="#B8860B"
              strokeWidth="2"
            />
          </svg>
        </div>

        {/* Foundation actions */}
        <h3 className="mb-1">Nền Móng — {foundationActions.length} hành động</h3>
        <div className="h-1 bg-sand rounded-sm overflow-hidden mb-6" style={{ width: 120 }}>
          <div className="h-full bg-gold rounded-sm transition-all duration-300" style={{ width: `${progressPercent}%` }} />
        </div>

        <div className="flex flex-col gap-3">
          {foundationActions.map((action) => (
            <div
              key={action.id}
              onClick={() => setSelectedAction(action.id)}
              className={`bg-warm-white border rounded-xl p-4 cursor-pointer transition-colors ${
                selectedAction === action.id ? "border-gold border-2" : "border-border hover:border-gold/50"
              }`}
            >
              <div className="flex items-start gap-3">
                <input
                  type="checkbox"
                  checked={checked.has(action.id)}
                  onChange={() => toggleCheck(action.id)}
                  className="w-auto mt-1"
                  onClick={(e) => e.stopPropagation()}
                />
                <div className="flex-1">
                  <strong>{action.id}. {action.title}</strong>
                  <p className="text-stone text-[13px] mt-1">{action.description}</p>
                </div>
                <span className="inline-flex px-2 py-0.5 text-xs rounded bg-sand text-stone border border-border">
                  {action.system}
                </span>
              </div>
            </div>
          ))}
        </div>

        {/* Locked layers */}
        {!isPro && (
          <div className="mt-6 p-4 bg-sand rounded-lg text-center">
            <p className="text-stone text-sm">
              Mở khóa Nuôi Dưỡng & Khai Phóng với{" "}
              <Link href="/pricing" className="text-gold no-underline hover:underline font-medium">PRO</Link>
            </p>
          </div>
        )}

        {/* PRO: Show nurture & unlock layers */}
        {isPro && (
          <>
            <h3 className="mt-8 mb-1">Nuôi Dưỡng — {nurtureActions.length} hành động</h3>
            <div className="flex flex-col gap-3 mt-4">
              {nurtureActions.map((action) => (
                <div
                  key={action.id}
                  onClick={() => setSelectedAction(action.id)}
                  className={`bg-warm-white border rounded-xl p-4 cursor-pointer transition-colors ${
                    selectedAction === action.id ? "border-gold border-2" : "border-border hover:border-gold/50"
                  }`}
                >
                  <div className="flex items-start gap-3">
                    <input
                      type="checkbox"
                      checked={checked.has(action.id)}
                      onChange={() => toggleCheck(action.id)}
                      className="w-auto mt-1"
                      onClick={(e) => e.stopPropagation()}
                    />
                    <div className="flex-1">
                      <strong>{action.id}. {action.title}</strong>
                      <p className="text-stone text-[13px] mt-1">{action.description}</p>
                    </div>
                    <span className="inline-flex px-2 py-0.5 text-xs rounded bg-sand text-stone border border-border">
                      {action.system}
                    </span>
                  </div>
                </div>
              ))}
            </div>

            <h3 className="mt-8 mb-1">Khai Phóng — {unlockActions.length} hành động</h3>
            <div className="flex flex-col gap-3 mt-4">
              {unlockActions.map((action) => (
                <div
                  key={action.id}
                  onClick={() => setSelectedAction(action.id)}
                  className={`bg-warm-white border rounded-xl p-4 cursor-pointer transition-colors ${
                    selectedAction === action.id ? "border-gold border-2" : "border-border hover:border-gold/50"
                  }`}
                >
                  <div className="flex items-start gap-3">
                    <input
                      type="checkbox"
                      checked={checked.has(action.id)}
                      onChange={() => toggleCheck(action.id)}
                      className="w-auto mt-1"
                      onClick={(e) => e.stopPropagation()}
                    />
                    <div className="flex-1">
                      <strong>{action.id}. {action.title}</strong>
                      <p className="text-stone text-[13px] mt-1">{action.description}</p>
                    </div>
                    <span className="inline-flex px-2 py-0.5 text-xs rounded bg-sand text-stone border border-border">
                      {action.system}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </>
        )}
      </div>

      {/* RIGHT: WHAT & WHY panels */}
      <div className="flex-1" style={{ padding: "32px 48px 32px 32px" }}>
        {active ? (
          <>
            <div className="bg-warm-white border border-border rounded-xl p-5 mb-4">
              <h4 className="mb-3 text-stone">WHAT — Xuất phát từ đặc điểm nào?</h4>
              <p className="text-[15px] leading-relaxed">
                Bạn có <strong>Canh Kim Nhật Chủ</strong> trong lửa đôi Ngọ — bản chất cứng rắn nhưng môi trường đòi hỏi linh hoạt.
                Viết nhật ký giúp bạn quan sát sự mâu thuẫn này thay vì bị nó điều khiển.
              </p>
            </div>
            <div className="bg-warm-white border border-border rounded-xl p-5">
              <h4 className="mb-3 text-stone">WHY — Từ hệ thống nào?</h4>
              <div className="flex items-center gap-2 mb-3">
                <span className="inline-flex px-2 py-0.5 text-xs rounded bg-sand text-stone border border-border">
                  {active.system}
                </span>
                <span className="text-[15px] font-medium">Tứ Trụ — Nhật Chủ</span>
              </div>
              <p className="text-[15px] leading-relaxed">
                Canh Kim là kim loại cứng — thanh kiếm, búa rìu. Ngọ là lửa mạnh. Kim gặp lửa = bị tôi luyện.
                Nhật ký là cách bạn tự tôi luyện có ý thức thay vì bị hoàn cảnh ép.
              </p>
              {!isPro && (
                <span className="inline-block mt-3 text-[13px] text-gold opacity-50">
                  Xem chi tiết trong biểu đồ → (PRO)
                </span>
              )}
              {isPro && (
                <Link
                  href={`/system/bazi?profile=`}
                  className="inline-block mt-3 text-[13px] text-gold no-underline hover:underline"
                >
                  Xem chi tiết trong biểu đồ →
                </Link>
              )}
            </div>
          </>
        ) : (
          <div className="text-center py-16 text-stone">
            Chọn một hành động để xem chi tiết
          </div>
        )}
      </div>
    </div>
  );
}
