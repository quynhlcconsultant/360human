"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { profilesApi, type ProfileCreate } from "@/lib/profiles.api";

const STEPS = ["Họ tên", "Ngày sinh", "Giờ sinh", "Nơi sinh", "Xác nhận"];

const GENDERS = [
  { value: "male", label: "Nam" },
  { value: "female", label: "Nữ" },
  { value: "other", label: "Khác" },
];

export default function OnboardingPage() {
  const router = useRouter();
  const [step, setStep] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const [form, setForm] = useState<ProfileCreate>({
    full_name: "",
    birth_date: "",
    birth_time: "",
    birth_city: "",
    birth_lat: "",
    birth_lon: "",
    birth_timezone: "Asia/Ho_Chi_Minh",
    gender: "male",
  });

  function set(field: keyof ProfileCreate, value: string) {
    setForm((prev) => ({ ...prev, [field]: value }));
  }

  function canNext(): boolean {
    if (step === 0) return form.full_name.trim().length > 1;
    if (step === 1) return form.birth_date.length === 10;
    return true;
  }

  async function handleSubmit() {
    setLoading(true);
    setError("");
    try {
      const payload: ProfileCreate = {
        ...form,
        birth_time: form.birth_time || undefined,
        birth_city: form.birth_city || undefined,
        birth_lat: form.birth_lat || undefined,
        birth_lon: form.birth_lon || undefined,
      };
      const { data } = await profilesApi.create(payload);
      router.push(`/dashboard?profile=${data.id}`);
    } catch (err: unknown) {
      const msg = (err as { response?: { data?: { detail?: string } } })?.response?.data?.detail;
      setError(msg ?? "Tạo hồ sơ thất bại, vui lòng thử lại");
    } finally {
      setLoading(false);
    }
  }

  const progressPercent = (step / (STEPS.length - 1)) * 100;

  return (
    <main className="min-h-screen flex items-center justify-center px-5 py-12 bg-cream">
      <div className="w-full max-w-[480px]">
        <div className="text-center mb-8">
          <div className="font-[family-name:var(--font-display)] text-2xl font-semibold">360Human</div>
          <p className="text-stone mt-2">Chỉ cần vài thông tin để bắt đầu</p>
        </div>

        {/* Progress bar */}
        <div className="h-1 bg-sand rounded-sm overflow-hidden mb-8">
          <div className="h-full bg-gold rounded-sm transition-all duration-300" style={{ width: `${progressPercent}%` }} />
        </div>

        {/* Step 0: Name + Gender */}
        {step === 0 && (
          <div className="flex flex-col gap-4">
            <div>
              <label className="block text-[13px] font-medium text-charcoal mb-1.5">Họ tên</label>
              <input
                autoFocus
                type="text"
                value={form.full_name}
                onChange={(e) => set("full_name", e.target.value)}
                placeholder="Họ và tên khai sinh"
                className="w-full px-4 py-3 text-[15px] border border-border rounded-md bg-warm-white text-ink outline-none focus:border-gold focus:shadow-[0_0_0_2px_rgba(184,134,11,0.15)] transition-all"
              />
            </div>
            <div>
              <label className="block text-[13px] font-medium text-charcoal mb-1.5">Giới tính</label>
              <div className="flex gap-2">
                {GENDERS.map((g) => (
                  <button
                    key={g.value}
                    type="button"
                    onClick={() => set("gender", g.value)}
                    className={`flex-1 py-3 rounded-md text-[15px] font-medium transition-colors cursor-pointer ${
                      form.gender === g.value
                        ? "bg-gold text-white border border-gold"
                        : "border border-border text-charcoal hover:bg-sand bg-transparent"
                    }`}
                  >
                    {g.label}
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* Step 1: Birth date */}
        {step === 1 && (
          <div>
            <label className="block text-[13px] font-medium text-charcoal mb-1.5">Ngày sinh</label>
            <input
              type="date"
              value={form.birth_date}
              onChange={(e) => set("birth_date", e.target.value)}
              max={new Date().toISOString().split("T")[0]}
              className="w-full px-4 py-3 text-[15px] border border-border rounded-md bg-warm-white text-ink outline-none focus:border-gold focus:shadow-[0_0_0_2px_rgba(184,134,11,0.15)] transition-all"
            />
          </div>
        )}

        {/* Step 2: Birth time */}
        {step === 2 && (
          <div>
            <label className="block text-[13px] font-medium text-charcoal mb-1.5">Giờ sinh</label>
            <input
              type="text"
              value={form.birth_time ?? ""}
              onChange={(e) => set("birth_time", e.target.value)}
              placeholder="HH:MM (24h)"
              className="w-full px-4 py-3 text-[15px] border border-border rounded-md bg-warm-white text-ink outline-none focus:border-gold focus:shadow-[0_0_0_2px_rgba(184,134,11,0.15)] transition-all"
            />
            <label className="flex items-center gap-2 mt-2 text-[13px] text-stone cursor-pointer">
              <input type="checkbox" className="w-auto" onChange={(e) => { if (e.target.checked) set("birth_time", ""); }} />
              Tôi không nhớ giờ sinh
            </label>
          </div>
        )}

        {/* Step 3: Birth city */}
        {step === 3 && (
          <div>
            <label className="block text-[13px] font-medium text-charcoal mb-1.5">Nơi sinh</label>
            <input
              type="text"
              value={form.birth_city ?? ""}
              onChange={(e) => set("birth_city", e.target.value)}
              placeholder="Thành phố"
              className="w-full px-4 py-3 text-[15px] border border-border rounded-md bg-warm-white text-ink outline-none focus:border-gold focus:shadow-[0_0_0_2px_rgba(184,134,11,0.15)] transition-all"
            />
          </div>
        )}

        {/* Step 4: Confirm */}
        {step === 4 && (
          <div className="bg-sand rounded-xl p-4 flex flex-col gap-2 text-[15px]">
            <Row label="Họ tên" value={form.full_name} />
            <Row label="Giới tính" value={form.gender === "male" ? "Nam" : form.gender === "female" ? "Nữ" : "Khác"} />
            <Row label="Ngày sinh" value={form.birth_date} />
            <Row label="Giờ sinh" value={form.birth_time || "Không có"} />
            <Row label="Nơi sinh" value={form.birth_city || "Không có"} />
            {error && <p className="text-ember mt-2 text-[13px]">{error}</p>}
          </div>
        )}

        {/* Navigation */}
        <div className="flex gap-3 mt-8">
          {step > 0 && (
            <button
              onClick={() => setStep((s) => s - 1)}
              className="flex-1 py-3 border border-border rounded-md text-charcoal hover:bg-sand transition-colors cursor-pointer bg-transparent text-[15px]"
            >
              Quay lại
            </button>
          )}
          {step < STEPS.length - 1 ? (
            <button
              onClick={() => setStep((s) => s + 1)}
              disabled={!canNext()}
              className="flex-1 py-3 bg-gold text-white rounded-md font-medium disabled:opacity-40 hover:bg-gold-soft transition-colors cursor-pointer text-[15px]"
            >
              Tiếp tục
            </button>
          ) : (
            <button
              onClick={handleSubmit}
              disabled={loading}
              className="flex-1 py-4 bg-gold text-white rounded-md font-medium disabled:opacity-40 hover:bg-gold-soft transition-colors cursor-pointer text-base"
            >
              {loading ? "Đang tạo biểu đồ..." : "Bắt đầu khám phá"}
            </button>
          )}
        </div>
      </div>
    </main>
  );
}

function Row({ label, value }: { label: string; value: string }) {
  return (
    <div className="flex justify-between">
      <span className="text-stone">{label}</span>
      <span className="font-medium text-ink">{value}</span>
    </div>
  );
}
