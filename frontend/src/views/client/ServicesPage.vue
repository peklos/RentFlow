<template>
  <div>
    <AppHeader />
    <div class="services-page">
      <div class="container">
        <h1 class="page-title">Дополнительные услуги</h1>

        <div v-if="loading" class="text-center">
          <div class="loader"></div>
        </div>

        <div v-else-if="services.length === 0" class="text-center text-secondary">
          <p class="text-xl">Услуги не найдены</p>
        </div>

        <div v-else class="services-grid">
          <BaseCard v-for="service in services" :key="service.id" elevated>
            <h3 class="text-xl font-semibold mb-sm">{{ service.name }}</h3>
            <p class="text-secondary mb-md">{{ service.description }}</p>
            <div class="service-footer">
              <div class="service-price">
                <span class="text-2xl font-bold text-primary">₽{{ formatMoney(service.price) }}</span>
                <span class="text-tertiary">/ {{ service.unit }}</span>
              </div>
              <BaseButton variant="primary">Заказать</BaseButton>
            </div>
          </BaseCard>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { servicesAPI } from '@/api/services/services'
import AppHeader from '@/components/layout/AppHeader.vue'
import BaseCard from '@/components/common/BaseCard.vue'
import BaseButton from '@/components/common/BaseButton.vue'

const services = ref([])
const loading = ref(false)

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
</script>

<style scoped>
.services-page {
  min-height: calc(100vh - var(--header-height));
  padding: var(--spacing-2xl) 0;
  background: var(--bg-primary);
}

.page-title {
  font-size: var(--font-size-4xl);
  font-weight: var(--font-weight-bold);
  margin-bottom: var(--spacing-2xl);
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: var(--spacing-lg);
}

.service-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: var(--spacing-lg);
  padding-top: var(--spacing-md);
  border-top: 1px solid var(--border-color);
}

.service-price {
  display: flex;
  align-items: baseline;
  gap: var(--spacing-xs);
}
</style>
