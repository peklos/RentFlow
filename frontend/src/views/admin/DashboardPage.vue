<template>
  <AdminLayout>
    <div class="dashboard-content">
      <h1 class="page-title">Обзор</h1>

      <!-- Statistics Cards -->
      <div class="stats-grid">
        <BaseCard elevated>
          <div class="stat-card">
            <div class="stat-icon bg-primary">🏠</div>
            <div class="stat-content">
              <p class="stat-label">Всего объектов</p>
              <p class="stat-value">{{ stats?.properties?.total || 0 }}</p>
              <p class="stat-subtext text-success">
                {{ stats?.properties?.available || 0 }} доступно
              </p>
            </div>
          </div>
        </BaseCard>

        <BaseCard elevated>
          <div class="stat-card">
            <div class="stat-icon bg-secondary">👥</div>
            <div class="stat-content">
              <p class="stat-label">Всего клиентов</p>
              <p class="stat-value">{{ stats?.clients?.total || 0 }}</p>
              <p class="stat-subtext text-info">
                {{ stats?.clients?.verified || 0 }} подтверждено
              </p>
            </div>
          </div>
        </BaseCard>

        <BaseCard elevated>
          <div class="stat-card">
            <div class="stat-icon bg-success">📄</div>
            <div class="stat-content">
              <p class="stat-label">Активные договоры</p>
              <p class="stat-value">{{ stats?.contracts?.active || 0 }}</p>
              <p class="stat-subtext text-tertiary">
                {{ stats?.contracts?.total || 0 }} всего
              </p>
            </div>
          </div>
        </BaseCard>

        <BaseCard elevated>
          <div class="stat-card">
            <div class="stat-icon bg-warning">💰</div>
            <div class="stat-content">
              <p class="stat-label">Общий доход</p>
              <p class="stat-value">₽{{ formatMoney(stats?.revenue?.total || 0) }}</p>
              <p class="stat-subtext text-success">За месяц</p>
            </div>
          </div>
        </BaseCard>
      </div>

      <!-- Recent Activity -->
      <BaseCard title="Недавняя активность" class="activity-card">
        <div class="activity-list">
          <div class="activity-item">
            <span class="badge badge-primary">Новое</span>
            <p class="text-secondary">Новая заявка от клиента №123</p>
            <span class="text-tertiary text-sm">2 ч назад</span>
          </div>
          <div class="activity-item">
            <span class="badge badge-success">Одобрено</span>
            <p class="text-secondary">Договор №456 подписан</p>
            <span class="text-tertiary text-sm">5 ч назад</span>
          </div>
          <div class="activity-item">
            <span class="badge badge-warning">Ожидание</span>
            <p class="text-secondary">Платеж №789 ожидает подтверждения</p>
            <span class="text-tertiary text-sm">1 д назад</span>
          </div>
        </div>
      </BaseCard>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAdminStore } from '@/stores/admin'
import AdminLayout from '@/components/layout/AdminLayout.vue'
import BaseCard from '@/components/common/BaseCard.vue'

const adminStore = useAdminStore()
const stats = ref(null)

onMounted(async () => {
  try {
    stats.value = await adminStore.fetchStatistics()
  } catch (error) {
    console.error('Failed to fetch statistics:', error)
  }
})

const formatMoney = (value) => {
  return new Intl.NumberFormat('ru-RU').format(value)
}
</script>

<style scoped>
.dashboard-content {
  max-width: 1400px;
  margin: 0 auto;
}

.page-title {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 2rem;
  color: var(--text-primary);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.stat-icon {
  width: 60px;
  height: 60px;
  border-radius: 12px;
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
  font-size: 0.875rem;
  color: var(--text-tertiary);
  margin-bottom: 0.5rem;
}

.stat-value {
  font-size: 1.875rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.25rem;
}

.stat-subtext {
  font-size: 0.875rem;
}

.text-success {
  color: #10b981;
}

.text-info {
  color: #06b6d4;
}

.text-tertiary {
  color: var(--text-tertiary);
}

.activity-card {
  margin-top: 2rem;
}

.activity-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.activity-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: var(--bg-tertiary);
  border-radius: 8px;
}

.activity-item p {
  flex: 1;
  margin: 0;
  color: var(--text-secondary);
}

.badge {
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  white-space: nowrap;
}

.badge-primary {
  background: rgba(59, 130, 246, 0.2);
  color: #3b82f6;
}

.badge-success {
  background: rgba(16, 185, 129, 0.2);
  color: #10b981;
}

.badge-warning {
  background: rgba(245, 158, 11, 0.2);
  color: #f59e0b;
}

.text-sm {
  font-size: 0.875rem;
}

@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: 1fr;
  }

  .page-title {
    font-size: 1.5rem;
  }
}
</style>
