<template>
  <div class="applications-manage">
    <div class="page-header">
      <h1>Управление заявками</h1>
      <p class="subtitle">Просмотр и управление заявками на аренду</p>
    </div>

    <!-- Filters -->
    <div class="filters-section">
      <BaseCard>
        <div class="filters">
          <div class="filter-group">
            <label>Фильтр по статусу</label>
            <select v-model="filters.status" @change="loadApplications" class="filter-select">
              <option value="">Все статусы</option>
              <option value="pending">В ожидании</option>
              <option value="approved">Одобрено</option>
              <option value="rejected">Отклонено</option>
            </select>
          </div>
          <div class="filter-stats">
            <span class="stat-badge pending">В ожидании: {{ stats.pending }}</span>
            <span class="stat-badge approved">Одобрено: {{ stats.approved }}</span>
            <span class="stat-badge rejected">Отклонено: {{ stats.rejected }}</span>
          </div>
        </div>
      </BaseCard>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="loading-state">
      <div class="spinner"></div>
      <p>Загрузка заявок...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="error-state">
      <p>{{ error }}</p>
      <BaseButton @click="loadApplications">Повторить</BaseButton>
    </div>

    <!-- Applications List -->
    <div v-else-if="applications.length > 0" class="applications-list">
      <BaseCard v-for="application in applications" :key="application.id" elevated class="application-card">
        <div class="application-header">
          <div class="application-info">
            <h3>Application #{{ application.id }}</h3>
            <span :class="['status-badge', application.status]">
              {{ application.status }}
            </span>
          </div>
          <div class="application-date">
            {{ formatDate(application.application_date) }}
          </div>
        </div>

        <div class="application-details">
          <div class="detail-row">
            <span class="label">Client ID:</span>
            <span class="value">{{ application.client_id }}</span>
          </div>
          <div class="detail-row">
            <span class="label">Property ID:</span>
            <span class="value">{{ application.property_id }}</span>
          </div>
          <div class="detail-row">
            <span class="label">Move-in Date:</span>
            <span class="value">{{ formatDate(application.preferred_move_in_date) }}</span>
          </div>
          <div class="detail-row">
            <span class="label">Lease Duration:</span>
            <span class="value">{{ application.lease_duration_months }} months</span>
          </div>
          <div v-if="application.notes" class="detail-row full-width">
            <span class="label">Notes:</span>
            <span class="value">{{ application.notes }}</span>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="application-actions">
          <BaseButton
            v-if="application.status === 'pending'"
            variant="success"
            @click="updateApplicationStatus(application.id, 'approved')"
            :disabled="updatingId === application.id"
          >
            Approve
          </BaseButton>
          <BaseButton
            v-if="application.status === 'pending'"
            variant="danger"
            @click="updateApplicationStatus(application.id, 'rejected')"
            :disabled="updatingId === application.id"
          >
            Reject
          </BaseButton>
          <BaseButton
            v-if="application.status !== 'pending'"
            variant="secondary"
            @click="updateApplicationStatus(application.id, 'pending')"
            :disabled="updatingId === application.id"
          >
            Reset to Pending
          </BaseButton>
        </div>
      </BaseCard>
    </div>

    <!-- Empty State -->
    <div v-else class="empty-state">
      <p>No applications found</p>
      <p class="text-secondary">Applications will appear here when clients submit them</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { applicationsAPI } from '@/api/services/applications'
import BaseCard from '@/components/common/BaseCard.vue'
import BaseButton from '@/components/common/BaseButton.vue'

const applications = ref([])
const loading = ref(true)
const error = ref(null)
const filters = ref({
  status: ''
})
const updatingId = ref(null)

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
    const response = await applicationsAPI.getAllAdmin(filters.value)
    applications.value = response.data
  } catch (err) {
    error.value = err.response?.data?.detail || 'Failed to load applications'
    console.error('Error loading applications:', err)
  } finally {
    loading.value = false
  }
}

const updateApplicationStatus = async (id, status) => {
  updatingId.value = id
  try {
    await applicationsAPI.update(id, { status })

    // Update local state
    const application = applications.value.find(a => a.id === id)
    if (application) {
      application.status = status
    }
  } catch (err) {
    error.value = err.response?.data?.detail || 'Failed to update application'
    console.error('Error updating application:', err)
  } finally {
    updatingId.value = null
  }
}

const formatDate = (dateString) => {
  if (!dateString) return 'N/A'
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

onMounted(() => {
  loadApplications()
})
</script>

<style scoped>
.applications-manage {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.page-header {
  margin-bottom: 2rem;
}

.page-header h1 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  color: var(--text-primary);
}

.subtitle {
  color: var(--text-secondary);
  font-size: 1rem;
}

/* Filters */
.filters-section {
  margin-bottom: 2rem;
}

.filters {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.filter-group label {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--text-secondary);
}

.filter-select {
  padding: 0.625rem 1rem;
  background: var(--bg-tertiary);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  color: var(--text-primary);
  font-size: 1rem;
  min-width: 200px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.filter-select:hover {
  border-color: var(--primary-color);
}

.filter-select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px var(--primary-glow);
}

.filter-stats {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.stat-badge {
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 600;
}

.stat-badge.pending {
  background: rgba(250, 204, 21, 0.1);
  color: #facc15;
}

.stat-badge.approved {
  background: rgba(34, 197, 94, 0.1);
  color: #22c55e;
}

.stat-badge.rejected {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
}

/* Loading & Error States */
.loading-state,
.error-state,
.empty-state {
  text-align: center;
  padding: 4rem 2rem;
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
  align-items: center;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.application-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.application-info h3 {
  font-size: 1.25rem;
  color: var(--text-primary);
  margin: 0;
}

.status-badge {
  padding: 0.375rem 0.875rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: capitalize;
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

.application-date {
  color: var(--text-secondary);
  font-size: 0.875rem;
}

/* Application Details */
.application-details {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.detail-row {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.detail-row.full-width {
  grid-column: 1 / -1;
}

.detail-row .label {
  font-size: 0.875rem;
  color: var(--text-secondary);
  font-weight: 500;
}

.detail-row .value {
  color: var(--text-primary);
  font-size: 1rem;
}

/* Actions */
.application-actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

/* Responsive */
@media (max-width: 768px) {
  .applications-manage {
    padding: 1rem;
  }

  .filters {
    flex-direction: column;
    align-items: stretch;
  }

  .filter-select {
    min-width: 100%;
  }

  .application-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }

  .application-details {
    grid-template-columns: 1fr;
  }
}
</style>
