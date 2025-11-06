import apiClient from '../axios'

export const statisticsAPI = {
  getDashboard: () => apiClient.get('/admin/statistics/dashboard'),
  getRevenue: (params) => apiClient.get('/admin/statistics/revenue', { params }),
  getOccupancy: (params) => apiClient.get('/admin/statistics/occupancy', { params }),
  getPayments: (params) => apiClient.get('/admin/statistics/payments', { params })
}
