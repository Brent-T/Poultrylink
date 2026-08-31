import apiClient from './client';

export interface SupplierListing {
  id: string;
  supplier_id: string;
  product_name: string;
  quantity_available: number;
  price_per_unit: number;
}

export interface CreateListingPayload {
  product_name: string;
  quantity_available: number;
  price_per_unit: number;
}

export const getListings = async (): Promise<SupplierListing[]> => {
  const { data } = await apiClient.get('/supply-market/listings');
  return data;
};

export const createListing = async (payload: CreateListingPayload): Promise<SupplierListing> => {
  const { data } = await apiClient.post('/supply-market/listings', payload);
  return data;
};
