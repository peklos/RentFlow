import apiClient from '../axios'

export const adminAPI = {
  getStatistics: () => apiClient.get('/admin/statistics/dashboard'),

  // Clients
  getClients: (params) => apiClient.get('/admin/clients', { params }),
  getClient: (id) => apiClient.get(`/admin/clients/${id}`),

  // Verifications
  getVerifications: () => apiClient.get('/admin/verifications'),
  createVerification: (data) => apiClient.post('/admin/verifications', data),

  // Payments
  getPayments: (params) => apiClient.get('/admin/payments', { params }),
  updatePayment: (id, data) => apiClient.put(`/admin/payments/${id}`, data),

  // Employees
  getEmployees: (params) => apiClient.get('/admin/employees', { params }),
  createEmployee: (data) => apiClient.post('/admin/employees', data),

  // Positions
  getPositions: () => apiClient.get('/admin/positions'),
  createPosition: (data) => apiClient.post('/admin/positions', data),

  // Companies
  getCompanies: () => apiClient.get('/admin/companies'),
  createCompany: (data) => apiClient.post('/admin/companies', data),

  // Services
  getServices: () => apiClient.get('/admin/services'),
  createService: (data) => apiClient.post('/admin/services', data),
  updateService: (id, data) => apiClient.put(`/admin/services/${id}`, data),

  // Reviews
  getReviews: (params) => apiClient.get('/admin/reviews', { params }),
  updateReview: (id, data) => apiClient.put(`/admin/reviews/${id}`, data)
}
