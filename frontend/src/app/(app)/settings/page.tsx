"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { useQuery, useMutation } from "@tanstack/react-query";
import Link from "next/link";
import api from "@/lib/axios";
import { authApi } from "@/lib/auth.api";
import { profilesApi } from "@/lib/profiles.api";
import { useAuthStore } from "@/stores/auth.store";

export default function SettingsPage() {
  const router = useRouter();
  const { logout, isAuthenticated } = useAuthStore();

  const { data: user } = useQuery({
    queryKey: ["me"],
    queryFn: () => authApi.me().then((r) => r.data),
    enabled: isAuthenticated,
  });

  const { data: profiles } = useQuery({
    queryKey: ["profiles"],
    queryFn: () => profilesApi.list().then((r) => r.data),
    enabled: isAuthenticated,
  });

  const [currentPw, setCurrentPw] = useState("");
  const [newPw, setNewPw] = useState("");
  const [confirmPw, setConfirmPw] = useState("");
  const [pwError, setPwError] = useState("");
  const [pwSuccess, setPwSuccess] = useState(false);

  const changePw = useMutation({
    mutationFn: () =>
      api.post("/users/me/change-password", {
        current_password: currentPw,
        new_password: newPw,
      }),
    onSuccess: () => {
      setPwSuccess(true);
      setPwError("");
      setCurrentPw("");
      setNewPw("");
      setConfirmPw("");
    },
    onError: (e: unknown) => {
      const err = e as { response?: { data?: { detail?: string } } };
      setPwError(err?.response?.data?.detail ?? "Đổi mật khẩu thất bại.");
    },
  });

  const handleChangePw = () => {
    setPwError("");
    setPwSuccess(false);
    if (newPw !== confirmPw) { setPwError("Mật khẩu xác nhận không khớp."); return; }
    if (newPw.length < 8) { setPwError("Mật khẩu mới phải ít nhất 8 ký tự."); return; }
    changePw.mutate();
  };

  const handleLogout = () => { logout(); router.push("/login"); };
  const tierLabel = user?.tier?.toUpperCase() ?? "FREE";
  const initials = user?.email?.charAt(0).toUpperCase() ?? "?";
  const activeProfile = profiles?.[0];

  return (
    <div>
      <div className="px-12 py-3 border-b border-border bg-warm-white">
        <Link href="/dashboard" className="text-stone text-sm no-underline hover:text-charcoal">← Dashboard</Link>
      </div>

      <div className="max-w-[960px] mx-auto px-12 py-8 space-y-6">
        {/* Profile Card */}
        <div className="bg-warm-white border border-border rounded-xl p-6 flex gap-6 items-center">
          <div className="w-16 h-16 rounded-full bg-gold-bg flex items-center justify-center font-[family-name:var(--font-display)] text-2xl text-gold font-semibold">
            {initials}
          </div>
          <div className="flex-1">
            <div className="flex items-center gap-3 mb-1">
              <strong className="text-lg">{user?.email?.split("@")[0] ?? "..."}</strong>
              <span className={`inline-flex px-3 py-0.5 text-xs font-semibold rounded-full border ${
                tierLabel === "PRO" ? "bg-gold-bg text-gold border-gold" : "bg-sand text-charcoal border-border"
              }`}>
                {tierLabel}
              </span>
              <Link href="/pricing" className="text-[13px] text-gold no-underline hover:underline">Quản lý gói</Link>
            </div>
            <p className="text-stone text-sm">{user?.email}</p>
          </div>
        </div>

        {/* Birth Data */}
        {activeProfile && (
          <div className="bg-warm-white border border-border rounded-xl p-6">
            <h4 className="font-semibold mb-3">Dữ liệu sinh</h4>
            <p className="text-[15px]">
              {activeProfile.birth_date}
              {activeProfile.birth_time && ` · ${activeProfile.birth_time}`}
              {activeProfile.birth_city && ` · ${activeProfile.birth_city}`}
            </p>
          </div>
        )}

        {/* Profiles */}
        <div className="bg-warm-white border border-border rounded-xl p-6">
          <h4 className="font-semibold mb-3">Hồ sơ</h4>
          <div className="flex flex-col gap-2">
            {profiles?.map((p) => (
              <div key={p.id} className="flex items-center gap-3 p-3 bg-gold-bg rounded-md border border-gold">
                <span>◉</span>
                <strong>{p.full_name}</strong>
                <span className={`ml-auto inline-flex px-3 py-0.5 text-xs font-semibold rounded-full border ${
                  tierLabel === "PRO" ? "bg-gold-bg text-gold border-gold" : "bg-sand text-charcoal border-border"
                }`}>
                  {tierLabel}
                </span>
              </div>
            ))}
          </div>
          <Link
            href="/onboarding"
            className="inline-flex items-center mt-3 px-4 py-2 text-sm border border-border rounded-md text-charcoal no-underline hover:bg-sand transition-colors"
          >
            + Thêm hồ sơ mới
          </Link>
          <p className="text-stone text-xs mt-2">Mỗi hồ sơ mới = 199.000₫ (PRO)</p>
        </div>

        {/* Change Password */}
        <div className="bg-warm-white border border-border rounded-xl p-6">
          <h4 className="font-semibold mb-3">Đổi mật khẩu</h4>
          <div className="space-y-3 max-w-sm">
            <div>
              <label className="block text-[13px] font-medium text-charcoal mb-1">Mật khẩu hiện tại</label>
              <input
                type="password"
                value={currentPw}
                onChange={(e) => setCurrentPw(e.target.value)}
                className="w-full px-4 py-3 text-[15px] border border-border rounded-md bg-cream text-ink outline-none focus:border-gold transition-all"
              />
            </div>
            <div>
              <label className="block text-[13px] font-medium text-charcoal mb-1">Mật khẩu mới</label>
              <input
                type="password"
                value={newPw}
                onChange={(e) => setNewPw(e.target.value)}
                className="w-full px-4 py-3 text-[15px] border border-border rounded-md bg-cream text-ink outline-none focus:border-gold transition-all"
              />
            </div>
            <div>
              <label className="block text-[13px] font-medium text-charcoal mb-1">Xác nhận mật khẩu mới</label>
              <input
                type="password"
                value={confirmPw}
                onChange={(e) => setConfirmPw(e.target.value)}
                className="w-full px-4 py-3 text-[15px] border border-border rounded-md bg-cream text-ink outline-none focus:border-gold transition-all"
              />
            </div>
          </div>
          {pwError && <p className="text-[13px] text-ember mt-3">{pwError}</p>}
          {pwSuccess && <p className="text-[13px] text-sage mt-3">Đổi mật khẩu thành công.</p>}
          <button
            onClick={handleChangePw}
            disabled={!currentPw || !newPw || !confirmPw || changePw.isPending}
            className="mt-4 px-4 py-2 text-sm border border-border rounded-md text-charcoal hover:bg-sand disabled:opacity-40 transition-colors cursor-pointer bg-transparent"
          >
            {changePw.isPending ? "Đang lưu..." : "Đổi mật khẩu"}
          </button>
        </div>

        {/* Danger Zone */}
        <div className="bg-error-bg border border-error rounded-xl p-6">
          <h4 className="text-error font-semibold mb-3">Vùng nguy hiểm</h4>
          <button
            onClick={handleLogout}
            className="px-4 py-2 text-sm border border-error text-error rounded-md bg-transparent hover:bg-error/5 transition-colors cursor-pointer"
          >
            Đăng xuất
          </button>
        </div>
      </div>
    </div>
  );
}
