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
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { propertiesAPI } from '@/api/services/properties'
import AppHeader from '@/components/layout/AppHeader.vue'
import BaseCard from '@/components/common/BaseCard.vue'
import BaseButton from '@/components/common/BaseButton.vue'

const route = useRoute()
const router = useRouter()
const property = ref(null)
const loading = ref(true)

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
  router.push('/client/applications')
  alert('Функция подачи заявки в разработке')
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

@media (max-width: 1024px) {
  .property-grid {
    grid-template-columns: 1fr;
  }

  .details-grid, .amenities-grid {
    grid-template-columns: 1fr;
  }
}
</style>
