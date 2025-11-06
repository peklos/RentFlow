import apiClient from '../axios'

export const contractsAPI = {
  // Client endpoints
  getAll: () => apiClient.get('/client/contracts'),
  getById: (id) => apiClient.get(`/client/contracts/${id}`),

  // Admin endpoints
  getAllAdmin: (params) => apiClient.get('/admin/contracts', { params }),
  create: (data) => apiClient.post('/admin/contracts', data),
  update: (id, data) => apiClient.put(`/admin/contracts/${id}`, data)
}
