import apiClient from './client';
import { User } from '../types';

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface RegisterPayload {
  email: string;
  password: string;
  full_name: string;
  phone: string;
  location: string;
  role: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
  user: User;
}

export const login = async (credentials: LoginCredentials): Promise<AuthResponse> => {
  const { data } = await apiClient.post('/auth/login', credentials);
  return data;
};

export const register = async (payload: RegisterPayload): Promise<AuthResponse> => {
  const { data } = await apiClient.post('/auth/register', payload);
  return data;
};

export const getCurrentUser = async (): Promise<User> => {
  const { data } = await apiClient.get('/auth/me');
  return data;
};
