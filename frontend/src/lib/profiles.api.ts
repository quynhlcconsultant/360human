import api from "@/lib/axios";

export interface Profile {
  id: string;
  user_id: string;
  full_name: string;
  birth_date: string;
  birth_time: string | null;
  birth_city: string | null;
  birth_lat: string | null;
  birth_lon: string | null;
  birth_timezone: string | null;
  gender: string | null;
  chart_computed_at: string | null;
  created_at: string;
}

export interface ProfileCreate {
  full_name: string;
  birth_date: string;
  birth_time?: string;
  birth_city?: string;
  birth_lat?: string;
  birth_lon?: string;
  birth_timezone?: string;
  gender?: string;
}

export const profilesApi = {
  list: () => api.get<Profile[]>("/profiles"),
  get: (id: string) => api.get<Profile>(`/profiles/${id}`),
  create: (data: ProfileCreate) => api.post<Profile>("/profiles", data),
  update: (id: string, data: Partial<ProfileCreate>) =>
    api.put<Profile>(`/profiles/${id}`, data),
  delete: (id: string) => api.delete(`/profiles/${id}`),
};

export const interpretApi = {
  system: (framework: string, profileId: string) =>
    api.get(`/interpret/system/${framework}/${profileId}`),
  topic: (domain: string, profileId: string) =>
    api.get(`/interpret/topic/${domain}/${profileId}`),
};
