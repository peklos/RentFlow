<template>
  <div>
    <AppHeader />
    <div class="profile-page">
      <div class="container">
        <div class="page-header">
          <h1 class="page-title">Мой Профиль</h1>
          <BaseButton variant="primary" @click="showEditModal = true">Редактировать профиль</BaseButton>
        </div>

        <div v-if="loading" class="loading-state">
          <div class="spinner"></div>
          <p>Загрузка профиля...</p>
        </div>

        <div v-else-if="error" class="error-state">
          <BaseCard elevated>
            <p class="error-message">{{ error }}</p>
            <BaseButton @click="loadProfile" variant="primary">Повторить</BaseButton>
          </BaseCard>
        </div>

        <div v-else-if="profile" class="profile-content">
          <!-- Status Header -->
          <BaseCard elevated class="status-card">
            <div class="status-header">
              <div class="avatar-section">
                <div class="avatar">
                  {{ getInitials(profile.full_name) }}
                </div>
                <div class="user-info">
                  <h2 class="user-name">{{ profile.full_name }}</h2>
                  <p class="user-meta">Клиент с {{ formatDate(profile.registration_date) }}</p>
                </div>
              </div>
              <div class="badges">
                <span :class="['badge', profile.is_verified ? 'badge-success' : 'badge-warning']">
                  {{ profile.is_verified ? '✓ Верифицирован' : '⏳ Не верифицирован' }}
                </span>
                <span class="badge badge-secondary">
                  {{ profile.client_type === 'individual' ? '👤 Физ. лицо' : '🏢 Юр. лицо' }}
                </span>
              </div>
            </div>
          </BaseCard>

          <div class="profile-grid">
            <!-- Personal Information -->
            <BaseCard elevated>
              <div class="card-header">
                <h3 class="section-title">
                  <span class="icon">👤</span>
                  Личная информация
                </h3>
              </div>
              <div class="info-grid">
                <div class="info-item">
                  <span class="info-label">Телефон</span>
                  <span class="info-value">{{ profile.phone || 'Не указан' }}</span>
                </div>
                <div class="info-item">
                  <span class="info-label">Email</span>
                  <span class="info-value">{{ profile.email || 'Не указан' }}</span>
                </div>
                <div class="info-item">
                  <span class="info-label">Альтернативный телефон</span>
                  <span class="info-value">{{ profile.alternative_phone || 'Не указан' }}</span>
                </div>
                <div class="info-item">
                  <span class="info-label">Дата рождения</span>
                  <span class="info-value">{{ profile.date_of_birth ? formatDate(profile.date_of_birth) : 'Не указана' }}</span>
                </div>
              </div>
            </BaseCard>

            <!-- Address Information -->
            <BaseCard elevated>
              <div class="card-header">
                <h3 class="section-title">
                  <span class="icon">📍</span>
                  Адреса
                </h3>
              </div>
              <div class="info-grid">
                <div class="info-item full-width">
                  <span class="info-label">Адрес регистрации</span>
                  <span class="info-value">{{ profile.registration_address || 'Не указан' }}</span>
                </div>
                <div class="info-item full-width">
                  <span class="info-label">Фактический адрес</span>
                  <span class="info-value">{{ profile.actual_address || 'Не указан' }}</span>
                </div>
              </div>
            </BaseCard>

            <!-- Work Information -->
            <BaseCard elevated>
              <div class="card-header">
                <h3 class="section-title">
                  <span class="icon">💼</span>
                  Работа и доход
                </h3>
              </div>
              <div class="info-grid">
                <div class="info-item">
                  <span class="info-label">Место работы</span>
                  <span class="info-value">{{ profile.workplace || 'Не указано' }}</span>
                </div>
                <div class="info-item">
                  <span class="info-label">Должность</span>
                  <span class="info-value">{{ profile.position || 'Не указана' }}</span>
                </div>
                <div class="info-item full-width">
                  <span class="info-label">Ежемесячный доход</span>
                  <span class="info-value income">
                    {{ profile.monthly_income ? `₽${formatMoney(profile.monthly_income)}` : 'Не указан' }}
                  </span>
                </div>
              </div>
            </BaseCard>

            <!-- Statistics -->
            <BaseCard elevated class="stats-card">
              <div class="card-header">
                <h3 class="section-title">
                  <span class="icon">📊</span>
                  Статистика
                </h3>
              </div>
              <div class="stats-grid">
                <div class="stat-item">
                  <div class="stat-value">{{ stats.applications }}</div>
                  <div class="stat-label">Заявок</div>
                </div>
                <div class="stat-item">
                  <div class="stat-value">{{ stats.contracts }}</div>
                  <div class="stat-label">Договоров</div>
                </div>
                <div class="stat-item">
                  <div class="stat-value">{{ stats.reviews }}</div>
                  <div class="stat-label">Отзывов</div>
                </div>
              </div>
            </BaseCard>
          </div>
        </div>

        <!-- Edit Modal -->
        <div v-if="showEditModal" class="modal-overlay" @click.self="closeModal">
          <div class="modal">
            <div class="modal-header">
              <h2>Редактировать профиль</h2>
              <button class="close-btn" @click="closeModal">×</button>
            </div>
            <div class="modal-body">
              <form @submit.prevent="saveProfile" class="edit-form">
                <div class="form-section">
                  <h4 class="form-section-title">Личная информация</h4>
                  <div class="form-row">
                    <div class="form-group">
                      <label>ФИО *</label>
                      <input v-model="editForm.full_name" type="text" required />
                    </div>
                    <div class="form-group">
                      <label>Дата рождения</label>
                      <input v-model="editForm.date_of_birth" type="date" />
                    </div>
                  </div>
                  <div class="form-row">
                    <div class="form-group">
                      <label>Телефон *</label>
                      <input v-model="editForm.phone" type="tel" required />
                    </div>
                    <div class="form-group">
                      <label>Email</label>
                      <input v-model="editForm.email" type="email" />
                    </div>
                  </div>
                  <div class="form-group">
                    <label>Альтернативный телефон</label>
                    <input v-model="editForm.alternative_phone" type="tel" />
                  </div>
                </div>

                <div class="form-section">
                  <h4 class="form-section-title">Адреса</h4>
                  <div class="form-group">
                    <label>Адрес регистрации</label>
                    <textarea v-model="editForm.registration_address" rows="2"></textarea>
                  </div>
                  <div class="form-group">
                    <label>Фактический адрес</label>
                    <textarea v-model="editForm.actual_address" rows="2"></textarea>
                  </div>
                </div>

                <div class="form-section">
                  <h4 class="form-section-title">Работа</h4>
                  <div class="form-row">
                    <div class="form-group">
                      <label>Место работы</label>
                      <input v-model="editForm.workplace" type="text" />
                    </div>
                    <div class="form-group">
                      <label>Должность</label>
                      <input v-model="editForm.position" type="text" />
                    </div>
                  </div>
                  <div class="form-group">
                    <label>Ежемесячный доход</label>
                    <input v-model.number="editForm.monthly_income" type="number" step="0.01" placeholder="50000" />
                  </div>
                </div>

                <div class="form-actions">
                  <BaseButton type="button" variant="secondary" @click="closeModal">Отмена</BaseButton>
                  <BaseButton type="submit" variant="primary">Сохранить изменения</BaseButton>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { profileAPI } from '@/api/services/profile'
import { applicationsAPI } from '@/api/services/applications'
import { contractsAPI } from '@/api/services/contracts'
import { reviewsAPI } from '@/api/services/reviews'
import AppHeader from '@/components/layout/AppHeader.vue'
import BaseCard from '@/components/common/BaseCard.vue'
import BaseButton from '@/components/common/BaseButton.vue'

const authStore = useAuthStore()
const profile = ref(null)
const loading = ref(true)
const error = ref(null)
const showEditModal = ref(false)

const stats = ref({
  applications: 0,
  contracts: 0,
  reviews: 0
})

const editForm = ref({
  full_name: '',
  date_of_birth: null,
  phone: '',
  email: '',
  alternative_phone: '',
  registration_address: '',
  actual_address: '',
  workplace: '',
  position: '',
  monthly_income: null
})

onMounted(async () => {
  await loadProfile()
  await loadStats()
})

const loadProfile = async () => {
  loading.value = true
  error.value = null
  try {
    // Get client ID from auth store
    const clientId = authStore.user?.client_id || authStore.user?.id
    if (!clientId) {
      error.value = 'Пожалуйста, выйдите и войдите заново для обновления сессии'
      loading.value = false
      return
    }

    const response = await profileAPI.getProfile(clientId)
    profile.value = response.data
  } catch (err) {
    error.value = err.response?.data?.detail || 'Не удалось загрузить профиль'
    console.error('Error loading profile:', err)
  } finally {
    loading.value = false
  }
}

const loadStats = async () => {
  try {
    const [appsRes, contractsRes, reviewsRes] = await Promise.all([
      applicationsAPI.getMyApplications().catch(() => ({ data: [] })),
      contractsAPI.getAll().catch(() => ({ data: [] })),
      reviewsAPI.getMyReviews().catch(() => ({ data: [] }))
    ])

    stats.value = {
      applications: appsRes.data?.length || 0,
      contracts: contractsRes.data?.length || 0,
      reviews: reviewsRes.data?.length || 0
    }
  } catch (err) {
    console.error('Error loading stats:', err)
  }
}

const closeModal = () => {
  showEditModal.value = false
}

const openEditModal = () => {
  // Populate edit form with current profile data
  editForm.value = {
    full_name: profile.value.full_name || '',
    date_of_birth: profile.value.date_of_birth || null,
    phone: profile.value.phone || '',
    email: profile.value.email || '',
    alternative_phone: profile.value.alternative_phone || '',
    registration_address: profile.value.registration_address || '',
    actual_address: profile.value.actual_address || '',
    workplace: profile.value.workplace || '',
    position: profile.value.position || '',
    monthly_income: profile.value.monthly_income || null
  }
  showEditModal.value = true
}

const saveProfile = async () => {
  try {
    const clientId = authStore.user?.client_id || authStore.user?.id
    if (!clientId) {
      alert('Ошибка: ID клиента не найден. Пожалуйста, выйдите и войдите заново.')
      return
    }

    await profileAPI.updateProfile(clientId, editForm.value)
    await loadProfile()
    closeModal()
    alert('Профиль успешно обновлен!')
  } catch (err) {
    console.error('Error updating profile:', err)
    alert('Ошибка при обновлении профиля')
  }
}

// Watch for modal open to populate form
const watchModal = () => {
  if (showEditModal.value && profile.value) {
    openEditModal()
  }
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

const formatMoney = (value) => {
  return new Intl.NumberFormat('ru-RU').format(value)
}

const getInitials = (fullName) => {
  if (!fullName) return '??'
  const parts = fullName.split(' ')
  if (parts.length >= 2) {
    return (parts[0][0] + parts[1][0]).toUpperCase()
  }
  return fullName.substring(0, 2).toUpperCase()
}

// Update editForm when modal opens
const updateEditForm = () => {
  if (profile.value) {
    editForm.value = {
      full_name: profile.value.full_name || '',
      date_of_birth: profile.value.date_of_birth || null,
      phone: profile.value.phone || '',
      email: profile.value.email || '',
      alternative_phone: profile.value.alternative_phone || '',
      registration_address: profile.value.registration_address || '',
      actual_address: profile.value.actual_address || '',
      workplace: profile.value.workplace || '',
      position: profile.value.position || '',
      monthly_income: profile.value.monthly_income || null
    }
  }
}

// Watch showEditModal and update form when it opens
const handleModalOpen = () => {
  if (showEditModal.value) {
    updateEditForm()
  }
}
</script>

<style scoped>
.profile-page {
  min-height: calc(100vh - var(--header-height));
  padding: var(--spacing-2xl) 0;
  background: var(--bg-primary);
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--spacing-2xl);
}

.page-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--text-primary);
}

.loading-state, .error-state {
  text-align: center;
  padding: 4rem 2rem;
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

/* Status Card */
.status-card {
  margin-bottom: var(--spacing-2xl);
}

.status-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: var(--spacing-lg);
}

.avatar-section {
  display: flex;
  align-items: center;
  gap: var(--spacing-lg);
}

.avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  font-weight: 700;
  color: white;
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
}

.user-name {
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0;
}

.user-meta {
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin: 0.25rem 0 0 0;
}

.badges {
  display: flex;
  gap: var(--spacing-sm);
  flex-wrap: wrap;
}

/* Profile Grid */
.profile-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: var(--spacing-xl);
}

.card-header {
  margin-bottom: var(--spacing-lg);
  padding-bottom: var(--spacing-md);
  border-bottom: 2px solid rgba(255, 255, 255, 0.1);
}

.section-title {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0;
}

.section-title .icon {
  font-size: 1.5rem;
}

/* Info Grid */
.info-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--spacing-lg);
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xs);
}

.info-item.full-width {
  grid-column: 1 / -1;
}

.info-label {
  font-size: 0.875rem;
  color: var(--text-tertiary);
  text-transform: uppercase;
  font-weight: 500;
  letter-spacing: 0.5px;
}

.info-value {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-primary);
  word-break: break-word;
}

.info-value.income {
  font-size: 1.25rem;
  color: var(--primary-color);
  font-weight: 700;
}

/* Statistics */
.stats-card {
  grid-column: 1 / -1;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--spacing-lg);
  text-align: center;
}

.stat-item {
  padding: var(--spacing-lg);
  background: rgba(255, 255, 255, 0.03);
  border-radius: var(--radius-lg);
  transition: all 0.3s ease;
}

.stat-item:hover {
  background: rgba(59, 130, 246, 0.1);
  transform: translateY(-2px);
}

.stat-value {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--primary-color);
  margin-bottom: var(--spacing-xs);
}

.stat-label {
  font-size: 0.875rem;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* Modal */
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
  max-width: 700px;
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
  transition: color 0.3s ease;
}

.close-btn:hover {
  color: var(--text-primary);
}

.modal-body {
  padding: 1.5rem;
}

/* Form */
.edit-form {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xl);
}

.form-section {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
}

.form-section-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 var(--spacing-sm) 0;
  padding-bottom: var(--spacing-sm);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.form-row {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--spacing-md);
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
  transition: all 0.3s ease;
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

/* Responsive */
@media (max-width: 768px) {
  .page-header {
    flex-direction: column;
    align-items: flex-start;
    gap: var(--spacing-md);
  }

  .status-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .profile-grid {
    grid-template-columns: 1fr;
  }

  .info-grid {
    grid-template-columns: 1fr;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .form-row {
    grid-template-columns: 1fr;
  }
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
