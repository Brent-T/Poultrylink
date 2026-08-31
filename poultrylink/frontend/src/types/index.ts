export interface User {
  id: string;
  email: string;
  full_name: string;
  phone: string;
  location: string;
  role: UserRole;
  is_verified: boolean;
  rating: number;
  created_at: string;
}

export interface Batch {
  id: string;
  farmer_id: string;
  flock_size: number;
  breed: string;
  age_weeks: number;
  status: string;
  created_at: string;
}

export interface Order {
  id: string;
  buyer_id: string;
  seller_id: string;
  batch_id: string;
  quantity_kg: number;
  status: string;
  total_price: number;
  created_at: string;
}

export interface Delivery {
  id: string;
  order_id: string;
  driver_id: string;
  status: DeliveryStatus;
  updated_at: string;
}

export interface Payment {
  id: string;
  order_id: string;
  amount: number;
  method: string;
  status: string;
  created_at: string;
}

export enum UserRole {
  FARMER = "FARMER",
  BUYER = "BUYER",
  SUPPLIER = "SUPPLIER",
  PROCESSOR = "PROCESSOR",
  DRIVER = "DRIVER"
}

export enum DeliveryStatus {
  ASSIGNED = "ASSIGNED",
  IN_TRANSIT = "IN_TRANSIT",
  DELIVERED = "DELIVERED"
}
