<template>
  <div>
    <AppHeader />
    <div class="reviews-page">
      <div class="container">
        <div class="page-header">
          <h1 class="page-title">Мои отзывы</h1>
          <BaseButton variant="primary" @click="showCreateModal = true">+ Добавить отзыв</BaseButton>
        </div>

        <div v-if="loading" class="text-center">
          <div class="loader"></div>
        </div>

        <div v-else-if="reviews.length === 0" class="text-center text-secondary">
          <p class="text-xl">У вас пока нет отзывов</p>
        </div>

        <div v-else class="reviews-grid">
          <BaseCard v-for="review in reviews" :key="review.id" elevated>
            <div class="review-header">
              <div class="rating">
                <span v-for="i in 5" :key="i" :class="['star', { filled: i <= review.rating }]">★</span>
              </div>
              <span v-if="review.is_approved" class="badge badge-success">Одобрен</span>
              <span v-else class="badge badge-warning">На модерации</span>
            </div>
            <p class="review-text">{{ review.text }}</p>
            <p class="text-tertiary text-sm mt-md">{{ formatDate(review.review_date) }}</p>
          </BaseCard>
        </div>

        <!-- Create Modal -->
        <div v-if="showCreateModal" class="modal-overlay" @click.self="showCreateModal = false">
          <div class="modal">
            <div class="modal-header">
              <h2>Добавить отзыв</h2>
              <button class="close-btn" @click="showCreateModal = false">×</button>
            </div>
            <div class="modal-body">
              <form @submit.prevent="submitReview">
                <div class="form-group">
                  <label>Рейтинг *</label>
                  <div class="rating-input">
                    <span v-for="i in 5" :key="i" @click="reviewForm.rating = i"
                      :class="['star-input', { filled: i <= reviewForm.rating }]">★</span>
                  </div>
                </div>
                <div class="form-group">
                  <label>Отзыв *</label>
                  <textarea v-model="reviewForm.text" rows="4" required></textarea>
                </div>
                <div class="form-actions">
                  <BaseButton type="button" variant="secondary" @click="showCreateModal = false">Отмена</BaseButton>
                  <BaseButton type="submit" variant="primary">Отправить</BaseButton>
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
import { reviewsAPI } from '@/api/services/reviews'
import AppHeader from '@/components/layout/AppHeader.vue'
import BaseCard from '@/components/common/BaseCard.vue'
import BaseButton from '@/components/common/BaseButton.vue'

const reviews = ref([])
const loading = ref(false)
const showCreateModal = ref(false)

const reviewForm = ref({
  rating: 5,
  text: '',
  property_id: null
})

onMounted(async () => {
  await fetchReviews()
})

const fetchReviews = async () => {
  loading.value = true
  try {
    const response = await reviewsAPI.getMyReviews()
    reviews.value = response.data
  } catch (error) {
    console.error('Failed to fetch reviews:', error)
  } finally {
    loading.value = false
  }
}

const submitReview = async () => {
  try {
    await reviewsAPI.create(reviewForm.value)
    await fetchReviews()
    showCreateModal.value = false
    resetForm()
  } catch (error) {
    console.error('Failed to create review:', error)
    alert('Ошибка при создании отзыва')
  }
}

const resetForm = () => {
  reviewForm.value = { rating: 5, text: '', property_id: null }
}

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('ru-RU')
}
</script>

<style scoped>
.reviews-page {
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
  font-size: var(--font-size-4xl);
  font-weight: var(--font-weight-bold);
}

.reviews-grid {
  display: grid;
  gap: var(--spacing-lg);
}

.review-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--spacing-md);
}

.rating, .rating-input {
  display: flex;
  gap: 0.25rem;
}

.star, .star-input {
  font-size: 1.5rem;
  color: var(--text-tertiary);
}

.star.filled, .star-input.filled {
  color: #fbbf24;
}

.star-input {
  cursor: pointer;
  transition: all 0.2s ease;
}

.star-input:hover {
  transform: scale(1.2);
}

.review-text {
  color: var(--text-secondary);
  line-height: 1.6;
}

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

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.form-group label {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--text-secondary);
}

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
</style>
