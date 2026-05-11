import { create } from "zustand";
import { persist, type StorageValue } from "zustand/middleware";

// Lưu token vào cookie để Next.js middleware đọc được (server-side)
const cookieStorage = {
  getItem: (name: string) => {
    if (typeof document === "undefined") return null;
    const match = document.cookie
      .split("; ")
      .find((row) => row.startsWith(`${name}=`));
    if (!match) return null;
    try {
      return JSON.parse(decodeURIComponent(match.split("=").slice(1).join("=")));
    } catch {
      return null;
    }
  },
  setItem: (name: string, value: StorageValue<unknown>) => {
    if (typeof document === "undefined") return;
    const encoded = encodeURIComponent(JSON.stringify(value));
    document.cookie = `${name}=${encoded}; path=/; max-age=${30 * 24 * 60 * 60}; SameSite=Lax`;
  },
  removeItem: (name: string) => {
    if (typeof document === "undefined") return;
    document.cookie = `${name}=; path=/; max-age=0`;
  },
};

export type Tier = "free" | "pro";

export interface AuthUser {
  id: string;
  email: string;
  tier: Tier;
  is_active: boolean;
  paid_at: string | null;
  created_at: string;
}

interface AuthState {
  token: string | null;
  user: AuthUser | null;
  isAuthenticated: boolean;

  setToken: (token: string) => void;
  setUser: (user: AuthUser) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      token: null,
      user: null,
      isAuthenticated: false,

      setToken: (token) => set({ token, isAuthenticated: true }),

      setUser: (user) => set({ user }),

      logout: () => set({ token: null, user: null, isAuthenticated: false }),
    }),
    {
      name: "360human-auth",
      storage: cookieStorage,
      partialize: (state) => ({ token: state.token, isAuthenticated: state.isAuthenticated }),
    }
  )
);
