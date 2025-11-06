import apiClient from '../axios'

export const verificationsAPI = {
  getAll: (params) => apiClient.get('/admin/verifications', { params }),
  getById: (id) => apiClient.get(`/admin/verifications/${id}`),
  create: (data) => apiClient.post('/admin/verifications', data),
  update: (id, data) => apiClient.put(`/admin/verifications/${id}`, data),
  delete: (id) => apiClient.delete(`/admin/verifications/${id}`)
}
