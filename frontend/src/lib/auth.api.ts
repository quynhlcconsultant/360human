import api from "@/lib/axios";
import type { AuthUser } from "@/stores/auth.store";

export interface TokenResponse {
  access_token: string;
  token_type: string;
}

export const authApi = {
  register: (email: string, password: string) =>
    api.post<TokenResponse>("/auth/register", { email, password }),

  login: (email: string, password: string) =>
    api.post<TokenResponse>("/auth/login", { email, password }),

  me: () => api.get<AuthUser>("/auth/me"),

  refresh: () => api.post<TokenResponse>("/auth/refresh"),
};
