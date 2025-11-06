import apiClient from '../axios'

export const positionsAPI = {
  getAll: (params) => apiClient.get('/admin/positions', { params }),
  getById: (id) => apiClient.get(`/admin/positions/${id}`),
  create: (data) => apiClient.post('/admin/positions', data),
  update: (id, data) => apiClient.put(`/admin/positions/${id}`, data),
  delete: (id) => apiClient.delete(`/admin/positions/${id}`)
}
