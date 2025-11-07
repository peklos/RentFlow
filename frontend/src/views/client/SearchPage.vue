<template>
  <div>
    <AppHeader />
    <div class="search-page">
      <div class="container">
        <div class="search-header">
          <h1 class="page-title">🔍 Поиск</h1>
          <p class="page-subtitle">Найдите нужный раздел быстро и удобно</p>
        </div>

        <!-- Search Input -->
        <div class="search-box">
          <div class="search-input-wrapper">
            <svg class="search-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <circle cx="11" cy="11" r="8" stroke="currentColor" stroke-width="2"/>
              <path d="M21 21L16.65 16.65" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Введите что ищете: объекты, профиль, заявки..."
              class="search-input"
              @input="filterItems"
            />
            <button v-if="searchQuery" @click="clearSearch" class="clear-btn">×</button>
          </div>
        </div>

        <!-- Search History -->
        <div v-if="searchHistory.length > 0 && !searchQuery" class="search-history">
          <div class="history-header">
            <h3>📜 История поиска</h3>
            <button @click="clearHistory" class="clear-history-btn">Очистить</button>
          </div>
          <div class="history-items">
            <div
              v-for="(item, index) in searchHistory"
              :key="index"
              class="history-item"
              @click="navigateToItem(item)"
            >
              <span class="history-icon">🕐</span>
              <span class="history-text">{{ item.title }}</span>
              <span class="history-arrow">→</span>
            </div>
          </div>
        </div>

        <!-- Search Results -->
        <div class="search-results">
          <h2 class="results-title">
            {{ searchQuery ? 'Результаты поиска' : 'Все разделы' }}
          </h2>

          <div v-if="filteredItems.length === 0 && searchQuery" class="no-results">
            <div class="no-results-icon">🔍</div>
            <h3>Ничего не найдено</h3>
            <p>Попробуйте изменить запрос или выберите раздел из списка ниже</p>
          </div>

          <div class="results-grid">
            <BaseCard
              v-for="item in filteredItems"
              :key="item.path"
              elevated
              class="result-card"
              @click="navigateToItem(item)"
            >
              <div class="card-icon">{{ item.icon }}</div>
              <h3 class="card-title">{{ item.title }}</h3>
              <p class="card-description">{{ item.description }}</p>
              <div class="card-tags">
                <span v-for="tag in item.tags" :key="tag" class="tag">{{ tag }}</span>
              </div>
            </BaseCard>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import AppHeader from '@/components/layout/AppHeader.vue'
import BaseCard from '@/components/common/BaseCard.vue'

const router = useRouter()
const authStore = useAuthStore()
const searchQuery = ref('')
const searchHistory = ref([])

const allItems = computed(() => {
  const items = [
    {
      path: '/properties',
      icon: '🏢',
      title: 'Все объекты',
      description: 'Просмотр доступных объектов недвижимости для аренды',
      tags: ['недвижимость', 'аренда', 'квартиры', 'объекты'],
      requiresAuth: false
    }
  ]

  if (authStore.isAuthenticated && authStore.userRole === 'client') {
    items.push(
      {
        path: '/client/profile',
        icon: '👤',
        title: 'Мой профиль',
        description: 'Просмотр и редактирование личных данных, контактов',
        tags: ['профиль', 'данные', 'настройки', 'личный кабинет'],
        requiresAuth: true
      },
      {
        path: '/client/applications',
        icon: '📝',
        title: 'Мои заявки',
        description: 'Управление заявками на аренду, статусы заявок',
        tags: ['заявки', 'аренда', 'статус', 'подача'],
        requiresAuth: true
      },
      {
        path: '/client/contracts',
        icon: '📄',
        title: 'Мои договоры',
        description: 'Просмотр активных и завершенных договоров аренды',
        tags: ['договоры', 'контракты', 'аренда', 'документы'],
        requiresAuth: true
      },
      {
        path: '/client/payments',
        icon: '💳',
        title: 'Платежи',
        description: 'История платежей, оплата аренды',
        tags: ['платежи', 'оплата', 'деньги', 'счета'],
        requiresAuth: true
      },
      {
        path: '/client/services',
        icon: '🛠️',
        title: 'Дополнительные услуги',
        description: 'Заказ дополнительных услуг: уборка, парковка, интернет',
        tags: ['услуги', 'дополнительно', 'сервис', 'удобства'],
        requiresAuth: true
      },
      {
        path: '/client/reviews',
        icon: '⭐',
        title: 'Отзывы',
        description: 'Мои отзывы об объектах недвижимости',
        tags: ['отзывы', 'комментарии', 'рейтинг', 'оценки'],
        requiresAuth: true
      }
    )
  } else if (!authStore.isAuthenticated) {
    items.push(
      {
        path: '/client/login',
        icon: '🔐',
        title: 'Вход для клиентов',
        description: 'Войти в личный кабинет клиента',
        tags: ['вход', 'авторизация', 'логин', 'клиент'],
        requiresAuth: false
      },
      {
        path: '/client/register',
        icon: '📝',
        title: 'Регистрация',
        description: 'Создать новый аккаунт клиента',
        tags: ['регистрация', 'новый', 'аккаунт', 'создать'],
        requiresAuth: false
      },
      {
        path: '/employee/login',
        icon: '👔',
        title: 'Вход для сотрудников',
        description: 'Вход в панель управления для сотрудников',
        tags: ['сотрудники', 'админ', 'управление', 'панель'],
        requiresAuth: false
      }
    )
  }

  if (authStore.isAuthenticated && authStore.userRole === 'employee') {
    items.push(
      {
        path: '/admin/dashboard',
        icon: '📊',
        title: 'Панель управления',
        description: 'Обзор статистики и управление системой',
        tags: ['панель', 'админ', 'статистика', 'управление'],
        requiresAuth: true
      },
      {
        path: '/admin/properties',
        icon: '🏢',
        title: 'Управление объектами',
        description: 'Добавление и редактирование объектов недвижимости',
        tags: ['объекты', 'недвижимость', 'управление', 'админ'],
        requiresAuth: true
      },
      {
        path: '/admin/applications',
        icon: '📋',
        title: 'Управление заявками',
        description: 'Обработка заявок клиентов на аренду',
        tags: ['заявки', 'обработка', 'клиенты', 'админ'],
        requiresAuth: true
      },
      {
        path: '/admin/clients',
        icon: '👥',
        title: 'Управление клиентами',
        description: 'Просмотр и управление данными клиентов',
        tags: ['клиенты', 'пользователи', 'управление', 'админ'],
        requiresAuth: true
      }
    )
  }

  return items
})

const filteredItems = computed(() => {
  if (!searchQuery.value) return allItems.value

  const query = searchQuery.value.toLowerCase()
  return allItems.value.filter(item => {
    return (
      item.title.toLowerCase().includes(query) ||
      item.description.toLowerCase().includes(query) ||
      item.tags.some(tag => tag.toLowerCase().includes(query))
    )
  })
})

onMounted(() => {
  loadSearchHistory()
})

const loadSearchHistory = () => {
  const history = localStorage.getItem('rentflow_search_history')
  if (history) {
    try {
      searchHistory.value = JSON.parse(history)
    } catch (e) {
      searchHistory.value = []
    }
  }
}

const saveToHistory = (item) => {
  // Remove duplicates
  searchHistory.value = searchHistory.value.filter(h => h.path !== item.path)

  // Add to beginning
  searchHistory.value.unshift({
    path: item.path,
    title: item.title,
    icon: item.icon
  })

  // Keep only last 5 items
  searchHistory.value = searchHistory.value.slice(0, 5)

  // Save to localStorage
  localStorage.setItem('rentflow_search_history', JSON.stringify(searchHistory.value))
}

const navigateToItem = (item) => {
  saveToHistory(item)
  router.push(item.path)
}

const clearSearch = () => {
  searchQuery.value = ''
}

const clearHistory = () => {
  searchHistory.value = []
  localStorage.removeItem('rentflow_search_history')
}

const filterItems = () => {
  // Filtering happens in computed property
}
</script>

<style scoped>
.search-page {
  min-height: calc(100vh - var(--header-height));
  padding: var(--spacing-2xl) 0;
  background: var(--bg-primary);
}

.search-header {
  text-align: center;
  margin-bottom: var(--spacing-2xl);
}

.page-title {
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: var(--spacing-sm);
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.page-subtitle {
  font-size: 1.25rem;
  color: var(--text-secondary);
}

/* Search Box */
.search-box {
  max-width: 800px;
  margin: 0 auto var(--spacing-2xl);
}

.search-input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  background: var(--bg-secondary);
  border: 2px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  padding: 0 1.5rem;
  transition: all 0.3s ease;
}

.search-input-wrapper:focus-within {
  border-color: var(--primary-color);
  box-shadow: 0 0 0 4px var(--primary-glow);
}

.search-icon {
  color: var(--text-tertiary);
  margin-right: 1rem;
  flex-shrink: 0;
}

.search-input {
  flex: 1;
  background: none;
  border: none;
  padding: 1.25rem 0;
  font-size: 1.125rem;
  color: var(--text-primary);
  outline: none;
}

.search-input::placeholder {
  color: var(--text-tertiary);
}

.clear-btn {
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: var(--text-secondary);
  font-size: 2rem;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  padding: 0;
  line-height: 1;
}

.clear-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  color: var(--text-primary);
}

/* Search History */
.search-history {
  max-width: 800px;
  margin: 0 auto var(--spacing-2xl);
  background: var(--bg-secondary);
  border-radius: 16px;
  padding: 1.5rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.history-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.history-header h3 {
  font-size: 1.125rem;
  color: var(--text-primary);
  margin: 0;
}

.clear-history-btn {
  background: none;
  border: none;
  color: var(--text-tertiary);
  cursor: pointer;
  font-size: 0.875rem;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.clear-history-btn:hover {
  background: rgba(255, 255, 255, 0.05);
  color: var(--text-secondary);
}

.history-items {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.history-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.03);
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.history-item:hover {
  background: rgba(59, 130, 246, 0.1);
  transform: translateX(4px);
}

.history-icon {
  font-size: 1.5rem;
}

.history-text {
  flex: 1;
  color: var(--text-primary);
  font-size: 1rem;
}

.history-arrow {
  color: var(--text-tertiary);
  font-size: 1.25rem;
}

/* Search Results */
.search-results {
  max-width: 1200px;
  margin: 0 auto;
}

.results-title {
  font-size: 1.75rem;
  font-weight: 700;
  margin-bottom: var(--spacing-xl);
  color: var(--text-primary);
}

.no-results {
  text-align: center;
  padding: 4rem 2rem;
}

.no-results-icon {
  font-size: 5rem;
  margin-bottom: 1rem;
  opacity: 0.5;
}

.no-results h3 {
  font-size: 1.5rem;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}

.no-results p {
  color: var(--text-secondary);
  font-size: 1.125rem;
}

.results-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: var(--spacing-lg);
}

.result-card {
  cursor: pointer;
  transition: all 0.3s ease;
}

.result-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.3);
}

.card-icon {
  font-size: 3rem;
  margin-bottom: var(--spacing-md);
}

.card-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: var(--spacing-sm);
}

.card-description {
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: var(--spacing-md);
  min-height: 3rem;
}

.card-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  padding: 0.25rem 0.75rem;
  background: rgba(59, 130, 246, 0.15);
  border: 1px solid rgba(59, 130, 246, 0.3);
  border-radius: 12px;
  font-size: 0.75rem;
  color: var(--primary-color);
  font-weight: 500;
}

/* Responsive */
@media (max-width: 768px) {
  .page-title {
    font-size: 2rem;
  }

  .search-input {
    font-size: 1rem;
    padding: 1rem 0;
  }

  .results-grid {
    grid-template-columns: 1fr;
  }

  .search-input::placeholder {
    font-size: 0.875rem;
  }
}
</style>
