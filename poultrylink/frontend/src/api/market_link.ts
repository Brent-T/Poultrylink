import apiClient from './client';

export interface MarketMatch {
  id: string;
  buyer_id: string;
  farmer_id: string;
  match_score: number;
  status: string;
}

export interface CreateMatchPayload {
  buyer_id: string;
  farmer_id: string;
  match_score: number;
}

export const getMatches = async (): Promise<MarketMatch[]> => {
  const { data } = await apiClient.get('/market-link/matches');
  return data;
};

export const createMatch = async (payload: CreateMatchPayload): Promise<MarketMatch> => {
  const { data } = await apiClient.post('/market-link/matches', payload);
  return data;
};
