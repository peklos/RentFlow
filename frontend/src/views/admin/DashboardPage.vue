<template>
  <div class="dashboard-page">
    <div class="app-header">
      <div class="container flex items-center justify-between" style="height: 100%;">
        <h1 class="text-2xl font-bold">Admin Dashboard</h1>
        <BaseButton variant="ghost" @click="handleLogout">Logout</BaseButton>
      </div>
    </div>

    <div class="app-main">
      <aside class="app-sidebar">
        <nav class="sidebar-nav">
          <router-link to="/admin/dashboard" class="sidebar-link active">
            📊 Dashboard
          </router-link>
          <router-link to="/admin/properties" class="sidebar-link">
            🏢 Properties
          </router-link>
          <router-link to="/admin/applications" class="sidebar-link">
            📝 Applications
          </router-link>
          <router-link to="/admin/clients" class="sidebar-link">
            👥 Clients
          </router-link>
        </nav>
      </aside>

      <main class="app-content">
        <h2 class="text-3xl font-bold mb-xl">Overview</h2>

        <!-- Statistics Cards -->
        <div class="grid grid-cols-4 gap-lg mb-2xl">
          <BaseCard elevated>
            <div class="stat-card">
              <div class="stat-icon bg-primary">🏠</div>
              <div class="stat-content">
                <p class="stat-label">Total Properties</p>
                <p class="stat-value">{{ stats?.properties?.total || 0 }}</p>
                <p class="stat-subtext text-success">
                  {{ stats?.properties?.available || 0 }} available
                </p>
              </div>
            </div>
          </BaseCard>

          <BaseCard elevated>
            <div class="stat-card">
              <div class="stat-icon bg-secondary">👥</div>
              <div class="stat-content">
                <p class="stat-label">Total Clients</p>
                <p class="stat-value">{{ stats?.clients?.total || 0 }}</p>
                <p class="stat-subtext text-info">
                  {{ stats?.clients?.verified || 0 }} verified
                </p>
              </div>
            </div>
          </BaseCard>

          <BaseCard elevated>
            <div class="stat-card">
              <div class="stat-icon bg-success">📄</div>
              <div class="stat-content">
                <p class="stat-label">Active Contracts</p>
                <p class="stat-value">{{ stats?.contracts?.active || 0 }}</p>
                <p class="stat-subtext text-tertiary">
                  {{ stats?.contracts?.total || 0 }} total
                </p>
              </div>
            </div>
          </BaseCard>

          <BaseCard elevated>
            <div class="stat-card">
              <div class="stat-icon bg-warning">💰</div>
              <div class="stat-content">
                <p class="stat-label">Total Revenue</p>
                <p class="stat-value">₽{{ formatMoney(stats?.revenue?.total || 0) }}</p>
                <p class="stat-subtext text-success">This month</p>
              </div>
            </div>
          </BaseCard>
        </div>

        <!-- Recent Activity -->
        <BaseCard title="Recent Activity" class="mb-xl">
          <div class="activity-list">
            <div class="activity-item">
              <span class="badge badge-primary">New</span>
              <p class="text-secondary">New application from Client #123</p>
              <span class="text-tertiary text-sm">2 hours ago</span>
            </div>
            <div class="activity-item">
              <span class="badge badge-success">Approved</span>
              <p class="text-secondary">Contract #456 has been signed</p>
              <span class="text-tertiary text-sm">5 hours ago</span>
            </div>
            <div class="activity-item">
              <span class="badge badge-warning">Pending</span>
              <p class="text-secondary">Payment #789 awaiting confirmation</p>
              <span class="text-tertiary text-sm">1 day ago</span>
            </div>
          </div>
        </BaseCard>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useAdminStore } from '@/stores/admin'
import BaseCard from '@/components/common/BaseCard.vue'
import BaseButton from '@/components/common/BaseButton.vue'

const router = useRouter()
const authStore = useAuthStore()
const adminStore = useAdminStore()

const stats = ref(null)

onMounted(async () => {
  try {
    stats.value = await adminStore.fetchStatistics()
  } catch (error) {
    console.error('Failed to fetch statistics:', error)
  }
})

const handleLogout = () => {
  authStore.logout()
  router.push('/')
}

const formatMoney = (value) => {
  return new Intl.NumberFormat('ru-RU').format(value)
}
</script>

<style scoped>
.dashboard-page {
  min-height: 100vh;
  background: var(--bg-primary);
}

.sidebar-nav {
  padding: var(--spacing-lg);
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xs);
}

.sidebar-link {
  padding: var(--spacing-md);
  border-radius: var(--radius-md);
  color: var(--text-secondary);
  transition: all var(--transition-fast);
  font-weight: var(--font-weight-medium);
}

.sidebar-link:hover,
.sidebar-link.active {
  background: var(--bg-tertiary);
  color: var(--text-primary);
}

.stat-card {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
}

.stat-icon {
  width: 60px;
  height: 60px;
  border-radius: var(--radius-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
}

.stat-icon.bg-primary {
  background: rgba(59, 130, 246, 0.2);
}

.stat-icon.bg-secondary {
  background: rgba(6, 182, 212, 0.2);
}

.stat-icon.bg-success {
  background: rgba(16, 185, 129, 0.2);
}

.stat-icon.bg-warning {
  background: rgba(245, 158, 11, 0.2);
}

.stat-content {
  flex: 1;
}

.stat-label {
  font-size: var(--font-size-sm);
  color: var(--text-tertiary);
  margin-bottom: var(--spacing-xs);
}

.stat-value {
  font-size: var(--font-size-2xl);
  font-weight: var(--font-weight-bold);
  color: var(--text-primary);
  margin-bottom: var(--spacing-xs);
}

.stat-subtext {
  font-size: var(--font-size-sm);
}

.activity-list {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
}

.activity-item {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
  padding: var(--spacing-md);
  background: var(--bg-tertiary);
  border-radius: var(--radius-md);
}

.activity-item p {
  flex: 1;
  margin: 0;
}
</style>
