<template>
  <div>
    <AppHeader />
    <div class="services-page">
      <div class="container">
        <h1 class="page-title">Дополнительные услуги</h1>
        <p class="page-subtitle">Сделайте вашу аренду ещё комфортнее с нашими дополнительными услугами</p>

        <div v-if="loading" class="loading-state">
          <div class="loader"></div>
          <p>Загрузка услуг...</p>
        </div>

        <div v-else-if="services.length === 0" class="empty-state">
          <BaseCard elevated>
            <div class="empty-content">
              <div class="empty-icon">🛠️</div>
              <h3>Услуги временно недоступны</h3>
              <p>В данный момент дополнительные услуги не предоставляются</p>
            </div>
          </BaseCard>
        </div>

        <div v-else class="services-grid">
          <BaseCard v-for="service in services" :key="service.id" elevated class="service-card">
            <div class="service-icon">
              {{ getServiceIcon(service.name) }}
            </div>
            <h3 class="service-name">{{ service.name }}</h3>
            <p class="service-description">{{ service.description }}</p>
            <div class="service-footer">
              <div class="service-price">
                <span class="price-value">₽{{ formatMoney(service.price) }}</span>
                <span class="price-unit">{{ service.unit }}</span>
              </div>
              <BaseButton variant="primary" @click="orderService(service)">
                Заказать
              </BaseButton>
            </div>
          </BaseCard>
        </div>

        <!-- Order Modal -->
        <div v-if="showOrderModal" class="modal-overlay" @click.self="closeOrderModal">
          <div class="modal">
            <div class="modal-header">
              <h2>Заказ услуги</h2>
              <button class="close-btn" @click="closeOrderModal">×</button>
            </div>
            <div class="modal-body">
              <div v-if="selectedService" class="order-details">
                <div class="service-summary">
                  <div class="service-icon-large">{{ getServiceIcon(selectedService.name) }}</div>
                  <div>
                    <h3>{{ selectedService.name }}</h3>
                    <p class="text-secondary">{{ selectedService.description }}</p>
                  </div>
                </div>

                <div class="price-summary">
                  <div class="price-row">
                    <span>Стоимость:</span>
                    <span class="price-highlight">₽{{ formatMoney(selectedService.price) }} {{ selectedService.unit }}</span>
                  </div>
                </div>

                <form @submit.prevent="submitOrder" class="order-form">
                  <div class="form-group">
                    <label>Адрес предоставления услуги *</label>
                    <textarea
                      v-model="orderForm.address"
                      rows="2"
                      required
                      placeholder="Укажите адрес, где нужна услуга"
                    ></textarea>
                  </div>

                  <div class="form-group">
                    <label>Желаемая дата начала</label>
                    <input v-model="orderForm.start_date" type="date" :min="today" />
                  </div>

                  <div class="form-group">
                    <label>Комментарий</label>
                    <textarea
                      v-model="orderForm.notes"
                      rows="3"
                      placeholder="Дополнительные пожелания или информация"
                    ></textarea>
                  </div>

                  <div class="form-actions">
                    <BaseButton type="button" variant="secondary" @click="closeOrderModal">
                      Отмена
                    </BaseButton>
                    <BaseButton type="submit" variant="primary">
                      Подтвердить заказ
                    </BaseButton>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { servicesAPI } from '@/api/services/services'
import { useAuthStore } from '@/stores/auth'
import AppHeader from '@/components/layout/AppHeader.vue'
import BaseCard from '@/components/common/BaseCard.vue'
import BaseButton from '@/components/common/BaseButton.vue'

const authStore = useAuthStore()
const services = ref([])
const loading = ref(false)
const showOrderModal = ref(false)
const selectedService = ref(null)

const orderForm = ref({
  address: '',
  start_date: '',
  notes: ''
})

const today = computed(() => {
  const date = new Date()
  return date.toISOString().split('T')[0]
})

onMounted(async () => {
  await fetchServices()
})

const fetchServices = async () => {
  loading.value = true
  try {
    const response = await servicesAPI.getAll({ is_active: true })
    services.value = response.data
  } catch (error) {
    console.error('Failed to fetch services:', error)
  } finally {
    loading.value = false
  }
}

const formatMoney = (value) => {
  return new Intl.NumberFormat('ru-RU').format(value)
}

const getServiceIcon = (name) => {
  const iconMap = {
    'Уборка помещения': '🧹',
    'Парковочное место': '🅿️',
    'Интернет': '📡',
    'Аренда мебели': '🛋️',
    'Консьерж-сервис': '🎩',
    'Химчистка': '✨',
    'Кабельное ТВ': '📺',
    'Вывоз мусора': '🗑️',
    'Хранение вещей': '📦',
    'Доступ в спортзал': '💪'
  }
  return iconMap[name] || '🛠️'
}

const orderService = (service) => {
  if (!authStore.isAuthenticated) {
    alert('Пожалуйста, войдите в систему для заказа услуг')
    return
  }
  selectedService.value = service
  showOrderModal.value = true
}

const closeOrderModal = () => {
  showOrderModal.value = false
  selectedService.value = null
  orderForm.value = {
    address: '',
    start_date: '',
    notes: ''
  }
}

const submitOrder = async () => {
  try {
    // В будущем здесь будет реальный API запрос
    console.log('Заказ услуги:', {
      service_id: selectedService.value.id,
      ...orderForm.value
    })

    alert(`Заказ услуги "${selectedService.value.name}" успешно оформлен!\n\nМы свяжемся с вами в ближайшее время для уточнения деталей.`)
    closeOrderModal()
  } catch (error) {
    console.error('Ошибка при оформлении заказа:', error)
    alert('Произошла ошибка при оформлении заказа. Пожалуйста, попробуйте позже.')
  }
}
</script>

<style scoped>
.services-page {
  min-height: calc(100vh - var(--header-height));
  padding: var(--spacing-2xl) 0;
  background: var(--bg-primary);
}

.page-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: var(--spacing-sm);
  color: var(--text-primary);
}

.page-subtitle {
  font-size: 1.125rem;
  color: var(--text-secondary);
  margin-bottom: var(--spacing-2xl);
}

.loading-state {
  text-align: center;
  padding: 4rem 2rem;
  color: var(--text-secondary);
}

.loader {
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
  font-size: 1.125rem;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: var(--spacing-xl);
}

.service-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.service-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}

.service-icon {
  font-size: 3rem;
  margin-bottom: var(--spacing-md);
  text-align: center;
}

.service-name {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: var(--spacing-sm);
  color: var(--text-primary);
}

.service-description {
  color: var(--text-secondary);
  margin-bottom: var(--spacing-lg);
  line-height: 1.6;
  min-height: 3rem;
}

.service-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: var(--spacing-md);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.service-price {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.price-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary-color);
}

.price-unit {
  font-size: 0.875rem;
  color: var(--text-tertiary);
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
  transition: color 0.3s ease;
}

.close-btn:hover {
  color: var(--text-primary);
}

.modal-body {
  padding: 1.5rem;
}

.service-summary {
  display: flex;
  gap: 1rem;
  padding: 1.5rem;
  background: rgba(59, 130, 246, 0.1);
  border-radius: 12px;
  margin-bottom: 1.5rem;
}

.service-icon-large {
  font-size: 3rem;
}

.service-summary h3 {
  font-size: 1.25rem;
  color: var(--text-primary);
  margin: 0 0 0.5rem 0;
}

.price-summary {
  padding: 1rem;
  background: rgba(255, 255, 255, 0.03);
  border-radius: 8px;
  margin-bottom: 1.5rem;
}

.price-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 1.125rem;
}

.price-highlight {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary-color);
}

.order-form {
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
  .page-title {
    font-size: 2rem;
  }

  .services-grid {
    grid-template-columns: 1fr;
  }

  .service-footer {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }

  .service-footer button {
    width: 100%;
  }
}
</style>
