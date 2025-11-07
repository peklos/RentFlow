import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const routes = [
  // Public routes
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/client/HomePage.vue')
  },
  {
    path: '/properties',
    name: 'Properties',
    component: () => import('@/views/client/PropertiesPage.vue')
  },
  {
    path: '/properties/:id',
    name: 'PropertyDetail',
    component: () => import('@/views/client/PropertyDetailPage.vue')
  },
  {
    path: '/search',
    name: 'Search',
    component: () => import('@/views/client/SearchPage.vue')
  },

  // Client authentication
  {
    path: '/client/login',
    name: 'ClientLogin',
    component: () => import('@/views/auth/ClientLoginPage.vue'),
    meta: { requiresGuest: true, role: 'client' }
  },
  {
    path: '/client/register',
    name: 'ClientRegister',
    component: () => import('@/views/auth/ClientRegisterPage.vue'),
    meta: { requiresGuest: true, role: 'client' }
  },

  // Client protected routes
  {
    path: '/client/profile',
    name: 'ClientProfile',
    component: () => import('@/views/client/ProfilePage.vue'),
    meta: { requiresAuth: true, role: 'client' }
  },
  {
    path: '/client/applications',
    name: 'ClientApplications',
    component: () => import('@/views/client/ApplicationsPage.vue'),
    meta: { requiresAuth: true, role: 'client' }
  },
  {
    path: '/client/contracts',
    name: 'ClientContracts',
    component: () => import('@/views/client/ContractsPage.vue'),
    meta: { requiresAuth: true, role: 'client' }
  },
  {
    path: '/client/payments',
    name: 'ClientPayments',
    component: () => import('@/views/client/PaymentsPage.vue'),
    meta: { requiresAuth: true, role: 'client' }
  },
  {
    path: '/client/reviews',
    name: 'ClientReviews',
    component: () => import('@/views/client/ReviewsPage.vue'),
    meta: { requiresAuth: true, role: 'client' }
  },
  {
    path: '/client/services',
    name: 'ClientServices',
    component: () => import('@/views/client/ServicesPage.vue'),
    meta: { requiresAuth: true, role: 'client' }
  },

  // Employee login
  {
    path: '/employee/login',
    name: 'EmployeeLogin',
    component: () => import('@/views/auth/EmployeeLoginPage.vue'),
    meta: { requiresGuest: true, role: 'employee' }
  },

  // Admin routes
  {
    path: '/admin',
    redirect: '/admin/dashboard'
  },
  {
    path: '/admin/dashboard',
    name: 'AdminDashboard',
    component: () => import('@/views/admin/DashboardPage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/properties',
    name: 'AdminProperties',
    component: () => import('@/views/admin/PropertiesManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/applications',
    name: 'AdminApplications',
    component: () => import('@/views/admin/ApplicationsManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/clients',
    name: 'AdminClients',
    component: () => import('@/views/admin/ClientsManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/payments',
    name: 'AdminPayments',
    component: () => import('@/views/admin/PaymentsManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/reviews',
    name: 'AdminReviews',
    component: () => import('@/views/admin/ReviewsManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/companies',
    name: 'AdminCompanies',
    component: () => import('@/views/admin/CompaniesManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/positions',
    name: 'AdminPositions',
    component: () => import('@/views/admin/PositionsManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/employees',
    name: 'AdminEmployees',
    component: () => import('@/views/admin/EmployeesManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/services',
    name: 'AdminServices',
    component: () => import('@/views/admin/ServicesManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/verifications',
    name: 'AdminVerifications',
    component: () => import('@/views/admin/VerificationsManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Navigation guard
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()

  // Redirect authenticated users away from login/register pages
  if (to.meta.requiresGuest) {
    if (authStore.isAuthenticated) {
      // Already authenticated - redirect based on role
      if (authStore.userRole === 'client') {
        next('/client/profile')
      } else if (authStore.userRole === 'employee') {
        next('/admin/dashboard')
      } else {
        next('/')
      }
      return
    }
  }

  // Protect authenticated routes
  if (to.meta.requiresAuth) {
    if (!authStore.isAuthenticated) {
      // Not authenticated - redirect to login
      if (to.meta.role === 'client') {
        next('/client/login')
      } else {
        next('/employee/login')
      }
      return
    } else if (to.meta.role && authStore.userRole !== to.meta.role) {
      // Wrong role
      next('/')
      return
    }
  }

  next()
})

export default router
