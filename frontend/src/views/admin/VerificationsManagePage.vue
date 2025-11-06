<template>
  <div class="verifications-manage">
    <div class="page-header">
      <h1>Управление верификациями</h1>
      <BaseButton variant="primary" @click="showCreateModal = true">+ Добавить верификацию</BaseButton>
    </div>

    <div v-if="loading" class="loading-state"><div class="spinner"></div></div>

    <div v-else class="table-container">
      <table class="data-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>ID клиента</th>
            <th>Дата</th>
            <th>Кредитный рейтинг</th>
            <th>Результат</th>
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="verification in verifications" :key="verification.id">
            <td>{{ verification.id }}</td>
            <td>{{ verification.client_id }}</td>
            <td>{{ formatDate(verification.verification_date) }}</td>
            <td>{{ verification.credit_score || 'Н/Д' }}</td>
            <td><span :class="['badge', `badge-${getResultClass(verification.result)}`]">{{ verification.result }}</span></td>
            <td>
              <div class="action-buttons">
                <BaseButton variant="secondary" size="small" @click="editVerification(verification)">Изменить</BaseButton>
                <BaseButton variant="danger" size="small" @click="deleteVerification(verification.id)">Удалить</BaseButton>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-if="showCreateModal || editingVerification" class="modal-overlay" @click.self="closeModal">
      <div class="modal">
        <div class="modal-header">
          <h2>{{ editingVerification ? 'Редактировать верификацию' : 'Новая верификация' }}</h2>
          <button class="close-btn" @click="closeModal">×</button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="submitVerification" class="form">
            <div class="form-group">
              <label>ID клиента *</label>
              <input v-model.number="verificationForm.client_id" type="number" required />
            </div>
            <div class="form-group">
              <label>ID проверяющего *</label>
              <input v-model.number="verificationForm.verified_by" type="number" required />
            </div>
            <div class="form-group">
              <label>Кредитный рейтинг</label>
              <input v-model.number="verificationForm.credit_score" type="number" min="300" max="850" />
            </div>
            <div class="form-group">
              <label>Результат *</label>
              <select v-model="verificationForm.result" required>
                <option value="approved">Одобрено</option>
                <option value="conditionally_approved">Условно одобрено</option>
                <option value="rejected">Отклонено</option>
              </select>
            </div>
            <div class="form-group">
              <label>Примечания</label>
              <textarea v-model="verificationForm.notes" rows="3"></textarea>
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
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { verificationsAPI } from '@/api/services/verifications'
import BaseButton from '@/components/common/BaseButton.vue'

const verifications = ref([])
const loading = ref(true)
const showCreateModal = ref(false)
const editingVerification = ref(null)
const verificationForm = ref({ client_id: null, verified_by: null, credit_score: null, result: 'approved', notes: '' })

onMounted(() => { loadVerifications() })

const loadVerifications = async () => {
  loading.value = true
  try {
    const response = await verificationsAPI.getAll()
    verifications.value = response.data
  } catch (error) {
    console.error('Error loading verifications:', error)
  } finally {
    loading.value = false
  }
}

const editVerification = (verification) => {
  editingVerification.value = verification
  verificationForm.value = { ...verification }
}

const closeModal = () => {
  showCreateModal.value = false
  editingVerification.value = null
  verificationForm.value = { client_id: null, verified_by: null, credit_score: null, result: 'approved', notes: '' }
}

const submitVerification = async () => {
  try {
    if (editingVerification.value) {
      await verificationsAPI.update(editingVerification.value.id, verificationForm.value)
    } else {
      await verificationsAPI.create(verificationForm.value)
    }
    await loadVerifications()
    closeModal()
  } catch (error) {
    console.error('Error saving verification:', error)
    alert('Ошибка при сохранении верификации')
  }
}

const deleteVerification = async (id) => {
  if (!confirm('Удалить эту верификацию?')) return
  try {
    await verificationsAPI.delete(id)
    await loadVerifications()
  } catch (error) {
    console.error('Error deleting verification:', error)
  }
}

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('ru-RU')
}

const getResultClass = (result) => {
  const map = { 'approved': 'success', 'conditionally_approved': 'warning', 'rejected': 'danger' }
  return map[result] || 'secondary'
}
</script>

<style scoped>
.verifications-manage { max-width: 1400px; margin: 0 auto; padding: 2rem; }
.page-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; }
.page-header h1 { font-size: 2rem; color: var(--text-primary); }
.loading-state { text-align: center; padding: 4rem 2rem; }
.spinner { width: 50px; height: 50px; margin: 0 auto; border: 3px solid var(--bg-tertiary); border-top-color: var(--primary-color); border-radius: 50%; animation: spin 0.8s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
.table-container { background: var(--bg-secondary); border-radius: 12px; overflow-x: auto; border: 1px solid rgba(255, 255, 255, 0.1); }
.data-table { width: 100%; border-collapse: collapse; }
.data-table thead { background: var(--bg-tertiary); }
.data-table th { padding: 1rem; text-align: left; font-weight: 600; color: var(--text-secondary); font-size: 0.875rem; text-transform: uppercase; }
.data-table td { padding: 1rem; border-top: 1px solid rgba(255, 255, 255, 0.05); color: var(--text-primary); }
.action-buttons { display: flex; gap: 0.5rem; }
.modal-overlay { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0, 0, 0, 0.8); display: flex; align-items: center; justify-content: center; z-index: 1000; padding: 1rem; }
.modal { background: var(--bg-secondary); border-radius: 16px; max-width: 600px; width: 100%; max-height: 90vh; overflow-y: auto; border: 1px solid rgba(255, 255, 255, 0.1); }
.modal-header { display: flex; justify-content: space-between; align-items: center; padding: 1.5rem; border-bottom: 1px solid rgba(255, 255, 255, 0.1); }
.modal-header h2 { font-size: 1.5rem; color: var(--text-primary); margin: 0; }
.close-btn { background: none; border: none; font-size: 2rem; color: var(--text-secondary); cursor: pointer; padding: 0; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; }
.close-btn:hover { color: var(--text-primary); }
.modal-body { padding: 1.5rem; }
.form { display: flex; flex-direction: column; gap: 1rem; }
.form-group { display: flex; flex-direction: column; gap: 0.5rem; }
.form-group label { font-size: 0.875rem; font-weight: 500; color: var(--text-secondary); }
.form-group input, .form-group select, .form-group textarea { padding: 0.75rem; background: var(--bg-tertiary); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; color: var(--text-primary); font-size: 1rem; font-family: inherit; }
.form-group input:focus, .form-group select:focus, .form-group textarea:focus { outline: none; border-color: var(--primary-color); box-shadow: 0 0 0 3px var(--primary-glow); }
.form-actions { display: flex; gap: 1rem; margin-top: 1rem; }
.form-actions button { flex: 1; }
input[type="number"]::-webkit-inner-spin-button, input[type="number"]::-webkit-outer-spin-button { -webkit-appearance: none; margin: 0; }
input[type="number"] { -moz-appearance: textfield; }
</style>
