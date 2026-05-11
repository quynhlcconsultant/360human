"use client";

import { useQuery } from "@tanstack/react-query";
import { interpretApi } from "@/lib/profiles.api";
import { useAuthStore } from "@/stores/auth.store";

export interface InterpretResult {
  profile_id: string;
  tier: string;
  interpretation: string;
  word_count: number;
  framework?: string;
  domain?: string;
}

/**
 * Hook luận giải theo hệ thống (Tử Vi, BaZi, HD, Vedic, Số học)
 * Cache 30 phút phía client — Redis cache 30 ngày phía server
 */
export function useSystemInterpret(framework: string, profileId: string) {
  const isAuthenticated = useAuthStore((s) => s.isAuthenticated);

  return useQuery<InterpretResult>({
    queryKey: ["interpret", "system", framework, profileId],
    queryFn: () => interpretApi.system(framework, profileId).then((r) => r.data),
    enabled: isAuthenticated && !!profileId && !!framework,
    staleTime: 1000 * 60 * 30,
    retry: 1,
  });
}

/**
 * Hook luận giải theo chủ đề (overview, love, career, ...)
 */
export function useTopicInterpret(domain: string, profileId: string) {
  const isAuthenticated = useAuthStore((s) => s.isAuthenticated);

  return useQuery<InterpretResult>({
    queryKey: ["interpret", "topic", domain, profileId],
    queryFn: () => interpretApi.topic(domain, profileId).then((r) => r.data),
    enabled: isAuthenticated && !!profileId && !!domain,
    staleTime: 1000 * 60 * 30,
    retry: 1,
  });
}

/**
 * Hook lấy raw chart data (L1) của profile
 */
export function useChartData(profileId: string) {
  const isAuthenticated = useAuthStore((s) => s.isAuthenticated);
  const { profilesApi } = require("@/lib/profiles.api");

  return useQuery({
    queryKey: ["charts", profileId],
    queryFn: () => profilesApi.get(profileId).then((r: { data: unknown }) => r.data),
    enabled: isAuthenticated && !!profileId,
    staleTime: 1000 * 60 * 60,  // chart data ít thay đổi hơn
  });
}
