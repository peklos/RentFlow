<template>
  <AdminLayout>
    <div class="reviews-manage">
      <div class="page-header">
        <div>
          <h1>Управление отзывами</h1>
          <p class="subtitle">Модерация отзывов клиентов</p>
        </div>
      </div>

      <div v-if="loading" class="loading-state">
        <div class="spinner"></div>
      </div>

      <div v-else class="reviews-list">
      <div v-for="review in reviews" :key="review.id" class="review-card">
        <div class="review-header">
          <div class="rating">
            <span v-for="i in 5" :key="i" :class="['star', { filled: i <= review.rating }]">★</span>
          </div>
          <span v-if="review.is_approved" class="badge badge-success">Одобрен</span>
          <span v-else class="badge badge-warning">На модерации</span>
        </div>
        <p class="review-text">{{ review.text }}</p>
        <div class="review-meta">
          <span class="text-tertiary">ID клиента: {{ review.client_id }}</span>
          <span class="text-tertiary">{{ formatDate(review.review_date) }}</span>
        </div>
        <div class="review-actions">
          <BaseButton v-if="!review.is_approved" variant="primary" size="small" @click="approveReview(review.id)">Одобрить</BaseButton>
          <BaseButton variant="danger" size="small" @click="deleteReview(review.id)">Удалить</BaseButton>
        </div>
      </div>
      </div>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { reviewsAPI } from '@/api/services/reviews'
import AdminLayout from '@/components/layout/AdminLayout.vue'
import BaseButton from '@/components/common/BaseButton.vue'

const reviews = ref([])
const loading = ref(true)

onMounted(() => {
  loadReviews()
})

const loadReviews = async () => {
  loading.value = true
  try {
    const response = await reviewsAPI.getAll()
    reviews.value = response.data
  } catch (error) {
    console.error('Error loading reviews:', error)
  } finally {
    loading.value = false
  }
}

const approveReview = async (id) => {
  try {
    await reviewsAPI.approve(id)
    await loadReviews()
  } catch (error) {
    console.error('Error approving review:', error)
  }
}

const deleteReview = async (id) => {
  if (!confirm('Удалить этот отзыв?')) return
  try {
    await reviewsAPI.delete(id)
    await loadReviews()
  } catch (error) {
    console.error('Error deleting review:', error)
  }
}

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('ru-RU')
}
</script>

<style scoped>
.reviews-manage {
  max-width: 1200px;
  margin: 0 auto;
}

.page-header h1 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  color: var(--text-primary);
}

.subtitle {
  color: var(--text-secondary);
  margin-bottom: 2rem;
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

.reviews-list {
  display: grid;
  gap: 1.5rem;
}

.review-card {
  background: var(--bg-secondary);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 1.5rem;
}

.review-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.rating {
  display: flex;
  gap: 0.25rem;
}

.star {
  font-size: 1.5rem;
  color: var(--text-tertiary);
}

.star.filled {
  color: #fbbf24;
}

.review-text {
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: 1rem;
}

.review-meta {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
  font-size: 0.875rem;
}

.review-actions {
  display: flex;
  gap: 0.75rem;
}
</style>
