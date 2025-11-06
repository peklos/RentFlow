<template>
  <div class="clients-manage">
    <div class="page-header">
      <div>
        <h1>Clients Management</h1>
        <p class="subtitle">View and manage client information</p>
      </div>
    </div>

    <!-- Stats -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-label">Total Clients</div>
        <div class="stat-value">{{ clients.length }}</div>
      </div>
      <div class="stat-card verified">
        <div class="stat-label">Verified Clients</div>
        <div class="stat-value">{{ stats.verified }}</div>
      </div>
      <div class="stat-card active">
        <div class="stat-label">With Active Contracts</div>
        <div class="stat-value">{{ stats.withContracts }}</div>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="loading-state">
      <div class="spinner"></div>
      <p>Loading clients...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="error-state">
      <p>{{ error }}</p>
      <BaseButton @click="loadClients">Retry</BaseButton>
    </div>

    <!-- Clients List -->
    <div v-else-if="clients.length > 0" class="clients-list">
      <BaseCard v-for="client in clients" :key="client.id" elevated class="client-card">
        <div class="client-header">
          <div class="client-avatar">
            <span class="avatar-icon">👤</span>
          </div>
          <div class="client-main-info">
            <h3>{{ client.full_name }}</h3>
            <p class="client-type">{{ client.type === 'individual' ? 'Individual' : 'Company' }}</p>
          </div>
          <span v-if="client.is_verified" class="verified-badge" title="Verified">
            ✓ Verified
          </span>
        </div>

        <div class="client-details">
          <div class="detail-section">
            <h4>Contact Information</h4>
            <div class="detail-grid">
              <div class="detail-row">
                <span class="label">Phone:</span>
                <span class="value">{{ client.phone || 'N/A' }}</span>
              </div>
              <div class="detail-row">
                <span class="label">Email:</span>
                <span class="value">{{ client.email || 'N/A' }}</span>
              </div>
              <div class="detail-row">
                <span class="label">Address:</span>
                <span class="value">{{ client.address || 'N/A' }}</span>
              </div>
            </div>
          </div>

          <div v-if="client.type === 'individual'" class="detail-section">
            <h4>Personal Information</h4>
            <div class="detail-grid">
              <div class="detail-row">
                <span class="label">Date of Birth:</span>
                <span class="value">{{ formatDate(client.date_of_birth) }}</span>
              </div>
              <div class="detail-row">
                <span class="label">Passport:</span>
                <span class="value">{{ client.passport_series_number || 'N/A' }}</span>
              </div>
              <div class="detail-row">
                <span class="label">INN:</span>
                <span class="value">{{ client.inn || 'N/A' }}</span>
              </div>
            </div>
          </div>

          <div v-if="client.type === 'company'" class="detail-section">
            <h4>Company Information</h4>
            <div class="detail-grid">
              <div class="detail-row">
                <span class="label">Company Name:</span>
                <span class="value">{{ client.company_name || 'N/A' }}</span>
              </div>
              <div class="detail-row">
                <span class="label">INN:</span>
                <span class="value">{{ client.inn || 'N/A' }}</span>
              </div>
              <div class="detail-row">
                <span class="label">KPP:</span>
                <span class="value">{{ client.kpp || 'N/A' }}</span>
              </div>
            </div>
          </div>

          <div class="detail-section">
            <h4>System Information</h4>
            <div class="detail-grid">
              <div class="detail-row">
                <span class="label">Client ID:</span>
                <span class="value">#{{ client.id }}</span>
              </div>
              <div class="detail-row">
                <span class="label">Registered:</span>
                <span class="value">{{ formatDate(client.created_at) }}</span>
              </div>
              <div class="detail-row">
                <span class="label">Verification:</span>
                <span :class="['value', client.is_verified ? 'verified' : 'not-verified']">
                  {{ client.is_verified ? 'Verified' : 'Not Verified' }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <div class="client-actions">
          <BaseButton variant="secondary" size="small" @click="viewClientDetails(client.id)">
            View Full Profile
          </BaseButton>
        </div>
      </BaseCard>
    </div>

    <!-- Empty State -->
    <div v-else class="empty-state">
      <p>No clients found</p>
      <p class="text-secondary">Clients will appear here when they register</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { adminAPI } from '@/api/services/admin'
import BaseCard from '@/components/common/BaseCard.vue'
import BaseButton from '@/components/common/BaseButton.vue'

const clients = ref([])
const loading = ref(true)
const error = ref(null)

const stats = computed(() => {
  return {
    verified: clients.value.filter(c => c.is_verified).length,
    withContracts: clients.value.filter(c => c.has_active_contract).length
  }
})

const loadClients = async () => {
  loading.value = true
  error.value = null
  try {
    const response = await adminAPI.getClients()
    clients.value = response.data
  } catch (err) {
    error.value = err.response?.data?.detail || 'Failed to load clients'
    console.error('Error loading clients:', err)
  } finally {
    loading.value = false
  }
}

const viewClientDetails = (clientId) => {
  // This could navigate to a detailed client page or open a modal
  console.log('View client details:', clientId)
  alert(`Client details view for ID: ${clientId}\n\nThis feature can be expanded to show more detailed information, contracts, applications, and payment history.`)
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
  loadClients()
})
</script>

<style scoped>
.clients-manage {
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

/* Stats */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: var(--bg-secondary);
  padding: 1.5rem;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.stat-card.verified {
  border-color: rgba(34, 197, 94, 0.3);
}

.stat-card.active {
  border-color: rgba(59, 130, 246, 0.3);
}

.stat-label {
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin-bottom: 0.5rem;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: var(--text-primary);
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

/* Clients List */
.clients-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.client-card {
  transition: transform 0.3s ease;
}

.client-card:hover {
  transform: translateY(-2px);
}

.client-header {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.client-avatar {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
}

.client-main-info {
  flex: 1;
}

.client-main-info h3 {
  font-size: 1.5rem;
  color: var(--text-primary);
  margin-bottom: 0.25rem;
}

.client-type {
  color: var(--text-secondary);
  font-size: 0.875rem;
  margin: 0;
}

.verified-badge {
  padding: 0.5rem 1rem;
  background: rgba(34, 197, 94, 0.15);
  color: #22c55e;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 600;
}

/* Client Details */
.client-details {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  margin-bottom: 1.5rem;
}

.detail-section h4 {
  font-size: 1rem;
  color: var(--text-primary);
  margin-bottom: 1rem;
  font-weight: 600;
}

.detail-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}

.detail-row {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
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

.detail-row .value.verified {
  color: #22c55e;
  font-weight: 600;
}

.detail-row .value.not-verified {
  color: #facc15;
}

/* Actions */
.client-actions {
  display: flex;
  gap: 1rem;
}

/* Responsive */
@media (max-width: 768px) {
  .clients-manage {
    padding: 1rem;
  }

  .client-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .verified-badge {
    align-self: flex-start;
  }

  .detail-grid {
    grid-template-columns: 1fr;
  }
}
</style>
