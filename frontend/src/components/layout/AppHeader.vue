<template>
  <header class="app-header">
    <div class="container flex items-center justify-between" style="height: 100%;">
      <!-- Logo -->
      <router-link to="/" class="flex items-center gap-md">
        <div class="logo-icon">
          <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect width="40" height="40" rx="10" fill="url(#gradient)"/>
            <path d="M12 28V16L20 10L28 16V28H23V21H17V28H12Z" fill="white"/>
            <defs>
              <linearGradient id="gradient" x1="0" y1="0" x2="40" y2="40">
                <stop stop-color="#3b82f6"/>
                <stop offset="1" stop-color="#2563eb"/>
              </linearGradient>
            </defs>
          </svg>
        </div>
        <span class="text-2xl font-bold text-primary">RentFlow</span>
      </router-link>

      <!-- Navigation -->
      <nav class="flex items-center gap-lg">
        <router-link to="/properties" class="nav-link">Properties</router-link>

        <template v-if="authStore.isAuthenticated">
          <router-link v-if="authStore.isClient" to="/client/profile" class="nav-link">
            My Account
          </router-link>
          <router-link v-if="authStore.isEmployee" to="/admin/dashboard" class="nav-link">
            Dashboard
          </router-link>
          <BaseButton variant="ghost" @click="handleLogout">Logout</BaseButton>
        </template>
        <template v-else>
          <router-link to="/client/login">
            <BaseButton variant="outline">Login</BaseButton>
          </router-link>
          <router-link to="/client/register">
            <BaseButton variant="primary">Sign Up</BaseButton>
          </router-link>
        </template>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import BaseButton from '@/components/common/BaseButton.vue'

const authStore = useAuthStore()
const router = useRouter()

const handleLogout = () => {
  authStore.logout()
  router.push('/')
}
</script>

<style scoped>
.nav-link {
  color: var(--text-secondary);
  font-weight: var(--font-weight-medium);
  transition: color var(--transition-fast);
}

.nav-link:hover,
.nav-link.router-link-active {
  color: var(--primary-color);
}

.logo-icon {
  filter: drop-shadow(0 0 10px rgba(59, 130, 246, 0.5));
}
</style>
