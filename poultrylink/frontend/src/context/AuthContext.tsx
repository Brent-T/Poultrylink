import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { User, UserRole } from '../types';
import { login as apiLogin, register as apiRegister, getCurrentUser } from '../api/auth';

interface AuthContextType {
  user: User | null;
  access_token: string | null;
  role: UserRole | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
  register: (payload: { email: string; password: string; full_name: string; phone: string; location: string; role: string }) => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<User | null>(null);
  const [access_token, setAccessToken] = useState<string | null>(localStorage.getItem('access_token'));
  const [role, setRole] = useState<UserRole | null>(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const initAuth = async () => {
      const token = localStorage.getItem('access_token');
      if (token) {
        try {
          const currentUser = await getCurrentUser();
          setUser(currentUser);
          setAccessToken(token);
          setRole(currentUser.role);
          setIsAuthenticated(true);
        } catch (error) {
          localStorage.removeItem('access_token');
          setAccessToken(null);
          setUser(null);
          setIsAuthenticated(false);
        }
      }
      setIsLoading(false);
    };

    initAuth();
  }, []);

  const login = async (email: string, password: string) => {
    const response = await apiLogin({ email, password });
    localStorage.setItem('access_token', response.access_token);
    setAccessToken(response.access_token);
    setUser(response.user);
    setRole(response.user.role);
    setIsAuthenticated(true);
  };

  const register = async (payload: { email: string; password: string; full_name: string; phone: string; location: string; role: string }) => {
    const response = await apiRegister(payload);
    localStorage.setItem('access_token', response.access_token);
    setAccessToken(response.access_token);
    setUser(response.user);
    setRole(response.user.role);
    setIsAuthenticated(true);
  };

  const logout = () => {
    localStorage.removeItem('access_token');
    setAccessToken(null);
    setUser(null);
    setRole(null);
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{ user, access_token, role, isAuthenticated, isLoading, login, logout, register }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
