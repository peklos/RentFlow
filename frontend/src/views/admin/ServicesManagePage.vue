<template>
  <AdminLayout>
  <div class="services-manage">
    <div class="page-header">
      <h1>Управление услугами</h1>
      <BaseButton variant="primary" @click="showCreateModal = true">+ Добавить услугу</BaseButton>
    </div>

    <div v-if="loading" class="loading-state"><div class="spinner"></div></div>

    <div v-else class="table-container">
      <table class="data-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Название</th>
            <th>Описание</th>
            <th>Цена</th>
            <th>Единица</th>
            <th>Статус</th>
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="service in services" :key="service.id">
            <td>{{ service.id }}</td>
            <td class="font-semibold">{{ service.name }}</td>
            <td class="text-secondary">{{ service.description }}</td>
            <td class="font-bold">₽{{ formatMoney(service.price) }}</td>
            <td>{{ service.unit }}</td>
            <td><span :class="['badge', service.is_active ? 'badge-success' : 'badge-danger']">{{ service.is_active ? 'Активна' : 'Неактивна' }}</span></td>
            <td>
              <div class="action-buttons">
                <BaseButton variant="secondary" size="small" @click="editService(service)">Изменить</BaseButton>
                <BaseButton variant="danger" size="small" @click="deleteService(service.id)">Удалить</BaseButton>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-if="showCreateModal || editingService" class="modal-overlay" @click.self="closeModal">
      <div class="modal">
        <div class="modal-header">
          <h2>{{ editingService ? 'Редактировать услугу' : 'Новая услуга' }}</h2>
          <button class="close-btn" @click="closeModal">×</button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="submitService" class="form">
            <div class="form-group">
              <label>Название *</label>
              <input v-model="serviceForm.name" required />
            </div>
            <div class="form-group">
              <label>Описание</label>
              <textarea v-model="serviceForm.description" rows="3"></textarea>
            </div>
            <div class="form-group">
              <label>Цена *</label>
              <input v-model.number="serviceForm.price" type="number" step="0.01" required />
            </div>
            <div class="form-group">
              <label>Единица измерения</label>
              <input v-model="serviceForm.unit" placeholder="например: в месяц" />
            </div>
            <div class="form-group checkbox">
              <label>
                <input type="checkbox" v-model="serviceForm.is_active" />
                <span>Услуга активна</span>
              </label>
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
import { servicesAPI } from '@/api/services/services'
import AdminLayout from '@/components/layout/AdminLayout.vue'
import BaseButton from '@/components/common/BaseButton.vue'

const services = ref([])
const loading = ref(true)
const showCreateModal = ref(false)
const editingService = ref(null)
const serviceForm = ref({ name: '', description: '', price: null, unit: '', is_active: true })

onMounted(() => { loadServices() })

const loadServices = async () => {
  loading.value = true
  try {
    const response = await servicesAPI.getAllAdmin()
    services.value = response.data
  } catch (error) {
    console.error('Error loading services:', error)
  } finally {
    loading.value = false
  }
}

const editService = (service) => {
  editingService.value = service
  serviceForm.value = { ...service }
}

const closeModal = () => {
  showCreateModal.value = false
  editingService.value = null
  serviceForm.value = { name: '', description: '', price: null, unit: '', is_active: true }
}

const submitService = async () => {
  try {
    if (editingService.value) {
      await servicesAPI.update(editingService.value.id, serviceForm.value)
    } else {
      await servicesAPI.create(serviceForm.value)
    }
    await loadServices()
    closeModal()
  } catch (error) {
    console.error('Error saving service:', error)
    alert('Ошибка при сохранении услуги')
  }
}

const deleteService = async (id) => {
  if (!confirm('Удалить эту услугу?')) return
  try {
    await servicesAPI.delete(id)
    await loadServices()
  } catch (error) {
    console.error('Error deleting service:', error)
  }
}

const formatMoney = (value) => {
  return new Intl.NumberFormat('ru-RU').format(value)
}
</script>

<style scoped>
.services-manage { max-width: 1400px; margin: 0 auto; padding: 2rem; }
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
.form-group input, .form-group textarea { padding: 0.75rem; background: var(--bg-tertiary); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; color: var(--text-primary); font-size: 1rem; font-family: inherit; }
.form-group input:focus, .form-group textarea:focus { outline: none; border-color: var(--primary-color); box-shadow: 0 0 0 3px var(--primary-glow); }
.form-group.checkbox { flex-direction: row; align-items: center; }
.form-group.checkbox label { display: flex; align-items: center; gap: 0.5rem; cursor: pointer; }
.form-group.checkbox input[type="checkbox"] { width: auto; cursor: pointer; }
.form-actions { display: flex; gap: 1rem; margin-top: 1rem; }
.form-actions button { flex: 1; }
input[type="number"]::-webkit-inner-spin-button, input[type="number"]::-webkit-outer-spin-button { -webkit-appearance: none; margin: 0; }
input[type="number"] { -moz-appearance: textfield; }
</style>
