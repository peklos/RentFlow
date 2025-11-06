import apiClient from '../axios'

export const profileAPI = {
  getProfile: (clientId) => apiClient.get(`/client/profile/${clientId}`),
  updateProfile: (clientId, data) => apiClient.put(`/client/profile/${clientId}`, data)
}
