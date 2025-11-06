<template>
  <div class="employees-manage">
    <div class="page-header">
      <h1>Управление сотрудниками</h1>
      <BaseButton variant="primary" @click="showCreateModal = true">+ Добавить сотрудника</BaseButton>
    </div>

    <div v-if="loading" class="loading-state"><div class="spinner"></div></div>

    <div v-else class="table-container">
      <table class="data-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>ФИО</th>
            <th>Логин</th>
            <th>Должность</th>
            <th>Телефон</th>
            <th>Email</th>
            <th>Статус</th>
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="employee in employees" :key="employee.id">
            <td>{{ employee.id }}</td>
            <td class="font-semibold">{{ employee.full_name }}</td>
            <td><code>{{ employee.login }}</code></td>
            <td>{{ employee.position_id }}</td>
            <td>{{ employee.phone }}</td>
            <td>{{ employee.email }}</td>
            <td><span :class="['badge', employee.is_active ? 'badge-success' : 'badge-danger']">{{ employee.is_active ? 'Активен' : 'Неактивен' }}</span></td>
            <td>
              <div class="action-buttons">
                <BaseButton variant="secondary" size="small" @click="editEmployee(employee)">Изменить</BaseButton>
                <BaseButton variant="danger" size="small" @click="deleteEmployee(employee.id)">Удалить</BaseButton>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-if="showCreateModal || editingEmployee" class="modal-overlay" @click.self="closeModal">
      <div class="modal">
        <div class="modal-header">
          <h2>{{ editingEmployee ? 'Редактировать сотрудника' : 'Новый сотрудник' }}</h2>
          <button class="close-btn" @click="closeModal">×</button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="submitEmployee" class="form">
            <div class="form-group">
              <label>ФИО *</label>
              <input v-model="employeeForm.full_name" required />
            </div>
            <div class="form-group">
              <label>Логин *</label>
              <input v-model="employeeForm.login" required />
            </div>
            <div class="form-group">
              <label>Пароль *</label>
              <input v-model="employeeForm.password_hash" type="password" required />
            </div>
            <div class="form-group">
              <label>ID должности *</label>
              <input v-model.number="employeeForm.position_id" type="number" required />
            </div>
            <div class="form-group">
              <label>Телефон</label>
              <input v-model="employeeForm.phone" />
            </div>
            <div class="form-group">
              <label>Email</label>
              <input v-model="employeeForm.email" type="email" />
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
import { employeesAPI } from '@/api/services/employees'
import BaseButton from '@/components/common/BaseButton.vue'

const employees = ref([])
const loading = ref(true)
const showCreateModal = ref(false)
const editingEmployee = ref(null)
const employeeForm = ref({ full_name: '', login: '', password_hash: '', position_id: null, phone: '', email: '' })

onMounted(() => { loadEmployees() })

const loadEmployees = async () => {
  loading.value = true
  try {
    const response = await employeesAPI.getAll()
    employees.value = response.data
  } catch (error) {
    console.error('Error loading employees:', error)
  } finally {
    loading.value = false
  }
}

const editEmployee = (employee) => {
  editingEmployee.value = employee
  employeeForm.value = { ...employee, password_hash: '' }
}

const closeModal = () => {
  showCreateModal.value = false
  editingEmployee.value = null
  employeeForm.value = { full_name: '', login: '', password_hash: '', position_id: null, phone: '', email: '' }
}

const submitEmployee = async () => {
  try {
    if (editingEmployee.value) {
      await employeesAPI.update(editingEmployee.value.id, employeeForm.value)
    } else {
      await employeesAPI.create(employeeForm.value)
    }
    await loadEmployees()
    closeModal()
  } catch (error) {
    console.error('Error saving employee:', error)
    alert('Ошибка при сохранении сотрудника')
  }
}

const deleteEmployee = async (id) => {
  if (!confirm('Удалить этого сотрудника?')) return
  try {
    await employeesAPI.delete(id)
    await loadEmployees()
  } catch (error) {
    console.error('Error deleting employee:', error)
  }
}
</script>

<style scoped>
.employees-manage { max-width: 1600px; margin: 0 auto; padding: 2rem; }
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
.form-group input { padding: 0.75rem; background: var(--bg-tertiary); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; color: var(--text-primary); font-size: 1rem; }
.form-group input:focus { outline: none; border-color: var(--primary-color); box-shadow: 0 0 0 3px var(--primary-glow); }
.form-actions { display: flex; gap: 1rem; margin-top: 1rem; }
.form-actions button { flex: 1; }
input[type="number"]::-webkit-inner-spin-button, input[type="number"]::-webkit-outer-spin-button { -webkit-appearance: none; margin: 0; }
input[type="number"] { -moz-appearance: textfield; }
</style>
