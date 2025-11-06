import apiClient from '../axios'

export const companiesAPI = {
  getAll: (params) => apiClient.get('/admin/companies', { params }),
  getById: (id) => apiClient.get(`/admin/companies/${id}`),
  create: (data) => apiClient.post('/admin/companies', data),
  update: (id, data) => apiClient.put(`/admin/companies/${id}`, data),
  delete: (id) => apiClient.delete(`/admin/companies/${id}`)
}
