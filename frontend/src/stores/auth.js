import { defineStore } from 'pinia'
import { authAPI } from '@/api/services/auth'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: JSON.parse(localStorage.getItem('user')) || null,
    token: localStorage.getItem('token') || null,
    userRole: localStorage.getItem('userRole') || null, // 'client' or 'employee'
    loading: false,
    error: null
  }),

  getters: {
    isAuthenticated: (state) => !!state.token,
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
        this.token = response.data.access_token
        this.userRole = 'client'

        localStorage.setItem('token', this.token)
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
        this.token = response.data.access_token
        this.userRole = 'employee'

        localStorage.setItem('token', this.token)
        localStorage.setItem('userRole', 'employee')

        return response.data
      } catch (error) {
        this.error = error.response?.data?.detail || 'Login failed'
        throw error
      } finally {
        this.loading = false
      }
    },

    async verifyPhone(data) {
      try {
        const response = await authAPI.verifyPhone(data)
        return response.data
      } catch (error) {
        this.error = error.response?.data?.detail || 'Verification failed'
        throw error
      }
    },

    logout() {
      this.user = null
      this.token = null
      this.userRole = null
      localStorage.removeItem('user')
      localStorage.removeItem('token')
      localStorage.removeItem('userRole')
    }
  }
})
