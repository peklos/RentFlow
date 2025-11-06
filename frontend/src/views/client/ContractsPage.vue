<template>
  <div>
    <AppHeader />
    <div class="contracts-page">
      <div class="container">
        <div class="page-header">
          <h1>My Contracts</h1>
          <p class="subtitle">View your rental contracts and payment history</p>
        </div>

        <!-- Loading State -->
        <div v-if="loading" class="loading-state">
          <div class="spinner"></div>
          <p>Loading your contracts...</p>
        </div>

        <!-- Error State -->
        <div v-else-if="error" class="error-state">
          <BaseCard elevated>
            <p class="error-message">{{ error }}</p>
            <BaseButton @click="loadContracts" variant="primary">Retry</BaseButton>
          </BaseCard>
        </div>

        <!-- Contracts List -->
        <div v-else-if="contracts.length > 0" class="contracts-list">
          <BaseCard v-for="contract in contracts" :key="contract.id" elevated class="contract-card">
            <!-- Contract Header -->
            <div class="contract-header">
              <div class="contract-info">
                <h3>Contract #{{ contract.id }}</h3>
                <p class="contract-dates">
                  {{ formatDate(contract.start_date) }} - {{ formatDate(contract.end_date) }}
                </p>
              </div>
              <span :class="['status-badge', contract.status]">
                {{ getStatusText(contract.status) }}
              </span>
            </div>

            <!-- Property Info -->
            <div class="property-section">
              <div class="section-title">
                <span class="icon">🏢</span>
                <h4>Property Details</h4>
              </div>
              <div class="property-id">Property ID: #{{ contract.property_id }}</div>
            </div>

            <!-- Contract Details -->
            <div class="contract-details">
              <div class="detail-item">
                <span class="detail-label">Monthly Rent</span>
                <span class="detail-value price">{{ formatPrice(contract.monthly_rent) }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Security Deposit</span>
                <span class="detail-value price">{{ formatPrice(contract.security_deposit) }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Payment Day</span>
                <span class="detail-value">Day {{ contract.payment_day }} of each month</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Contract Duration</span>
                <span class="detail-value">{{ calculateDuration(contract.start_date, contract.end_date) }}</span>
              </div>
            </div>

            <!-- Payment Status -->
            <div v-if="contract.status === 'active'" class="payment-reminder">
              <div class="reminder-icon">💳</div>
              <div class="reminder-content">
                <h5>Next Payment Due</h5>
                <p>{{ getNextPaymentDate(contract.payment_day) }}</p>
              </div>
            </div>

            <!-- Special Conditions -->
            <div v-if="contract.special_conditions" class="special-conditions">
              <h5>Special Conditions</h5>
              <p>{{ contract.special_conditions }}</p>
            </div>

            <!-- Actions -->
            <div class="contract-actions">
              <BaseButton variant="secondary" size="small" @click="viewContractDetails(contract.id)">
                View Full Contract
              </BaseButton>
              <BaseButton v-if="contract.status === 'active'" variant="primary" size="small">
                Make Payment
              </BaseButton>
            </div>
          </BaseCard>
        </div>

        <!-- Empty State -->
        <div v-else class="empty-state">
          <BaseCard elevated>
            <div class="empty-content">
              <div class="empty-icon">📄</div>
              <h3>No Contracts Yet</h3>
              <p>You don't have any rental contracts yet. Once your application is approved and a contract is created, it will appear here.</p>
              <BaseButton variant="primary" @click="goToApplications">
                View My Applications
              </BaseButton>
            </div>
          </BaseCard>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { contractsAPI } from '@/api/services/contracts'
import AppHeader from '@/components/layout/AppHeader.vue'
import BaseCard from '@/components/common/BaseCard.vue'
import BaseButton from '@/components/common/BaseButton.vue'

const router = useRouter()
const authStore = useAuthStore()

const contracts = ref([])
const loading = ref(true)
const error = ref(null)

const loadContracts = async () => {
  loading.value = true
  error.value = null
  try {
    const response = await contractsAPI.getAll()
    contracts.value = response.data

    // If user is logged in, filter by their client_id
    if (authStore.user && authStore.user.id) {
      contracts.value = contracts.value.filter(c => c.client_id === authStore.user.id)
    }
  } catch (err) {
    error.value = err.response?.data?.detail || 'Failed to load contracts'
    console.error('Error loading contracts:', err)
  } finally {
    loading.value = false
  }
}

const getStatusText = (status) => {
  const statusMap = {
    active: 'Active',
    completed: 'Completed',
    terminated: 'Terminated'
  }
  return statusMap[status] || status
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

const formatPrice = (price) => {
  return new Intl.NumberFormat('ru-RU', {
    style: 'currency',
    currency: 'RUB',
    maximumFractionDigits: 0
  }).format(price)
}

const calculateDuration = (startDate, endDate) => {
  const start = new Date(startDate)
  const end = new Date(endDate)
  const months = Math.round((end - start) / (1000 * 60 * 60 * 24 * 30))
  return `${months} months`
}

const getNextPaymentDate = (paymentDay) => {
  const today = new Date()
  const currentMonth = today.getMonth()
  const currentYear = today.getFullYear()

  let nextPayment = new Date(currentYear, currentMonth, paymentDay)

  if (nextPayment < today) {
    nextPayment = new Date(currentYear, currentMonth + 1, paymentDay)
  }

  return formatDate(nextPayment)
}

const viewContractDetails = (contractId) => {
  console.log('View contract details:', contractId)
  alert(`Contract details for ID: ${contractId}\n\nThis would open a detailed view with full contract terms, payment history, and documents.`)
}

const goToApplications = () => {
  router.push('/applications')
}

onMounted(() => {
  loadContracts()
})
</script>

<style scoped>
.contracts-page {
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

/* Contracts List */
.contracts-list {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.contract-card {
  transition: transform 0.3s ease;
}

.contract-card:hover {
  transform: translateY(-2px);
}

.contract-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid rgba(255, 255, 255, 0.1);
}

.contract-info h3 {
  font-size: 1.75rem;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
  font-weight: 700;
}

.contract-dates {
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin: 0;
}

.status-badge {
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.status-badge.active {
  background: rgba(34, 197, 94, 0.15);
  color: #22c55e;
}

.status-badge.completed {
  background: rgba(59, 130, 246, 0.15);
  color: #3b82f6;
}

.status-badge.terminated {
  background: rgba(239, 68, 68, 0.15);
  color: #ef4444;
}

/* Property Section */
.property-section {
  padding: 1rem;
  background: rgba(255, 255, 255, 0.03);
  border-radius: 8px;
  margin-bottom: 1.5rem;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.75rem;
}

.section-title .icon {
  font-size: 1.5rem;
}

.section-title h4 {
  font-size: 1.125rem;
  color: var(--text-primary);
  margin: 0;
  font-weight: 600;
}

.property-id {
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin-left: 2.25rem;
}

/* Contract Details */
.contract-details {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.detail-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
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

.detail-value.price {
  font-size: 1.25rem;
  color: var(--primary-color);
  font-weight: 700;
}

/* Payment Reminder */
.payment-reminder {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.25rem;
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(37, 99, 235, 0.05) 100%);
  border: 1px solid rgba(59, 130, 246, 0.3);
  border-radius: 12px;
  margin-bottom: 1.5rem;
}

.reminder-icon {
  font-size: 2.5rem;
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(59, 130, 246, 0.15);
  border-radius: 50%;
}

.reminder-content h5 {
  font-size: 1rem;
  color: var(--text-primary);
  margin: 0 0 0.25rem 0;
  font-weight: 600;
}

.reminder-content p {
  font-size: 1.125rem;
  color: var(--primary-color);
  margin: 0;
  font-weight: 700;
}

/* Special Conditions */
.special-conditions {
  padding: 1.25rem;
  background: rgba(250, 204, 21, 0.1);
  border: 1px solid rgba(250, 204, 21, 0.3);
  border-radius: 8px;
  margin-bottom: 1.5rem;
}

.special-conditions h5 {
  font-size: 1rem;
  color: var(--text-primary);
  margin: 0 0 0.75rem 0;
  font-weight: 600;
}

.special-conditions p {
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin: 0;
  line-height: 1.6;
}

/* Actions */
.contract-actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
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
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

/* Responsive */
@media (max-width: 768px) {
  .page-header h1 {
    font-size: 2rem;
  }

  .contract-header {
    flex-direction: column;
    gap: 1rem;
  }

  .status-badge {
    align-self: flex-start;
  }

  .contract-details {
    grid-template-columns: 1fr;
  }

  .payment-reminder {
    flex-direction: column;
    text-align: center;
  }

  .contract-actions {
    flex-direction: column;
  }

  .contract-actions button {
    width: 100%;
  }
}
</style>
