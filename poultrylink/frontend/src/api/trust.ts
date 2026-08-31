import apiClient from './client';

export interface TrustProfile {
  id: string;
  email: string;
  full_name: string;
  role: string;
  rating: number;
  is_verified: boolean;
  order_count: number;
}

export const getUserTrustProfile = async (userId: string): Promise<TrustProfile> => {
  const { data } = await apiClient.get(`/trust/${userId}`);
  return data;
};
