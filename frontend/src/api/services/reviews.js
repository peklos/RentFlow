import apiClient from '../axios'

export const reviewsAPI = {
  // Client endpoints
  getMyReviews: () => apiClient.get('/client/reviews'),
  create: (data) => apiClient.post('/client/reviews', data),

  // Admin endpoints
  getAll: (params) => apiClient.get('/admin/reviews', { params }),
  getById: (id) => apiClient.get(`/admin/reviews/${id}`),
  update: (id, data) => apiClient.put(`/admin/reviews/${id}`, data),
  approve: (id) => apiClient.patch(`/admin/reviews/${id}/approve`),
  delete: (id) => apiClient.delete(`/admin/reviews/${id}`)
}
