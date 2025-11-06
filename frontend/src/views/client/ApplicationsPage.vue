<template>
  <div>
    <AppHeader />
    <div class="applications-page">
      <div class="container">
        <div class="page-header">
          <h1>Мои Заявки</h1>
          <p class="subtitle">Отслеживайте статус ваших заявок на аренду</p>
        </div>

        <!-- Summary Stats -->
        <div class="stats-summary">
          <div class="stat-box pending">
            <div class="stat-icon">⏳</div>
            <div class="stat-content">
              <div class="stat-value">{{ stats.pending }}</div>
              <div class="stat-label">В ожидании</div>
            </div>
          </div>
          <div class="stat-box approved">
            <div class="stat-icon">✓</div>
            <div class="stat-content">
              <div class="stat-value">{{ stats.approved }}</div>
              <div class="stat-label">Одобрено</div>
            </div>
          </div>
          <div class="stat-box rejected">
            <div class="stat-icon">✗</div>
            <div class="stat-content">
              <div class="stat-value">{{ stats.rejected }}</div>
              <div class="stat-label">Отклонено</div>
            </div>
          </div>
        </div>

        <!-- Loading State -->
        <div v-if="loading" class="loading-state">
          <div class="spinner"></div>
          <p>Загрузка заявок...</p>
        </div>

        <!-- Error State -->
        <div v-else-if="error" class="error-state">
          <BaseCard elevated>
            <p class="error-message">{{ error }}</p>
            <BaseButton @click="loadApplications" variant="primary">Повторить</BaseButton>
          </BaseCard>
        </div>

        <!-- Applications List -->
        <div v-else-if="applications.length > 0" class="applications-list">
          <BaseCard v-for="application in applications" :key="application.id" elevated class="application-card">
            <!-- Application Header -->
            <div class="application-header">
              <div class="application-number">
                <h3>Заявка №{{ application.id }}</h3>
                <span class="application-date">
                  Подана {{ formatDate(application.application_date) }}
                </span>
              </div>
              <span :class="['status-badge', application.status]">
                {{ getStatusText(application.status) }}
              </span>
            </div>

            <!-- Property Info -->
            <div class="property-info">
              <div class="property-icon">🏢</div>
              <div class="property-details">
                <h4>Детали объекта</h4>
                <p class="property-id">ID объекта: #{{ application.property_id }}</p>
              </div>
            </div>

            <!-- Application Details -->
            <div class="application-details">
              <div class="detail-item">
                <span class="detail-label">Дата заселения</span>
                <span class="detail-value">{{ formatDate(application.preferred_move_in_date) }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Срок аренды</span>
                <span class="detail-value">{{ application.lease_duration_months }} мес</span>
              </div>
              <div v-if="application.notes" class="detail-item full-width">
                <span class="detail-label">Дополнительные заметки</span>
                <span class="detail-value">{{ application.notes }}</span>
              </div>
            </div>

            <!-- Status Message -->
            <div v-if="application.status === 'pending'" class="status-message pending">
              <p>⏳ Ваша заявка рассматривается. Мы уведомим вас, когда она будет обработана.</p>
            </div>
            <div v-else-if="application.status === 'approved'" class="status-message approved">
              <p>✓ Поздравляем! Ваша заявка одобрена. Наша команда свяжется с вами в ближайшее время.</p>
            </div>
            <div v-else-if="application.status === 'rejected'" class="status-message rejected">
              <p>✗ К сожалению, эта заявка не была одобрена. Вы можете подать заявку на другие объекты.</p>
            </div>
          </BaseCard>
        </div>

        <!-- Empty State -->
        <div v-else class="empty-state">
          <BaseCard elevated>
            <div class="empty-content">
              <div class="empty-icon">📝</div>
              <h3>Пока нет заявок</h3>
              <p>Вы еще не подали ни одной заявки на аренду. Просмотрите доступные объекты и подайте заявку!</p>
              <BaseButton variant="primary" @click="goToProperties">
                Смотреть объекты
              </BaseButton>
            </div>
          </BaseCard>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { applicationsAPI } from '@/api/services/applications'
import AppHeader from '@/components/layout/AppHeader.vue'
import BaseCard from '@/components/common/BaseCard.vue'
import BaseButton from '@/components/common/BaseButton.vue'

const router = useRouter()
const authStore = useAuthStore()

const applications = ref([])
const loading = ref(true)
const error = ref(null)

const stats = computed(() => {
  return {
    pending: applications.value.filter(a => a.status === 'pending').length,
    approved: applications.value.filter(a => a.status === 'approved').length,
    rejected: applications.value.filter(a => a.status === 'rejected').length
  }
})

const loadApplications = async () => {
  loading.value = true
  error.value = null
  try {
    const response = await applicationsAPI.getAll()
    applications.value = response.data

    // If user is logged in, filter by their client_id
    if (authStore.user && authStore.user.id) {
      applications.value = applications.value.filter(a => a.client_id === authStore.user.id)
    }
  } catch (err) {
    error.value = err.response?.data?.detail || 'Failed to load applications'
    console.error('Error loading applications:', err)
  } finally {
    loading.value = false
  }
}

const getStatusText = (status) => {
  const statusMap = {
    pending: 'На рассмотрении',
    approved: 'Одобрено',
    rejected: 'Отклонено'
  }
  return statusMap[status] || status
}

const formatDate = (dateString) => {
  if (!dateString) return 'Н/Д'
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

const goToProperties = () => {
  router.push('/properties')
}

onMounted(() => {
  loadApplications()
})
</script>

<style scoped>
.applications-page {
  min-height: 100vh;
  padding: 2rem 0;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.page-header {
  margin-bottom: 2rem;
}

.page-header h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
  color: var(--text-primary);
  font-weight: 700;
}

.subtitle {
  color: var(--text-secondary);
  font-size: 1.125rem;
}

/* Stats Summary */
.stats-summary {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-box {
  background: var(--bg-secondary);
  border-radius: 12px;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  border: 2px solid rgba(255, 255, 255, 0.1);
  transition: transform 0.3s ease;
}

.stat-box:hover {
  transform: translateY(-2px);
}

.stat-box.pending {
  border-color: rgba(250, 204, 21, 0.3);
}

.stat-box.approved {
  border-color: rgba(34, 197, 94, 0.3);
}

.stat-box.rejected {
  border-color: rgba(239, 68, 68, 0.3);
}

.stat-icon {
  font-size: 2.5rem;
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
}

.stat-content {
  flex: 1;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1;
  margin-bottom: 0.25rem;
}

.stat-label {
  font-size: 0.875rem;
  color: var(--text-secondary);
  font-weight: 500;
}

/* Loading & Error States */
.loading-state,
.error-state {
  text-align: center;
  padding: 4rem 2rem;
}

.loading-state {
  color: var(--text-secondary);
}

.spinner {
  width: 50px;
  height: 50px;
  margin: 0 auto 1rem;
  border: 3px solid var(--bg-tertiary);
  border-top-color: var(--primary-color);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-message {
  color: #ef4444;
  margin-bottom: 1rem;
  font-size: 1.125rem;
}

/* Applications List */
.applications-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.application-card {
  transition: transform 0.3s ease;
}

.application-card:hover {
  transform: translateY(-2px);
}

.application-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.application-number h3 {
  font-size: 1.5rem;
  color: var(--text-primary);
  margin-bottom: 0.25rem;
}

.application-date {
  font-size: 0.875rem;
  color: var(--text-secondary);
}

.status-badge {
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.status-badge.pending {
  background: rgba(250, 204, 21, 0.15);
  color: #facc15;
}

.status-badge.approved {
  background: rgba(34, 197, 94, 0.15);
  color: #22c55e;
}

.status-badge.rejected {
  background: rgba(239, 68, 68, 0.15);
  color: #ef4444;
}

/* Property Info */
.property-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.03);
  border-radius: 8px;
  margin-bottom: 1.5rem;
}

.property-icon {
  font-size: 2rem;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--primary-glow);
  border-radius: 8px;
}

.property-details h4 {
  font-size: 1rem;
  color: var(--text-primary);
  margin-bottom: 0.25rem;
}

.property-id {
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin: 0;
}

/* Application Details */
.application-details {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.detail-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.detail-item.full-width {
  grid-column: 1 / -1;
}

.detail-label {
  font-size: 0.875rem;
  color: var(--text-secondary);
  font-weight: 500;
}

.detail-value {
  font-size: 1rem;
  color: var(--text-primary);
  font-weight: 600;
}

/* Status Messages */
.status-message {
  padding: 1rem;
  border-radius: 8px;
  font-size: 0.875rem;
  line-height: 1.5;
}

.status-message.pending {
  background: rgba(250, 204, 21, 0.1);
  color: #facc15;
  border: 1px solid rgba(250, 204, 21, 0.3);
}

.status-message.approved {
  background: rgba(34, 197, 94, 0.1);
  color: #22c55e;
  border: 1px solid rgba(34, 197, 94, 0.3);
}

.status-message.rejected {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  border: 1px solid rgba(239, 68, 68, 0.3);
}

.status-message p {
  margin: 0;
}

/* Empty State */
.empty-state {
  margin-top: 2rem;
}

.empty-content {
  text-align: center;
  padding: 4rem 2rem;
}

.empty-icon {
  font-size: 5rem;
  margin-bottom: 1.5rem;
  opacity: 0.5;
}

.empty-content h3 {
  font-size: 1.5rem;
  color: var(--text-primary);
  margin-bottom: 1rem;
}

.empty-content p {
  color: var(--text-secondary);
  margin-bottom: 2rem;
  font-size: 1.125rem;
}

/* Responsive */
@media (max-width: 768px) {
  .page-header h1 {
    font-size: 2rem;
  }

  .application-header {
    flex-direction: column;
    gap: 1rem;
  }

  .status-badge {
    align-self: flex-start;
  }

  .application-details {
    grid-template-columns: 1fr;
  }

  .stats-summary {
    grid-template-columns: 1fr;
  }
}
</style>
