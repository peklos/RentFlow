import apiClient from '../axios'

export const servicesAPI = {
  // Client endpoints
  getAll: (params) => apiClient.get('/client/services', { params }),

  // Admin endpoints
  getAllAdmin: (params) => apiClient.get('/admin/services', { params }),
  getById: (id) => apiClient.get(`/admin/services/${id}`),
  create: (data) => apiClient.post('/admin/services', data),
  update: (id, data) => apiClient.put(`/admin/services/${id}`, data),
  delete: (id) => apiClient.delete(`/admin/services/${id}`)
}
