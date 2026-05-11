import api from "./axios";

export interface CheckoutResponse {
  payment_id: string;
  transaction_ref: string;
  amount: number;
  tier: string;
  vietqr_url: string;
  bank_name: string;
  account_number: string;
  account_name: string;
  status: string;
}

export interface PaymentStatus {
  transaction_ref: string;
  status: string;
  tier: string;
  amount: number;
  confirmed_at: string | null;
}

export const paymentsApi = {
  checkout: (tier: string) =>
    api.post<CheckoutResponse>("/payments/checkout", { tier }),

  verify: (transaction_ref: string, bank_transaction_id: string) =>
    api.post("/payments/verify", { transaction_ref, bank_transaction_id }),

  status: (ref: string) =>
    api.get<PaymentStatus>(`/payments/status/${ref}`),
};
