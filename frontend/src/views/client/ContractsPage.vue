<template>
  <div>
    <AppHeader />
    <div class="contracts-page">
      <div class="container">
        <div class="page-header">
          <h1>Мои Договоры</h1>
          <p class="subtitle">Просмотр договоров аренды и истории платежей</p>
        </div>

        <!-- Loading State -->
        <div v-if="loading" class="loading-state">
          <div class="spinner"></div>
          <p>Загрузка договоров...</p>
        </div>

        <!-- Error State -->
        <div v-else-if="error" class="error-state">
          <BaseCard elevated>
            <p class="error-message">{{ error }}</p>
            <BaseButton @click="loadContracts" variant="primary">Повторить</BaseButton>
          </BaseCard>
        </div>

        <!-- Contracts List -->
        <div v-else-if="contracts.length > 0" class="contracts-list">
          <BaseCard v-for="contract in contracts" :key="contract.id" elevated class="contract-card">
            <!-- Contract Header -->
            <div class="contract-header">
              <div class="contract-info">
                <h3>Договор №{{ contract.id }}</h3>
                <p class="contract-dates">
                  {{ formatDate(contract.start_date) }} - {{ formatDate(contract.end_date) }}
                </p>
              </div>
              <span :class="['status-badge', contract.contract_status]">
                {{ getStatusText(contract.contract_status) }}
              </span>
            </div>

            <!-- Property Info -->
            <div class="property-section">
              <div class="section-title">
                <span class="icon">🏢</span>
                <h4>Детали объекта</h4>
              </div>
              <div class="property-id">ID объекта: #{{ contract.property_id }}</div>
            </div>

            <!-- Contract Details -->
            <div class="contract-details">
              <div class="detail-item">
                <span class="detail-label">Ежемесячная плата</span>
                <span class="detail-value price">{{ formatPrice(contract.monthly_rent) }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Залог</span>
                <span class="detail-value price">{{ formatPrice(contract.deposit_amount) }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">День платежа</span>
                <span class="detail-value">{{ contract.payment_day }} числа каждого месяца</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Срок договора</span>
                <span class="detail-value">{{ calculateDuration(contract.start_date, contract.end_date) }}</span>
              </div>
            </div>

            <!-- Payment Status -->
            <div v-if="contract.contract_status === 'active'" class="payment-reminder">
              <div class="reminder-icon">💳</div>
              <div class="reminder-content">
                <h5>Следующий платеж</h5>
                <p>{{ getNextPaymentDate(contract.payment_day) }}</p>
              </div>
            </div>

            <!-- Special Conditions -->
            <div v-if="contract.notes" class="special-conditions">
              <h5>Особые условия</h5>
              <p>{{ contract.notes }}</p>
            </div>

            <!-- Actions -->
            <div class="contract-actions">
              <BaseButton variant="secondary" size="small" @click="viewContractDetails(contract.id)">
                Полный договор
              </BaseButton>
              <BaseButton v-if="contract.contract_status === 'active'" variant="primary" size="small">
                Оплатить
              </BaseButton>
            </div>
          </BaseCard>
        </div>

        <!-- Empty State -->
        <div v-else class="empty-state">
          <BaseCard elevated>
            <div class="empty-content">
              <div class="empty-icon">📄</div>
              <h3>Пока нет договоров</h3>
              <p>У вас пока нет договоров аренды. Когда ваша заявка будет одобрена и договор создан, он появится здесь.</p>

              <div class="info-blocks">
                <div class="info-block">
                  <div class="info-block-icon">🔍</div>
                  <h4>Найдите объект</h4>
                  <p>Просмотрите доступные объекты недвижимости</p>
                </div>
                <div class="info-block">
                  <div class="info-block-icon">📝</div>
                  <h4>Подайте заявку</h4>
                  <p>Выберите подходящий объект и создайте заявку на аренду</p>
                </div>
                <div class="info-block">
                  <div class="info-block-icon">✅</div>
                  <h4>Получите договор</h4>
                  <p>После одобрения заявки будет создан договор аренды</p>
                </div>
              </div>

              <div class="empty-actions">
                <BaseButton variant="primary" @click="goToApplications">
                  Мои заявки
                </BaseButton>
                <BaseButton variant="secondary" @click="router.push('/client/properties')">
                  Все объекты
                </BaseButton>
              </div>
            </div>
          </BaseCard>
        </div>

        <!-- Full Contract Modal -->
        <div v-if="showContractModal" class="modal-overlay" @click.self="closeContractModal">
          <div class="modal-large">
            <div class="modal-header">
              <h2>Договор аренды №{{ selectedContract?.contract_number || selectedContract?.id }}</h2>
              <button class="close-btn" @click="closeContractModal">×</button>
            </div>
            <div class="modal-body" v-if="selectedContract">
              <div class="contract-document">
                <div class="document-header">
                  <h3>ДОГОВОР АРЕНДЫ НЕДВИЖИМОСТИ</h3>
                  <p class="document-number">№{{ selectedContract.contract_number || selectedContract.id }}</p>
                  <p class="document-date">от {{ formatDate(selectedContract.signing_date) }}</p>
                </div>

                <div class="document-section">
                  <h4>1. ПРЕДМЕТ ДОГОВОРА</h4>
                  <p>Арендодатель обязуется предоставить Арендатору во временное владение и пользование объект недвижимости (Объект ID: #{{ selectedContract.property_id }}), а Арендатор обязуется принять Объект и своевременно уплачивать арендную плату.</p>
                </div>

                <div class="document-section">
                  <h4>2. СРОК ДОГОВОРА</h4>
                  <div class="info-grid">
                    <div class="info-item">
                      <span class="info-label">Дата начала:</span>
                      <span class="info-value">{{ formatDate(selectedContract.start_date) }}</span>
                    </div>
                    <div class="info-item">
                      <span class="info-label">Дата окончания:</span>
                      <span class="info-value">{{ formatDate(selectedContract.end_date) }}</span>
                    </div>
                    <div class="info-item">
                      <span class="info-label">Срок действия:</span>
                      <span class="info-value">{{ calculateDuration(selectedContract.start_date, selectedContract.end_date) }}</span>
                    </div>
                  </div>
                </div>

                <div class="document-section">
                  <h4>3. АРЕНДНАЯ ПЛАТА</h4>
                  <div class="info-grid">
                    <div class="info-item">
                      <span class="info-label">Размер арендной платы:</span>
                      <span class="info-value price">{{ formatPrice(selectedContract.monthly_rent) }} / месяц</span>
                    </div>
                    <div class="info-item">
                      <span class="info-label">День платежа:</span>
                      <span class="info-value">{{ selectedContract.payment_day }} число каждого месяца</span>
                    </div>
                    <div class="info-item">
                      <span class="info-label">Способ оплаты:</span>
                      <span class="info-value">{{ selectedContract.payment_method || 'Банковский перевод' }}</span>
                    </div>
                  </div>
                </div>

                <div class="document-section">
                  <h4>4. ОБЕСПЕЧИТЕЛЬНЫЙ ДЕПОЗИТ</h4>
                  <div class="info-grid">
                    <div class="info-item">
                      <span class="info-label">Размер залога:</span>
                      <span class="info-value price">{{ formatPrice(selectedContract.deposit_amount) }}</span>
                    </div>
                    <div class="info-item">
                      <span class="info-label">Статус оплаты:</span>
                      <span :class="['info-value', selectedContract.deposit_paid ? 'status-paid' : 'status-pending']">
                        {{ selectedContract.deposit_paid ? '✓ Оплачен' : '⏳ Не оплачен' }}
                      </span>
                    </div>
                  </div>
                  <p class="section-note">Залог возвращается Арендатору в течение 14 дней после окончания срока аренды и передачи Объекта в надлежащем состоянии.</p>
                </div>

                <div class="document-section">
                  <h4>5. ОСОБЫЕ УСЛОВИЯ</h4>
                  <p v-if="selectedContract.notes">{{ selectedContract.notes }}</p>
                  <p v-else class="text-secondary">Особых условий не установлено.</p>
                </div>

                <div class="document-section">
                  <h4>6. СТАТУС ДОГОВОРА</h4>
                  <div class="status-info">
                    <span :class="['status-badge-large', selectedContract.contract_status]">
                      {{ getStatusText(selectedContract.contract_status) }}
                    </span>
                    <p v-if="selectedContract.signed_electronically" class="signature-info">
                      ✓ Подписан электронной подписью
                    </p>
                  </div>
                </div>

                <div class="document-footer">
                  <p class="footer-note">Настоящий договор составлен в электронной форме и имеет юридическую силу.</p>
                  <p class="footer-date">Дата формирования документа: {{ formatDate(new Date()) }}</p>
                </div>
              </div>

              <div class="modal-actions">
                <BaseButton variant="secondary" @click="printContract">
                  🖨️ Печать
                </BaseButton>
                <BaseButton variant="primary" @click="closeContractModal">
                  Закрыть
                </BaseButton>
              </div>
            </div>
          </div>
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
const showContractModal = ref(false)
const selectedContract = ref(null)

const loadContracts = async () => {
  loading.value = true
  error.value = null
  try {
    const response = await contractsAPI.getAll()
    contracts.value = response.data

    // If user is logged in, filter by their client_id
    if (authStore.user && authStore.user.client_id) {
      contracts.value = contracts.value.filter(c => c.client_id === authStore.user.client_id)
    }
  } catch (err) {
    error.value = err.response?.data?.detail || 'Не удалось загрузить договоры'
    console.error('Error loading contracts:', err)
  } finally {
    loading.value = false
  }
}

const getStatusText = (status) => {
  const statusMap = {
    active: 'Активен',
    completed: 'Завершен',
    terminated: 'Расторгнут'
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
  return `${months} мес`
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
  const contract = contracts.value.find(c => c.id === contractId)
  if (contract) {
    selectedContract.value = contract
    showContractModal.value = true
  }
}

const closeContractModal = () => {
  showContractModal.value = false
  selectedContract.value = null
}

const printContract = () => {
  window.print()
}

const goToApplications = () => {
  router.push('/client/applications')
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

.empty-content > p {
  color: var(--text-secondary);
  margin-bottom: 3rem;
  font-size: 1.125rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.info-blocks {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin: 3rem 0;
  text-align: center;
}

.info-block {
  padding: 2rem 1.5rem;
  background: rgba(255, 255, 255, 0.03);
  border-radius: 12px;
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.info-block:hover {
  background: rgba(59, 130, 246, 0.08);
  border-color: rgba(59, 130, 246, 0.3);
  transform: translateY(-4px);
}

.info-block-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.info-block h4 {
  font-size: 1.125rem;
  color: var(--text-primary);
  margin: 0 0 0.75rem 0;
  font-weight: 600;
}

.info-block p {
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin: 0;
  line-height: 1.5;
}

.empty-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 2rem;
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

/* Contract Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 1rem;
}

.modal-large {
  background: var(--bg-secondary);
  border-radius: 16px;
  max-width: 900px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  position: sticky;
  top: 0;
  background: var(--bg-secondary);
  z-index: 10;
}

.modal-header h2 {
  font-size: 1.5rem;
  color: var(--text-primary);
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  color: var(--text-secondary);
  cursor: pointer;
  padding: 0;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.3s ease;
}

.close-btn:hover {
  color: var(--text-primary);
}

.modal-body {
  padding: 2rem;
}

.contract-document {
  background: rgba(255, 255, 255, 0.02);
  padding: 2rem;
  border-radius: 12px;
  margin-bottom: 1.5rem;
}

.document-header {
  text-align: center;
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 2px solid rgba(59, 130, 246, 0.3);
}

.document-header h3 {
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0 0 0.5rem 0;
}

.document-number {
  font-size: 1.25rem;
  color: var(--primary-color);
  margin: 0.5rem 0;
}

.document-date {
  color: var(--text-tertiary);
  margin: 0;
}

.document-section {
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.document-section:last-of-type {
  border-bottom: none;
}

.document-section h4 {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 1rem 0;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.document-section p {
  line-height: 1.8;
  color: var(--text-secondary);
  margin: 0.5rem 0;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 1rem 0;
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.info-label {
  font-size: 0.875rem;
  color: var(--text-tertiary);
  font-weight: 500;
}

.info-value {
  font-size: 1rem;
  color: var(--text-primary);
  font-weight: 600;
}

.info-value.price {
  font-size: 1.25rem;
  color: var(--primary-color);
  font-weight: 700;
}

.info-value.status-paid {
  color: #22c55e;
}

.info-value.status-pending {
  color: #facc15;
}

.section-note {
  margin-top: 1rem;
  padding: 1rem;
  background: rgba(59, 130, 246, 0.05);
  border-left: 3px solid var(--primary-color);
  border-radius: 4px;
  font-size: 0.875rem;
  font-style: italic;
}

.status-info {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 1rem;
}

.status-badge-large {
  padding: 0.75rem 1.5rem;
  border-radius: 24px;
  font-size: 1rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.status-badge-large.active {
  background: rgba(34, 197, 94, 0.15);
  color: #22c55e;
}

.status-badge-large.completed {
  background: rgba(59, 130, 246, 0.15);
  color: #3b82f6;
}

.status-badge-large.terminated {
  background: rgba(239, 68, 68, 0.15);
  color: #ef4444;
}

.signature-info {
  color: #22c55e;
  font-size: 0.875rem;
  margin: 0;
}

.document-footer {
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 2px solid rgba(255, 255, 255, 0.1);
  text-align: center;
}

.footer-note {
  color: var(--text-tertiary);
  font-size: 0.875rem;
  margin: 0 0 0.5rem 0;
}

.footer-date {
  color: var(--text-tertiary);
  font-size: 0.875rem;
  margin: 0;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
}

@media print {
  .modal-header,
  .modal-actions,
  .close-btn {
    display: none !important;
  }

  .modal-large {
    max-width: 100%;
    max-height: none;
    overflow: visible;
    border: none;
  }

  .contract-document {
    background: white;
    color: black;
  }
}
</style>
