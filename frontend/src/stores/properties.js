import { defineStore } from 'pinia'
import { propertiesAPI } from '@/api/services/properties'

export const usePropertiesStore = defineStore('properties', {
  state: () => ({
    properties: [],
    currentProperty: null,
    loading: false,
    error: null,
    filters: {
      type: null,
      min_price: null,
      max_price: null,
      min_area: null,
      max_area: null,
      rooms_count: null,
      is_furnished: null,
      status: 'available'
    }
  }),

  getters: {
    availableProperties: (state) =>
      state.properties.filter(p => p.status === 'available')
  },

  actions: {
    async fetchProperties(params = {}) {
      this.loading = true
      this.error = null
      try {
        const response = await propertiesAPI.getAll({ ...this.filters, ...params })
        this.properties = response.data
        return response.data
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to fetch properties'
        throw error
      } finally {
        this.loading = false
      }
    },

    async fetchPropertyById(id) {
      this.loading = true
      this.error = null
      try {
        const response = await propertiesAPI.getById(id)
        this.currentProperty = response.data
        return response.data
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to fetch property'
        throw error
      } finally {
        this.loading = false
      }
    },

    async createProperty(data) {
      this.loading = true
      this.error = null
      try {
        const response = await propertiesAPI.create(data)
        this.properties.unshift(response.data)
        return response.data
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to create property'
        throw error
      } finally {
        this.loading = false
      }
    },

    updateFilters(newFilters) {
      this.filters = { ...this.filters, ...newFilters }
    }
  }
})
