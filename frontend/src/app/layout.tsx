import type { Metadata } from "next";
import "./globals.css";
import { Providers } from "@/components/providers";

export const metadata: Metadata = {
  title: {
    default: "360Human — Khám phá bản thân toàn diện",
    template: "%s | 360Human",
  },
  description: "Nền tảng phân tích cá nhân tích hợp 5 hệ thống cổ xưa và hiện đại: Tử Vi, BaZi, Human Design, Số học, Vedic Astrology. Hiểu mình sâu hơn, sống đúng hơn.",
  keywords: ["astrology", "tử vi", "bazi", "human design", "số học", "numerology", "vedic astrology", "phát triển bản thân", "thấu hiểu nội tâm"],
  authors: [{ name: "360Human Team" }],
  creator: "360Human",
  publisher: "360Human",
  formatDetection: {
    email: false,
    address: false,
    telephone: false,
  },
  metadataBase: new URL("https://360human.vn"),
  alternates: {
    canonical: "/",
  },
  openGraph: {
    title: "360Human — Khám phá bản thân toàn diện",
    description: "Hiểu mình sâu hơn, sống đúng hơn qua 5 hệ thống phân tích tích hợp.",
    url: "https://360human.vn",
    siteName: "360Human",
    images: [
      {
        url: "/logo.png",
        width: 1200,
        height: 630,
        alt: "360Human Logo",
      },
    ],
    locale: "vi_VN",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "360Human — Khám phá bản thân toàn diện",
    description: "Nền tảng phân tích cá nhân tích hợp 5 hệ thống chuyên sâu.",
    images: ["/logo.png"],
  },
  icons: {
    icon: "/favicon.png",
    shortcut: "/favicon.png",
    apple: "/favicon.png",
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="vi">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono&family=Lora:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap"
          rel="stylesheet"
        />
      </head>
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
