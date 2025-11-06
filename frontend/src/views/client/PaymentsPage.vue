<template>
  <div>
    <AppHeader />
    <div class="payments-page">
      <div class="container">
        <h1 class="page-title">Мои платежи</h1>

        <div v-if="loading" class="text-center">
          <div class="loader"></div>
        </div>

        <div v-else-if="payments.length === 0" class="text-center text-secondary">
          <p class="text-xl">У вас пока нет платежей</p>
        </div>

        <div v-else class="payments-grid">
          <BaseCard v-for="payment in payments" :key="payment.id" elevated>
            <div class="payment-header">
              <div>
                <h3 class="text-xl font-semibold">Платеж №{{ payment.id }}</h3>
                <p class="text-secondary">{{ formatDate(payment.payment_date) }}</p>
              </div>
              <span :class="['badge', `badge-${getStatusClass(payment.payment_status)}`]">
                {{ getStatusText(payment.payment_status) }}
              </span>
            </div>

            <div class="payment-details">
              <div class="detail-row">
                <span class="text-tertiary">Тип:</span>
                <span class="font-medium">{{ getPaymentType(payment.payment_type) }}</span>
              </div>
              <div class="detail-row">
                <span class="text-tertiary">Сумма:</span>
                <span class="text-2xl font-bold text-primary">₽{{ formatMoney(payment.amount) }}</span>
              </div>
              <div class="detail-row" v-if="payment.period_month">
                <span class="text-tertiary">Период:</span>
                <span class="font-medium">{{ payment.period_month }}/{{ payment.period_year }}</span>
              </div>
              <div class="detail-row" v-if="payment.transaction_id">
                <span class="text-tertiary">ID транзакции:</span>
                <code class="text-sm">{{ payment.transaction_id }}</code>
              </div>
            </div>
          </BaseCard>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { paymentsAPI } from '@/api/services/payments'
import AppHeader from '@/components/layout/AppHeader.vue'
import BaseCard from '@/components/common/BaseCard.vue'

const payments = ref([])
const loading = ref(false)

onMounted(async () => {
  await fetchPayments()
})

const fetchPayments = async () => {
  loading.value = true
  try {
    const response = await paymentsAPI.getMyPayments()
    payments.value = response.data
  } catch (error) {
    console.error('Failed to fetch payments:', error)
  } finally {
    loading.value = false
  }
}

const formatMoney = (value) => {
  return new Intl.NumberFormat('ru-RU').format(value)
}

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('ru-RU')
}

const getStatusClass = (status) => {
  const map = {
    'completed': 'success',
    'pending': 'warning',
    'failed': 'danger',
    'refunded': 'secondary'
  }
  return map[status] || 'secondary'
}

const getStatusText = (status) => {
  const map = {
    'completed': 'Выполнен',
    'pending': 'Ожидание',
    'failed': 'Ошибка',
    'refunded': 'Возврат'
  }
  return map[status] || status
}

const getPaymentType = (type) => {
  const map = {
    'rent': 'Аренда',
    'deposit': 'Залог',
    'utilities': 'Коммунальные услуги',
    'service': 'Дополнительная услуга',
    'penalty': 'Штраф'
  }
  return map[type] || type
}
</script>

<style scoped>
.payments-page {
  min-height: calc(100vh - var(--header-height));
  padding: var(--spacing-2xl) 0;
  background: var(--bg-primary);
}

.page-title {
  font-size: var(--font-size-4xl);
  font-weight: var(--font-weight-bold);
  margin-bottom: var(--spacing-2xl);
}

.payments-grid {
  display: grid;
  gap: var(--spacing-lg);
}

.payment-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: var(--spacing-lg);
  padding-bottom: var(--spacing-md);
  border-bottom: 1px solid var(--border-color);
}

.payment-details {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
}

.detail-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
