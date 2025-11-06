<template>
  <div>
    <AppHeader />

    <div class="properties-page">
      <div class="container">
        <h1 class="page-title">Доступные объекты</h1>

        <!-- Filters -->
        <BaseCard class="mb-xl">
          <div class="grid grid-cols-4 gap-md">
            <BaseInput v-model="filters.type" label="Тип" placeholder="Все" />
            <BaseInput v-model="filters.min_price" label="Мин. цена" type="number" />
            <BaseInput v-model="filters.max_price" label="Макс. цена" type="number" />
            <BaseButton variant="primary" @click="applyFilters" style="margin-top: 1.5rem;">
              Применить
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
                src="https://via.placeholder.com/400x250/1e293b/3b82f6?text=Property"
                alt="Property"
              />
              <span class="badge badge-success property-status">{{ property.status }}</span>
            </div>

            <h3 class="text-xl font-semibold mt-md mb-sm">
              Недвижимость {{ property.type }}
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
  type: '',
  min_price: '',
  max_price: ''
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

const formatMoney = (value) => {
  return new Intl.NumberFormat('ru-RU').format(value)
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
</style>
