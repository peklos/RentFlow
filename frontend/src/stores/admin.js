import { defineStore } from 'pinia'
import { adminAPI } from '@/api/services/admin'

export const useAdminStore = defineStore('admin', {
  state: () => ({
    statistics: null,
    clients: [],
    employees: [],
    verifications: [],
    payments: [],
    loading: false,
    error: null
  }),

  actions: {
    async fetchStatistics() {
      this.loading = true
      this.error = null
      try {
        const response = await adminAPI.getStatistics()
        this.statistics = response.data
        return response.data
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to fetch statistics'
        throw error
      } finally {
        this.loading = false
      }
    },

    async fetchClients(params = {}) {
      this.loading = true
      this.error = null
      try {
        const response = await adminAPI.getClients(params)
        this.clients = response.data
        return response.data
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to fetch clients'
        throw error
      } finally {
        this.loading = false
      }
    },

    async fetchEmployees(params = {}) {
      this.loading = true
      this.error = null
      try {
        const response = await adminAPI.getEmployees(params)
        this.employees = response.data
        return response.data
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to fetch employees'
        throw error
      } finally {
        this.loading = false
      }
    }
  }
})
