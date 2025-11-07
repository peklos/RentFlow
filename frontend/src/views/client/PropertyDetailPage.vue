<template>
  <div>
    <AppHeader />
    <div class="property-detail-page">
      <div class="container">
        <div v-if="loading" class="loading-state">
          <div class="spinner"></div>
          <p>Загрузка...</p>
        </div>

        <div v-else-if="!property" class="error-state">
          <h2>Объект не найден</h2>
          <BaseButton @click="$router.push('/properties')">Вернуться к списку</BaseButton>
        </div>

        <div v-else>
          <BaseButton variant="ghost" @click="$router.push('/properties')" class="mb-lg">
            ← Назад к списку
          </BaseButton>

          <div class="property-header">
            <div>
              <h1 class="property-title">{{ property.subtype }}</h1>
              <p class="property-address">📍 {{ property.address }}</p>
            </div>
            <span :class="['status-badge', `status-${property.status}`]">
              {{ getStatusText(property.status) }}
            </span>
          </div>

          <div class="property-grid">
            <!-- Main Image -->
            <div class="property-image-section">
              <img :src="getPropertyImage(property.subtype)" :alt="property.subtype" class="main-image" />
            </div>

            <!-- Details -->
            <BaseCard elevated>
              <h2 class="section-title">Информация об объекте</h2>
              <div class="details-grid">
                <div class="detail-item">
                  <span class="detail-label">Площадь</span>
                  <span class="detail-value">{{ property.area }} м²</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">Комнаты</span>
                  <span class="detail-value">{{ property.rooms_count || 'Н/Д' }}</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">Этаж</span>
                  <span class="detail-value">{{ property.floor }}/{{ property.total_floors }}</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">Ремонт</span>
                  <span class="detail-value">{{ property.renovation_type || 'Не указан' }}</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">Мебель</span>
                  <span class="detail-value">{{ property.is_furnished ? 'Есть' : 'Без мебели' }}</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">Коммунальные</span>
                  <span class="detail-value">{{ property.utilities_included ? 'Включены' : 'Отдельно' }}</span>
                </div>
              </div>

              <div class="price-section">
                <div>
                  <p class="text-tertiary mb-xs">Цена за месяц</p>
                  <p class="price">₽{{ formatMoney(property.monthly_rent) }}</p>
                </div>
                <div>
                  <p class="text-tertiary mb-xs">Залог</p>
                  <p class="deposit">₽{{ formatMoney(property.deposit_amount) }}</p>
                </div>
              </div>

              <BaseButton variant="primary" size="lg" class="w-full" @click="applyForProperty">
                Подать заявку на аренду
              </BaseButton>
            </BaseCard>
          </div>

          <!-- Description -->
          <BaseCard elevated class="mt-lg">
            <h2 class="section-title">Описание</h2>
            <p class="description">{{ property.description || 'Описание не указано' }}</p>
          </BaseCard>

          <!-- Amenities -->
          <BaseCard elevated class="mt-lg" v-if="property.amenities">
            <h2 class="section-title">Удобства</h2>
            <div class="amenities-grid">
              <div v-for="(amenity, index) in getAmenities(property.amenities)" :key="index" class="amenity-item">
                ✓ {{ amenity }}
              </div>
            </div>
          </BaseCard>
        </div>
      </div>
    </div>

    <!-- Application Modal -->
    <div v-if="showApplicationModal" class="modal-overlay" @click.self="closeApplicationModal">
      <div class="modal-content">
        <BaseCard elevated>
          <div class="modal-header">
            <h2>Подать заявку на аренду</h2>
            <button class="close-btn" @click="closeApplicationModal">×</button>
          </div>

          <div v-if="submitSuccess" class="success-message">
            <div class="success-icon">✓</div>
            <h3>Заявка успешно подана!</h3>
            <p>Переадресация на страницу заявок...</p>
          </div>

          <form v-else @submit.prevent="submitApplication" class="application-form">
            <div class="property-summary">
              <h4>{{ property.subtype }}</h4>
              <p>{{ property.address }}</p>
              <p class="price">₽{{ formatMoney(property.monthly_rent) }}/месяц</p>
            </div>

            <BaseInput
              v-model="applicationForm.preferred_move_in_date"
              type="date"
              label="Желаемая дата заселения"
              required
            />

            <BaseInput
              v-model="applicationForm.lease_duration_months"
              type="number"
              label="Срок аренды (месяцев)"
              min="1"
              required
            />

            <div class="form-group">
              <label for="notes">Дополнительная информация (необязательно)</label>
              <textarea
                id="notes"
                v-model="applicationForm.notes"
                rows="4"
                placeholder="Расскажите о себе, укажите количество проживающих, наличие домашних животных и т.д."
                class="form-textarea"
              ></textarea>
            </div>

            <div v-if="submitError" class="error-message">
              {{ submitError }}
            </div>

            <div class="modal-actions">
              <BaseButton
                type="button"
                variant="ghost"
                @click="closeApplicationModal"
                :disabled="submitting"
              >
                Отмена
              </BaseButton>
              <BaseButton
                type="submit"
                variant="primary"
                :loading="submitting"
              >
                Подать заявку
              </BaseButton>
            </div>
          </form>
        </BaseCard>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { propertiesAPI } from '@/api/services/properties'
import { applicationsAPI } from '@/api/services/applications'
import { useAuthStore } from '@/stores/auth'
import AppHeader from '@/components/layout/AppHeader.vue'
import BaseCard from '@/components/common/BaseCard.vue'
import BaseButton from '@/components/common/BaseButton.vue'
import BaseInput from '@/components/common/BaseInput.vue'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()

const property = ref(null)
const loading = ref(true)

// Application modal state
const showApplicationModal = ref(false)
const applicationForm = ref({
  preferred_move_in_date: '',
  lease_duration_months: 12,
  notes: ''
})
const submitting = ref(false)
const submitError = ref('')
const submitSuccess = ref(false)

onMounted(async () => {
  await loadProperty()
})

const loadProperty = async () => {
  loading.value = true
  try {
    const response = await propertiesAPI.getById(route.params.id)
    property.value = response.data
  } catch (error) {
    console.error('Failed to load property:', error)
  } finally {
    loading.value = false
  }
}

const applyForProperty = () => {
  // Check if user is authenticated
  if (!authStore.isAuthenticated) {
    router.push('/client/login')
    return
  }

  // Check if user is a client
  if (!authStore.isClient) {
    alert('Только клиенты могут подавать заявки на аренду')
    return
  }

  // Open application modal
  showApplicationModal.value = true
  submitError.value = ''
  submitSuccess.value = false
}

const closeApplicationModal = () => {
  showApplicationModal.value = false
  applicationForm.value = {
    preferred_move_in_date: '',
    lease_duration_months: 12,
    notes: ''
  }
  submitError.value = ''
  submitSuccess.value = false
}

const submitApplication = async () => {
  // Validation
  if (!applicationForm.value.preferred_move_in_date) {
    submitError.value = 'Пожалуйста, выберите дату заселения'
    return
  }

  if (!applicationForm.value.lease_duration_months || applicationForm.value.lease_duration_months < 1) {
    submitError.value = 'Пожалуйста, укажите срок аренды (минимум 1 месяц)'
    return
  }

  submitting.value = true
  submitError.value = ''

  try {
    const applicationData = {
      client_id: authStore.user?.client_id || authStore.user?.id || 1,
      property_id: parseInt(route.params.id),
      preferred_move_in_date: applicationForm.value.preferred_move_in_date,
      lease_duration_months: parseInt(applicationForm.value.lease_duration_months),
      notes: applicationForm.value.notes || null
    }

    await applicationsAPI.create(applicationData)
    submitSuccess.value = true

    // Close modal after 2 seconds and redirect
    setTimeout(() => {
      closeApplicationModal()
      router.push('/client/applications')
    }, 2000)
  } catch (error) {
    console.error('Failed to submit application:', error)
    submitError.value = error.response?.data?.detail || 'Не удалось подать заявку. Попробуйте снова.'
  } finally {
    submitting.value = false
  }
}

const formatMoney = (value) => {
  return new Intl.NumberFormat('ru-RU').format(value)
}

const getStatusText = (status) => {
  const map = {
    'available': 'Доступно',
    'reserved': 'Забронировано',
    'rented': 'Сдано',
    'maintenance': 'На обслуживании'
  }
  return map[status] || status
}

const getPropertyImage = (subtype) => {
  const imageMap = {
    'Квартира': 'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800&h=500&fit=crop',
    'Студия': 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800&h=500&fit=crop',
    'Пентхаус': 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800&h=500&fit=crop',
    'Таунхаус': 'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=800&h=500&fit=crop',
    'Коттедж': 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&h=500&fit=crop',
    'Офис': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&h=500&fit=crop',
    'Торговое помещение': 'https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=800&h=500&fit=crop'
  }
  return imageMap[subtype] || 'https://images.unsplash.com/photo-1560184897-ae75f418493e?w=800&h=500&fit=crop'
}

const getAmenities = (amenitiesString) => {
  return amenitiesString.split(',').map(a => a.trim())
}
</script>

<style scoped>
.property-detail-page {
  min-height: calc(100vh - var(--header-height));
  padding: var(--spacing-2xl) 0;
  background: var(--bg-primary);
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

.property-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: var(--spacing-2xl);
}

.property-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: var(--spacing-sm);
}

.property-address {
  font-size: 1.125rem;
  color: var(--text-secondary);
}

.status-badge {
  padding: 0.5rem 1rem;
  border-radius: var(--radius-lg);
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.875rem;
}

.status-available {
  background: rgba(34, 197, 94, 0.15);
  color: #22c55e;
}

.status-reserved {
  background: rgba(251, 191, 36, 0.15);
  color: #fbbf24;
}

.status-rented {
  background: rgba(239, 68, 68, 0.15);
  color: #ef4444;
}

.property-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: var(--spacing-xl);
  margin-bottom: var(--spacing-2xl);
}

.property-image-section {
  border-radius: var(--radius-xl);
  overflow: hidden;
}

.main-image {
  width: 100%;
  height: 500px;
  object-fit: cover;
}

.section-title {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: var(--spacing-lg);
  color: var(--text-primary);
}

.details-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--spacing-lg);
  margin-bottom: var(--spacing-xl);
}

.detail-item {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xs);
}

.detail-label {
  font-size: 0.875rem;
  color: var(--text-tertiary);
  text-transform: uppercase;
  font-weight: 500;
}

.detail-value {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--text-primary);
}

.price-section {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--spacing-lg);
  padding: var(--spacing-lg);
  background: var(--bg-tertiary);
  border-radius: var(--radius-lg);
  margin-bottom: var(--spacing-xl);
}

.price {
  font-size: 2rem;
  font-weight: 700;
  color: var(--primary-color);
}

.deposit {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--text-secondary);
}

.description {
  line-height: 1.8;
  color: var(--text-secondary);
  font-size: 1.0625rem;
}

.amenities-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--spacing-md);
}

.amenity-item {
  padding: var(--spacing-sm);
  color: var(--text-secondary);
  font-size: 1rem;
}

/* Modal Styles */
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
  backdrop-filter: blur(4px);
}

.modal-content {
  width: 100%;
  max-width: 600px;
  max-height: 90vh;
  overflow-y: auto;
  animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--spacing-xl);
  padding-bottom: var(--spacing-md);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.modal-header h2 {
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  color: var(--text-secondary);
  cursor: pointer;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: all 0.3s ease;
  line-height: 1;
  padding: 0;
}

.close-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  color: var(--text-primary);
}

.success-message {
  text-align: center;
  padding: 3rem 2rem;
}

.success-icon {
  width: 80px;
  height: 80px;
  margin: 0 auto 1.5rem;
  background: rgba(34, 197, 94, 0.15);
  color: #22c55e;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  font-weight: bold;
}

.success-message h3 {
  font-size: 1.5rem;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}

.success-message p {
  color: var(--text-secondary);
}

.application-form {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-lg);
}

.property-summary {
  padding: var(--spacing-lg);
  background: var(--bg-tertiary);
  border-radius: var(--radius-lg);
  border: 1px solid rgba(59, 130, 246, 0.2);
}

.property-summary h4 {
  font-size: 1.25rem;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}

.property-summary p {
  color: var(--text-secondary);
  margin-bottom: 0.25rem;
}

.property-summary .price {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary-color);
  margin-top: 0.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group label {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-primary);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.form-textarea {
  width: 100%;
  padding: 0.75rem;
  background: var(--bg-tertiary);
  border: 2px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-md);
  color: var(--text-primary);
  font-family: inherit;
  font-size: 1rem;
  resize: vertical;
  transition: all 0.3s ease;
}

.form-textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 4px var(--primary-glow);
}

.form-textarea::placeholder {
  color: var(--text-tertiary);
}

.error-message {
  padding: 0.75rem 1rem;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
  border-radius: var(--radius-md);
  color: #ef4444;
  font-size: 0.875rem;
}

.modal-actions {
  display: flex;
  gap: var(--spacing-md);
  justify-content: flex-end;
  margin-top: var(--spacing-md);
}

@media (max-width: 1024px) {
  .property-grid {
    grid-template-columns: 1fr;
  }

  .details-grid, .amenities-grid {
    grid-template-columns: 1fr;
  }

  .modal-actions {
    flex-direction: column-reverse;
  }

  .modal-actions button {
    width: 100%;
  }
}
</style>
