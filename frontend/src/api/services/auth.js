import apiClient from '../axios'

export const authAPI = {
  // Client authentication
  clientRegister: (data) => apiClient.post('/client/auth/register', data),
  clientLogin: (data) => apiClient.post('/client/auth/login', data),
  verifyPhone: (data) => apiClient.post('/client/auth/verify-phone', data),
  resendCode: (phone) => apiClient.post('/client/auth/resend-code', { phone }),

  // Employee authentication
  employeeLogin: (data) => apiClient.post('/employee/auth/login', data)
}
