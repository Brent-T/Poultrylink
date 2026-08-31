import apiClient from './client';
import { Batch } from '../types';

export interface CreateBatchPayload {
  flock_size: number;
  breed: string;
  age_weeks: number;
}

export const getBatches = async (): Promise<Batch[]> => {
  const { data } = await apiClient.get('/farmhub/batches');
  return data;
};

export const createBatch = async (payload: CreateBatchPayload): Promise<Batch> => {
  const { data } = await apiClient.post('/farmhub/batches', payload);
  return data;
};
