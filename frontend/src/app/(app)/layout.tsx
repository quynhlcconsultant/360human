"use client";

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { useQuery } from "@tanstack/react-query";
import { authApi } from "@/lib/auth.api";
import { useAuthStore } from "@/stores/auth.store";

const NAV_ITEMS = [
  { href: "/dashboard", icon: "◉", label: "Tổng Quan" },
  { href: "/systems", icon: "◇", label: "Biểu đồ hệ thống" },
  { href: "/topics", icon: "⊚", label: "Phân tích sâu" },
  { href: "/time-oracle", icon: "◷", label: "Lịch Vận" },
  { href: "/actions", icon: "△", label: "Hành động" },
  { href: "/pricing", icon: "✦", label: "Nâng cấp" },
  { href: "/settings", icon: "⚙", label: "Cài đặt" },
];

export default function AppLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const router = useRouter();
  const { token, logout } = useAuthStore();

  const { data: user } = useQuery({
    queryKey: ["me"],
    queryFn: () => authApi.me().then((r) => r.data),
    enabled: !!token,
  });

  // Pages that should NOT show sidebar (onboarding, checkout flow)
  const fullscreenPaths = ["/onboarding", "/checkout"];
  const isFullscreen = fullscreenPaths.some((p) => pathname.startsWith(p));

  if (isFullscreen) {
    return <>{children}</>;
  }

  const handleLogout = () => {
    logout();
    router.push("/login");
  };

  const tierLabel = user?.tier?.toUpperCase() || "FREE";

  return (
    <div className="flex min-h-screen">
      {/* Sidebar */}
      <nav className="w-[240px] bg-warm-white border-r border-border flex-shrink-0 flex flex-col">
        <div className="px-6 py-6">
          <Link href="/dashboard" className="font-[family-name:var(--font-display)] text-xl font-semibold text-ink no-underline">
            360Human
          </Link>
        </div>
        <ul className="list-none flex flex-col">
          {NAV_ITEMS.map((item) => {
            const isActive = pathname === item.href || pathname.startsWith(item.href + "/");
            return (
              <li key={item.href}>
                <Link
                  href={item.href}
                  className={`flex items-center gap-2.5 px-6 py-2.5 text-[15px] no-underline transition-colors ${
                    isActive
                      ? "text-gold bg-gold-bg font-medium"
                      : "text-charcoal hover:bg-sand"
                  }`}
                >
                  <span>{item.icon}</span>
                  <span>{item.label}</span>
                </Link>
              </li>
            );
          })}
        </ul>
      </nav>

      {/* Main content */}
      <div className="flex-1 flex flex-col overflow-y-auto">
        {/* Topbar */}
        <div className="flex items-center justify-between px-12 py-4 border-b border-border bg-warm-white">
          <div className="flex items-center gap-3">
            <span className="font-medium">{user?.email?.split("@")[0] || "..."}</span>
            <span
              className={`inline-flex px-3 py-0.5 text-xs font-semibold rounded-full border ${
                tierLabel === "PRO"
                  ? "bg-gold-bg text-gold border-gold"
                  : "bg-sand text-charcoal border-border"
              }`}
            >
              {tierLabel}
            </span>
          </div>
          <div className="flex items-center gap-3">
            <button
              onClick={handleLogout}
              className="px-4 py-2 text-sm border border-border rounded-md text-charcoal hover:bg-sand transition-colors cursor-pointer bg-transparent"
            >
              Đăng xuất
            </button>
          </div>
        </div>

        {/* Page content */}
        <main className="flex-1">{children}</main>
      </div>
    </div>
  );
}
