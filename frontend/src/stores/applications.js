import { defineStore } from 'pinia'
import { applicationsAPI } from '@/api/services/applications'

export const useApplicationsStore = defineStore('applications', {
  state: () => ({
    applications: [],
    currentApplication: null,
    loading: false,
    error: null
  }),

  actions: {
    async createApplication(data) {
      this.loading = true
      this.error = null
      try {
        const response = await applicationsAPI.create(data)
        this.applications.unshift(response.data)
        return response.data
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to create application'
        throw error
      } finally {
        this.loading = false
      }
    },

    async fetchApplications() {
      this.loading = true
      this.error = null
      try {
        const response = await applicationsAPI.getAll()
        this.applications = response.data
        return response.data
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to fetch applications'
        throw error
      } finally {
        this.loading = false
      }
    },

    async fetchApplicationById(id) {
      this.loading = true
      this.error = null
      try {
        const response = await applicationsAPI.getById(id)
        this.currentApplication = response.data
        return response.data
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to fetch application'
        throw error
      } finally {
        this.loading = false
      }
    }
  }
})
