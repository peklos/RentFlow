import { defineStore } from 'pinia'
import { authAPI } from '@/api/services/auth'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: JSON.parse(localStorage.getItem('user')) || null,
    userRole: localStorage.getItem('userRole') || null,
    loading: false,
    error: null
  }),

  getters: {
    isAuthenticated: (state) => !!state.user,
    isClient: (state) => state.userRole === 'client',
    isEmployee: (state) => state.userRole === 'employee'
  },

  actions: {
    async clientRegister(data) {
      this.loading = true
      this.error = null
      try {
        const response = await authAPI.clientRegister(data)
        return response.data
      } catch (error) {
        this.error = error.response?.data?.detail || 'Registration failed'
        throw error
      } finally {
        this.loading = false
      }
    },

    async clientLogin(credentials) {
      this.loading = true
      this.error = null
      try {
        const response = await authAPI.clientLogin(credentials)
        this.user = response.data
        this.userRole = 'client'

        localStorage.setItem('user', JSON.stringify(response.data))
        localStorage.setItem('userRole', 'client')

        return response.data
      } catch (error) {
        this.error = error.response?.data?.detail || 'Login failed'
        throw error
      } finally {
        this.loading = false
      }
    },

    async employeeLogin(credentials) {
      this.loading = true
      this.error = null
      try {
        const response = await authAPI.employeeLogin(credentials)
        this.user = response.data
        this.userRole = 'employee'

        localStorage.setItem('user', JSON.stringify(response.data))
        localStorage.setItem('userRole', 'employee')

        return response.data
      } catch (error) {
        this.error = error.response?.data?.detail || 'Login failed'
        throw error
      } finally {
        this.loading = false
      }
    },

    logout() {
      this.user = null
      this.userRole = null
      localStorage.removeItem('user')
      localStorage.removeItem('userRole')
    }
  }
})
