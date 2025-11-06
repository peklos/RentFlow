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

  // Client authentication
  {
    path: '/client/login',
    name: 'ClientLogin',
    component: () => import('@/views/auth/ClientLoginPage.vue')
  },
  {
    path: '/client/register',
    name: 'ClientRegister',
    component: () => import('@/views/auth/ClientRegisterPage.vue')
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

  // Employee login
  {
    path: '/employee/login',
    name: 'EmployeeLogin',
    component: () => import('@/views/auth/EmployeeLoginPage.vue')
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
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Navigation guard
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()

  if (to.meta.requiresAuth) {
    if (!authStore.isAuthenticated) {
      // Not authenticated - redirect to login
      if (to.meta.role === 'client') {
        next('/client/login')
      } else {
        next('/employee/login')
      }
    } else if (to.meta.role && authStore.userRole !== to.meta.role) {
      // Wrong role
      next('/')
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
