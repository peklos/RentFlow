import apiClient from '../axios'

export const paymentsAPI = {
  // Client endpoints
  getMyPayments: () => apiClient.get('/client/payments'),

  // Admin endpoints
  getAll: (params) => apiClient.get('/admin/payments', { params }),
  getById: (id) => apiClient.get(`/admin/payments/${id}`),
  create: (data) => apiClient.post('/admin/payments', data),
  update: (id, data) => apiClient.put(`/admin/payments/${id}`, data),
  delete: (id) => apiClient.delete(`/admin/payments/${id}`)
}
