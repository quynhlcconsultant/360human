"use client";

import { Suspense, useEffect, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Image from "next/image";
import { paymentsApi, type CheckoutResponse } from "@/lib/payments.api";
import { useAuthStore } from "@/stores/auth.store";

type Step = "qr" | "verify" | "polling" | "done";

export default function CheckoutPage() {
  return (
    <Suspense fallback={<div className="min-h-screen flex items-center justify-center text-stone">Đang tải...</div>}>
      <CheckoutContent />
    </Suspense>
  );
}

function CheckoutContent() {
  const router = useRouter();
  const params = useSearchParams();
  const tier = params.get("tier") ?? "pro";

  const [checkout, setCheckout] = useState<CheckoutResponse | null>(null);
  const [step, setStep] = useState<Step>("qr");
  const [bankTxId, setBankTxId] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  const { setUser } = useAuthStore();

  useEffect(() => {
    paymentsApi
      .checkout(tier)
      .then((r) => {
        setCheckout(r.data);
        setLoading(false);
      })
      .catch((e) => {
        setError(e?.response?.data?.detail ?? "Không thể khởi tạo thanh toán.");
        setLoading(false);
      });
  }, [tier]);

  // Poll payment status every 5s after submitting verification
  useEffect(() => {
    if (step !== "polling" || !checkout) return;
    const interval = setInterval(async () => {
      try {
        const res = await paymentsApi.status(checkout.transaction_ref);
        if (res.data.status === "confirmed") {
          clearInterval(interval);
          setStep("done");
          // Refresh user data from auth store by re-fetching /auth/me
          setTimeout(() => router.push("/checkout/success"), 1500);
        }
      } catch {}
    }, 5000);
    return () => clearInterval(interval);
  }, [step, checkout, router]);

  const handleVerify = async () => {
    if (!checkout || !bankTxId.trim()) return;
    setError("");
    try {
      await paymentsApi.verify(checkout.transaction_ref, bankTxId.trim());
      setStep("polling");
    } catch (e: unknown) {
      const err = e as { response?: { data?: { detail?: string } } };
      setError(err?.response?.data?.detail ?? "Lỗi xác nhận. Vui lòng thử lại.");
    }
  };

  if (loading) {
    return (
      <main className="min-h-screen bg-[#F7F3ED] flex items-center justify-center">
        <div className="text-[#78716C]">Đang tạo mã QR...</div>
      </main>
    );
  }

  if (error && !checkout) {
    return (
      <main className="min-h-screen bg-[#F7F3ED] flex items-center justify-center px-6">
        <div className="bg-[#F2DDD3] border border-[#B85C38] rounded-xl p-6 text-[#B85C38] max-w-md text-center">
          <p className="font-semibold mb-2">Lỗi</p>
          <p className="text-sm">{error}</p>
          <button onClick={() => router.back()} className="mt-4 text-sm underline">
            Quay lại
          </button>
        </div>
      </main>
    );
  }

  const tierLabel = tier === "max" ? "MAX" : "PRO";
  const amount = checkout?.amount.toLocaleString("vi-VN") + "₫";

  return (
    <main className="min-h-screen bg-[#F7F3ED]">
      <header className="bg-[#FFFDF9] border-b border-[#E7E0D6] px-6 py-4 flex items-center gap-4">
        <button onClick={() => router.back()} className="text-[#78716C] hover:text-[#1C1917] text-sm">
          ← Quay lại
        </button>
        <h1 className="text-lg font-bold text-[#1C1917]" style={{ fontFamily: "var(--font-display)" }}>
          Thanh toán — Gói {tierLabel}
        </h1>
      </header>

      <div className="max-w-md mx-auto px-6 py-10">
        {/* Step: QR */}
        {(step === "qr" || step === "verify") && checkout && (
          <div className="bg-[#FFFDF9] border border-[#E7E0D6] rounded-2xl p-6">
            <div className="text-center mb-6">
              <p className="text-sm text-[#78716C] mb-1">Số tiền</p>
              <p className="text-3xl font-bold text-[#B8860B]" style={{ fontFamily: "var(--font-display)" }}>
                {amount}
              </p>
              <p className="text-xs text-[#78716C] mt-1">
                Mã giao dịch: <span className="font-mono font-bold text-[#1C1917]">{checkout.transaction_ref}</span>
              </p>
            </div>

            {/* VietQR image */}
            <div className="flex justify-center mb-6">
              <div className="border-4 border-[#E7E0D6] rounded-xl overflow-hidden">
                <img
                  src={checkout.vietqr_url}
                  alt="VietQR"
                  width={220}
                  height={220}
                  className="block"
                />
              </div>
            </div>

            <div className="bg-[#F7F3ED] rounded-xl p-4 text-sm text-[#44403C] space-y-1 mb-6">
              <p><span className="text-[#78716C]">Ngân hàng:</span> {checkout.bank_name}</p>
              <p><span className="text-[#78716C]">Số TK:</span> {checkout.account_number}</p>
              <p><span className="text-[#78716C]">Tên TK:</span> {checkout.account_name}</p>
              <p className="text-xs text-[#78716C] pt-1">
                Nội dung chuyển khoản phải có mã: <span className="font-mono font-bold text-[#1C1917]">{checkout.transaction_ref}</span>
              </p>
            </div>

            {step === "qr" && (
              <button
                onClick={() => setStep("verify")}
                className="w-full py-3 bg-[#B8860B] text-white rounded-xl font-semibold hover:bg-[#D4A843] transition-colors"
              >
                Tôi đã chuyển khoản →
              </button>
            )}

            {step === "verify" && (
              <div>
                <p className="text-sm font-medium text-[#1C1917] mb-2">
                  Nhập mã giao dịch ngân hàng của bạn:
                </p>
                <input
                  type="text"
                  value={bankTxId}
                  onChange={(e) => setBankTxId(e.target.value)}
                  placeholder="Ví dụ: FT26082345678"
                  className="w-full px-4 py-2.5 border border-[#E7E0D6] rounded-lg text-sm focus:outline-none focus:border-[#B8860B] mb-3"
                />
                {error && <p className="text-xs text-[#B85C38] mb-3">{error}</p>}
                <button
                  onClick={handleVerify}
                  disabled={!bankTxId.trim()}
                  className="w-full py-3 bg-[#B8860B] text-white rounded-xl font-semibold hover:bg-[#D4A843] transition-colors disabled:opacity-50"
                >
                  Xác nhận →
                </button>
              </div>
            )}
          </div>
        )}

        {/* Step: Polling */}
        {step === "polling" && (
          <div className="bg-[#FFFDF9] border border-[#E7E0D6] rounded-2xl p-8 text-center">
            <div className="text-4xl mb-4">⏳</div>
            <p className="font-semibold text-[#1C1917] mb-2">Đang xác nhận thanh toán</p>
            <p className="text-sm text-[#78716C]">
              Chúng tôi đang kiểm tra giao dịch của bạn. Trang này tự động cập nhật.
            </p>
            <div className="mt-6 flex justify-center gap-1">
              {[0, 1, 2].map((i) => (
                <div
                  key={i}
                  className="w-2 h-2 bg-[#B8860B] rounded-full animate-bounce"
                  style={{ animationDelay: `${i * 0.2}s` }}
                />
              ))}
            </div>
          </div>
        )}

        {/* Step: Done */}
        {step === "done" && (
          <div className="bg-[#FFFDF9] border border-[#6B8F71] rounded-2xl p-8 text-center">
            <div className="text-4xl mb-4">✅</div>
            <p className="font-bold text-[#1C1917] text-xl mb-2">Thanh toán thành công!</p>
            <p className="text-sm text-[#78716C]">Đang chuyển hướng...</p>
          </div>
        )}
      </div>
    </main>
  );
}
