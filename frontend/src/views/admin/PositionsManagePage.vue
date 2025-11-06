<template>
  <div class="positions-manage">
    <div class="page-header">
      <div>
        <h1>Управление должностями</h1>
        <p class="subtitle">Должности сотрудников компании</p>
      </div>
      <BaseButton variant="primary" @click="showCreateModal = true">+ Добавить должность</BaseButton>
    </div>

    <div v-if="loading" class="loading-state">
      <div class="spinner"></div>
    </div>

    <div v-else class="table-container">
      <table class="data-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Название</th>
            <th>Описание</th>
            <th>Уровень доступа</th>
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="position in positions" :key="position.id">
            <td>{{ position.id }}</td>
            <td class="font-semibold">{{ position.name }}</td>
            <td class="text-secondary">{{ position.description }}</td>
            <td><span class="badge badge-primary">Уровень {{ position.access_level }}</span></td>
            <td>
              <div class="action-buttons">
                <BaseButton variant="secondary" size="small" @click="editPosition(position)">Изменить</BaseButton>
                <BaseButton variant="danger" size="small" @click="deletePosition(position.id)">Удалить</BaseButton>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Create/Edit Modal -->
    <div v-if="showCreateModal || editingPosition" class="modal-overlay" @click.self="closeModal">
      <div class="modal">
        <div class="modal-header">
          <h2>{{ editingPosition ? 'Редактировать должность' : 'Новая должность' }}</h2>
          <button class="close-btn" @click="closeModal">×</button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="submitPosition" class="form">
            <div class="form-group">
              <label>Название *</label>
              <input v-model="positionForm.name" required />
            </div>
            <div class="form-group">
              <label>Описание</label>
              <textarea v-model="positionForm.description" rows="3"></textarea>
            </div>
            <div class="form-group">
              <label>Уровень доступа *</label>
              <input v-model.number="positionForm.access_level" type="number" min="1" max="10" required />
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
import { positionsAPI } from '@/api/services/positions'
import BaseButton from '@/components/common/BaseButton.vue'

const positions = ref([])
const loading = ref(true)
const showCreateModal = ref(false)
const editingPosition = ref(null)

const positionForm = ref({
  name: '',
  description: '',
  access_level: 1
})

onMounted(() => {
  loadPositions()
})

const loadPositions = async () => {
  loading.value = true
  try {
    const response = await positionsAPI.getAll()
    positions.value = response.data
  } catch (error) {
    console.error('Error loading positions:', error)
  } finally {
    loading.value = false
  }
}

const editPosition = (position) => {
  editingPosition.value = position
  positionForm.value = { ...position }
}

const closeModal = () => {
  showCreateModal.value = false
  editingPosition.value = null
  positionForm.value = { name: '', description: '', access_level: 1 }
}

const submitPosition = async () => {
  try {
    if (editingPosition.value) {
      await positionsAPI.update(editingPosition.value.id, positionForm.value)
    } else {
      await positionsAPI.create(positionForm.value)
    }
    await loadPositions()
    closeModal()
  } catch (error) {
    console.error('Error saving position:', error)
    alert('Ошибка при сохранении должности')
  }
}

const deletePosition = async (id) => {
  if (!confirm('Удалить эту должность?')) return
  try {
    await positionsAPI.delete(id)
    await loadPositions()
  } catch (error) {
    console.error('Error deleting position:', error)
  }
}
</script>

<style scoped>
.positions-manage {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
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
.form-group textarea {
  padding: 0.75rem;
  background: var(--bg-tertiary);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  color: var(--text-primary);
  font-size: 1rem;
  font-family: inherit;
}

.form-group input:focus,
.form-group textarea:focus {
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
