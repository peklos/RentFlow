<template>
  <AdminLayout>
    <div class="payments-manage">
      <div class="page-header">
        <div>
          <h1>Управление платежами</h1>
          <p class="subtitle">Все платежи по договорам аренды</p>
        </div>
        <BaseButton variant="primary" @click="showCreateModal = true">+ Добавить платеж</BaseButton>
      </div>

      <div v-if="loading" class="loading-state">
        <div class="spinner"></div>
      </div>

      <div v-else class="table-container">
      <table class="data-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Дата</th>
            <th>Сумма</th>
            <th>Тип</th>
            <th>Статус</th>
            <th>ID контракта</th>
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="payment in payments" :key="payment.id">
            <td>{{ payment.id }}</td>
            <td>{{ formatDate(payment.payment_date) }}</td>
            <td class="font-bold">₽{{ formatMoney(payment.amount) }}</td>
            <td><span class="badge badge-secondary">{{ payment.payment_type }}</span></td>
            <td><span :class="['badge', `badge-${getStatusClass(payment.payment_status)}`]">{{ payment.payment_status }}</span></td>
            <td>{{ payment.contract_id }}</td>
            <td>
              <div class="action-buttons">
                <BaseButton variant="secondary" size="small" @click="editPayment(payment)">Изменить</BaseButton>
                <BaseButton variant="danger" size="small" @click="deletePayment(payment.id)">Удалить</BaseButton>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
      </div>

      <!-- Create/Edit Modal -->
      <div v-if="showCreateModal || editingPayment" class="modal-overlay" @click.self="closeModal">
      <div class="modal">
        <div class="modal-header">
          <h2>{{ editingPayment ? 'Редактировать платеж' : 'Новый платеж' }}</h2>
          <button class="close-btn" @click="closeModal">×</button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="submitPayment" class="form">
            <div class="form-group">
              <label>ID контракта *</label>
              <input v-model.number="paymentForm.contract_id" type="number" required />
            </div>
            <div class="form-group">
              <label>Сумма *</label>
              <input v-model.number="paymentForm.amount" type="number" step="0.01" required />
            </div>
            <div class="form-group">
              <label>Тип платежа *</label>
              <select v-model="paymentForm.payment_type" required>
                <option value="rent">Аренда</option>
                <option value="deposit">Залог</option>
                <option value="utilities">Коммунальные услуги</option>
                <option value="service">Услуга</option>
                <option value="penalty">Штраф</option>
              </select>
            </div>
            <div class="form-group">
              <label>Статус *</label>
              <select v-model="paymentForm.payment_status" required>
                <option value="pending">Ожидание</option>
                <option value="completed">Выполнен</option>
                <option value="failed">Ошибка</option>
                <option value="refunded">Возврат</option>
              </select>
            </div>
            <div class="form-actions">
              <BaseButton type="button" variant="secondary" @click="closeModal">Отмена</BaseButton>
              <BaseButton type="submit" variant="primary">Сохранить</BaseButton>
            </div>
          </form>
        </div>
      </div>
      </div>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { paymentsAPI } from '@/api/services/payments'
import AdminLayout from '@/components/layout/AdminLayout.vue'
import BaseButton from '@/components/common/BaseButton.vue'

const payments = ref([])
const loading = ref(true)
const showCreateModal = ref(false)
const editingPayment = ref(null)

const paymentForm = ref({
  contract_id: null,
  amount: null,
  payment_type: 'rent',
  payment_status: 'pending'
})

onMounted(() => {
  loadPayments()
})

const loadPayments = async () => {
  loading.value = true
  try {
    const response = await paymentsAPI.getAll()
    payments.value = response.data
  } catch (error) {
    console.error('Error loading payments:', error)
  } finally {
    loading.value = false
  }
}

const editPayment = (payment) => {
  editingPayment.value = payment
  paymentForm.value = { ...payment }
}

const closeModal = () => {
  showCreateModal.value = false
  editingPayment.value = null
  paymentForm.value = { contract_id: null, amount: null, payment_type: 'rent', payment_status: 'pending' }
}

const submitPayment = async () => {
  try {
    if (editingPayment.value) {
      await paymentsAPI.update(editingPayment.value.id, paymentForm.value)
    } else {
      await paymentsAPI.create(paymentForm.value)
    }
    await loadPayments()
    closeModal()
  } catch (error) {
    console.error('Error saving payment:', error)
    alert('Ошибка при сохранении платежа')
  }
}

const deletePayment = async (id) => {
  if (!confirm('Удалить этот платеж?')) return
  try {
    await paymentsAPI.delete(id)
    await loadPayments()
  } catch (error) {
    console.error('Error deleting payment:', error)
  }
}

const formatMoney = (value) => {
  return new Intl.NumberFormat('ru-RU').format(value)
}

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('ru-RU')
}

const getStatusClass = (status) => {
  const map = { 'completed': 'success', 'pending': 'warning', 'failed': 'danger', 'refunded': 'secondary' }
  return map[status] || 'secondary'
}
</script>

<style scoped>
.payments-manage {
  max-width: 1400px;
  margin: 0 auto;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.page-header h1 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  color: var(--text-primary);
}

.subtitle {
  color: var(--text-secondary);
}

.loading-state {
  text-align: center;
  padding: 4rem 2rem;
}

.spinner {
  width: 50px;
  height: 50px;
  margin: 0 auto;
  border: 3px solid var(--bg-tertiary);
  border-top-color: var(--primary-color);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.table-container {
  background: var(--bg-secondary);
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.data-table {
  width: 100%;
  border-collapse: collapse;
}

.data-table thead {
  background: var(--bg-tertiary);
}

.data-table th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  color: var(--text-secondary);
  font-size: 0.875rem;
  text-transform: uppercase;
}

.data-table td {
  padding: 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  color: var(--text-primary);
}

.action-buttons {
  display: flex;
  gap: 0.5rem;
}

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

.modal {
  background: var(--bg-secondary);
  border-radius: 16px;
  max-width: 600px;
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
}

.close-btn:hover {
  color: var(--text-primary);
}

.modal-body {
  padding: 1.5rem;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group label {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--text-secondary);
}

.form-group input,
.form-group select {
  padding: 0.75rem;
  background: var(--bg-tertiary);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  color: var(--text-primary);
  font-size: 1rem;
}

.form-group input:focus,
.form-group select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px var(--primary-glow);
}

.form-actions {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

.form-actions button {
  flex: 1;
}

input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type="number"] {
  -moz-appearance: textfield;
}
</style>
