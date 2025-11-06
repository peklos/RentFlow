<template>
  <div>
    <AppHeader />

    <div class="properties-page">
      <div class="container">
        <h1 class="page-title">Доступные объекты</h1>

        <!-- Filters -->
        <BaseCard class="mb-xl">
          <h3 class="text-lg font-semibold mb-md">🔍 Фильтры поиска</h3>
          <div class="grid grid-cols-4 gap-md">
            <BaseInput v-model.number="filters.min_price" label="Мин. цена ₽" type="number" placeholder="от 30 000" />
            <BaseInput v-model.number="filters.max_price" label="Макс. цена ₽" type="number" placeholder="до 200 000" />
            <BaseInput v-model.number="filters.min_area" label="Мин. площадь м²" type="number" placeholder="от 30" />
            <BaseInput v-model.number="filters.max_area" label="Макс. площадь м²" type="number" placeholder="до 300" />
          </div>
          <div class="grid grid-cols-4 gap-md mt-md">
            <BaseInput v-model.number="filters.rooms_count" label="Количество комнат" type="number" placeholder="1, 2, 3..." />
            <BaseInput v-model.number="filters.floor" label="Этаж" type="number" placeholder="любой" />
            <BaseButton variant="secondary" @click="resetFilters" style="margin-top: 1.5rem;">
              Сбросить
            </BaseButton>
            <BaseButton variant="primary" @click="applyFilters" style="margin-top: 1.5rem;">
              Применить фильтры
            </BaseButton>
          </div>
        </BaseCard>

        <!-- Properties Grid -->
        <div v-if="loading" class="text-center">
          <div class="loader"></div>
        </div>

        <div v-else-if="properties.length === 0" class="text-center text-secondary">
          <p class="text-xl">Объекты не найдены</p>
        </div>

        <div v-else class="grid grid-cols-3 gap-lg">
          <BaseCard
            v-for="property in properties"
            :key="property.id"
            elevated
            class="property-card"
          >
            <div class="property-image">
              <img
                :src="getPropertyImage(property.subtype)"
                :alt="property.subtype"
              />
              <span class="badge badge-success property-status">{{ property.status }}</span>
            </div>

            <h3 class="text-xl font-semibold mt-md mb-sm">
              {{ property.subtype }}
            </h3>

            <p class="text-secondary mb-md">{{ property.address }}</p>

            <div class="property-details">
              <div class="detail-item">
                <span class="text-tertiary">Площадь:</span>
                <span class="font-medium">{{ property.area }} м²</span>
              </div>
              <div class="detail-item">
                <span class="text-tertiary">Комнат:</span>
                <span class="font-medium">{{ property.rooms_count || 'Н/Д' }}</span>
              </div>
              <div class="detail-item">
                <span class="text-tertiary">Этаж:</span>
                <span class="font-medium">{{ property.floor || 'Н/Д' }}</span>
              </div>
            </div>

            <div class="property-footer">
              <div class="property-price">
                <span class="text-tertiary">Цена:</span>
                <span class="text-2xl font-bold text-primary">
                  ₽{{ formatMoney(property.monthly_rent) }}/мес
                </span>
              </div>
              <router-link :to="`/properties/${property.id}`">
                <BaseButton variant="primary">Подробнее</BaseButton>
              </router-link>
            </div>
          </BaseCard>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { usePropertiesStore } from '@/stores/properties'
import AppHeader from '@/components/layout/AppHeader.vue'
import BaseCard from '@/components/common/BaseCard.vue'
import BaseInput from '@/components/common/BaseInput.vue'
import BaseButton from '@/components/common/BaseButton.vue'

const propertiesStore = usePropertiesStore()

const properties = ref([])
const loading = ref(false)
const filters = ref({
  min_price: null,
  max_price: null,
  min_area: null,
  max_area: null,
  rooms_count: null,
  floor: null
})

onMounted(async () => {
  await fetchProperties()
})

const fetchProperties = async () => {
  loading.value = true
  try {
    properties.value = await propertiesStore.fetchProperties()
  } catch (error) {
    console.error('Failed to fetch properties:', error)
  } finally {
    loading.value = false
  }
}

const applyFilters = async () => {
  loading.value = true
  try {
    properties.value = await propertiesStore.fetchProperties(filters.value)
  } catch (error) {
    console.error('Failed to apply filters:', error)
  } finally {
    loading.value = false
  }
}

const resetFilters = async () => {
  filters.value = {
    min_price: null,
    max_price: null,
    min_area: null,
    max_area: null,
    rooms_count: null,
    floor: null
  }
  await fetchProperties()
}

const formatMoney = (value) => {
  return new Intl.NumberFormat('ru-RU').format(value)
}

const getPropertyImage = (subtype) => {
  const imageMap = {
    'Квартира': 'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=400&h=250&fit=crop',
    'Студия': 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=400&h=250&fit=crop',
    'Пентхаус': 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=400&h=250&fit=crop',
    'Таунхаус': 'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=400&h=250&fit=crop',
    'Коттедж': 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=400&h=250&fit=crop',
    'Офис': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=400&h=250&fit=crop',
    'Торговое помещение': 'https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=400&h=250&fit=crop'
  }
  return imageMap[subtype] || 'https://images.unsplash.com/photo-1560184897-ae75f418493e?w=400&h=250&fit=crop'
}
</script>

<style scoped>
.properties-page {
  min-height: calc(100vh - var(--header-height));
  padding: var(--spacing-2xl) 0;
  background: var(--bg-primary);
}

.page-title {
  font-size: var(--font-size-4xl);
  font-weight: var(--font-weight-bold);
  margin-bottom: var(--spacing-2xl);
}

.property-card {
  display: flex;
  flex-direction: column;
  transition: transform var(--transition-base);
}

.property-card:hover {
  transform: translateY(-4px);
}

.property-image {
  position: relative;
  border-radius: var(--radius-md);
  overflow: hidden;
  margin-bottom: var(--spacing-md);
}

.property-image img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.property-status {
  position: absolute;
  top: var(--spacing-sm);
  right: var(--spacing-sm);
  text-transform: uppercase;
}

.property-details {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-sm);
  margin-bottom: var(--spacing-lg);
  padding: var(--spacing-md);
  background: var(--bg-tertiary);
  border-radius: var(--radius-md);
}

.detail-item {
  display: flex;
  justify-content: space-between;
}

.property-footer {
  margin-top: auto;
  padding-top: var(--spacing-md);
  border-top: 1px solid var(--border-color);
}

.property-price {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xs);
  margin-bottom: var(--spacing-md);
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xs);
}

.filter-label {
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  color: var(--text-secondary);
}

.filter-select {
  padding: 0.75rem;
  background: var(--bg-tertiary);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  color: var(--text-primary);
  font-size: var(--font-size-base);
  transition: all var(--transition-base);
  cursor: pointer;
}

.filter-select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px var(--primary-glow);
}

/* Remove arrows from number inputs */
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type="number"] {
  -moz-appearance: textfield;
}
</style>
