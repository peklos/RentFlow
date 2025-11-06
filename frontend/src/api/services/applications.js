import apiClient from '../axios'

export const applicationsAPI = {
  // Client endpoints
  create: (data) => apiClient.post('/client/applications', data),
  getAll: () => apiClient.get('/client/applications'),
  getById: (id) => apiClient.get(`/client/applications/${id}`),

  // Admin endpoints
  getAllAdmin: (params) => apiClient.get('/admin/applications', { params }),
  update: (id, data) => apiClient.put(`/admin/applications/${id}`, data)
}
