import apiClient from '../axios'

export const employeesAPI = {
  getAll: (params) => apiClient.get('/admin/employees', { params }),
  getById: (id) => apiClient.get(`/admin/employees/${id}`),
  create: (data) => apiClient.post('/admin/employees', data),
  update: (id, data) => apiClient.put(`/admin/employees/${id}`, data),
  delete: (id) => apiClient.delete(`/admin/employees/${id}`)
}
