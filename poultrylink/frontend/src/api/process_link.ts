import apiClient from './client';

export interface ProcessorBooking {
  id: string;
  farmer_id: string;
  processor_id: string;
  booking_date: string;
  quantity: number;
  status: string;
}

export interface CreateBookingPayload {
  processor_id: string;
  booking_date: string;
  quantity: number;
}

export const getBookings = async (): Promise<ProcessorBooking[]> => {
  const { data } = await apiClient.get('/process-link/bookings');
  return data;
};

export const createBooking = async (payload: CreateBookingPayload): Promise<ProcessorBooking> => {
  const { data } = await apiClient.post('/process-link/bookings', payload);
  return data;
};
