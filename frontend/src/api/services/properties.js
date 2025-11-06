import apiClient from '../axios'

export const propertiesAPI = {
  getAll: (params) => apiClient.get('/client/properties', { params }),
  getById: (id) => apiClient.get(`/client/properties/${id}`),

  // Admin endpoints
  getAllAdmin: (params) => apiClient.get('/admin/properties', { params }),
  create: (data) => apiClient.post('/admin/properties', data),
  update: (id, data) => apiClient.put(`/admin/properties/${id}`, data),
  delete: (id) => apiClient.delete(`/admin/properties/${id}`)
}
