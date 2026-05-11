"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { authApi } from "@/lib/auth.api";
import { useAuthStore } from "@/stores/auth.store";

export default function RegisterPage() {
  const router = useRouter();
  const { setToken, setUser } = useAuthStore();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError("");
    if (password.length < 8) {
      setError("Mật khẩu phải có ít nhất 8 ký tự");
      return;
    }
    if (password !== confirmPassword) {
      setError("Mật khẩu xác nhận không khớp");
      return;
    }
    setLoading(true);
    try {
      const { data } = await authApi.register(email, password);
      setToken(data.access_token);
      const { data: user } = await authApi.me();
      setUser(user);
      router.push("/onboarding");
    } catch (err: unknown) {
      const msg = (err as { response?: { data?: { detail?: string } } })?.response?.data?.detail;
      setError(msg ?? "Đăng ký thất bại, vui lòng thử lại");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen flex items-center justify-center px-5 py-12 bg-cream">
      <div className="w-full max-w-[480px]">
        <div className="text-center mb-8">
          <Link href="/" className="font-[family-name:var(--font-display)] text-2xl font-semibold text-ink no-underline">
            360Human
          </Link>
        </div>

        {/* Tabs */}
        <div className="flex border-b border-border mb-6">
          <div className="px-6 py-3 text-[15px] font-medium text-gold border-b-2 border-gold">
            Đăng ký
          </div>
          <Link href="/login" className="px-6 py-3 text-[15px] font-medium text-stone border-b-2 border-transparent hover:text-charcoal transition-colors no-underline">
            Đăng nhập
          </Link>
        </div>

        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          <div>
            <label className="block text-[13px] font-medium text-charcoal mb-1.5">Email</label>
            <input
              type="email"
              required
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-4 py-3 text-[15px] border border-border rounded-md bg-warm-white text-ink outline-none focus:border-gold focus:shadow-[0_0_0_2px_rgba(184,134,11,0.15)] transition-all"
              placeholder="email@example.com"
            />
          </div>
          <div>
            <label className="block text-[13px] font-medium text-charcoal mb-1.5">Mật khẩu</label>
            <input
              type="password"
              required
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-3 text-[15px] border border-border rounded-md bg-warm-white text-ink outline-none focus:border-gold focus:shadow-[0_0_0_2px_rgba(184,134,11,0.15)] transition-all"
              placeholder="Tối thiểu 8 ký tự"
            />
          </div>
          <div>
            <label className="block text-[13px] font-medium text-charcoal mb-1.5">Xác nhận mật khẩu</label>
            <input
              type="password"
              required
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              className="w-full px-4 py-3 text-[15px] border border-border rounded-md bg-warm-white text-ink outline-none focus:border-gold focus:shadow-[0_0_0_2px_rgba(184,134,11,0.15)] transition-all"
              placeholder="Nhập lại mật khẩu"
            />
          </div>

          {error && <p className="text-[13px] text-ember">{error}</p>}

          <button
            type="submit"
            disabled={loading}
            className="w-full py-3 rounded-md bg-gold text-white font-medium text-[15px] hover:bg-gold-soft disabled:opacity-50 transition-colors cursor-pointer"
          >
            {loading ? "Đang tạo tài khoản..." : "Tạo tài khoản"}
          </button>
        </form>

        <div className="flex items-center gap-4 my-6 text-stone text-[13px]">
          <div className="flex-1 h-px bg-border" />
          <span>hoặc</span>
          <div className="flex-1 h-px bg-border" />
        </div>
        <button className="w-full py-3 text-[15px] border border-border rounded-md text-charcoal opacity-50 cursor-not-allowed bg-transparent">
          Google Sign-In (sắp ra mắt)
        </button>
      </div>
    </main>
  );
}
