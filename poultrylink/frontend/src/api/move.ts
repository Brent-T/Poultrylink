import apiClient from './client';
import { Delivery } from '../types';

export interface CreateDeliveryPayload {
  order_id: string;
  driver_id: string;
  pickup_location: string;
  dropoff_location: string;
}

export const getDeliveries = async (): Promise<Delivery[]> => {
  const { data } = await apiClient.get('/move/deliveries');
  return data;
};

export const createDelivery = async (payload: CreateDeliveryPayload): Promise<Delivery> => {
  const { data } = await apiClient.post('/move/deliveries', payload);
  return data;
};
