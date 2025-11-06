<template>
  <header class="app-header">
    <div class="header-container">
      <!-- Logo -->
      <router-link to="/" class="logo-section">
        <div class="logo-icon">
          <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect width="40" height="40" rx="10" fill="url(#gradient)"/>
            <path d="M12 28V16L20 10L28 16V28H23V21H17V28H12Z" fill="white"/>
            <defs>
              <linearGradient id="gradient" x1="0" y1="0" x2="40" y2="40">
                <stop stop-color="#3b82f6"/>
                <stop offset="1" stop-color="#2563eb"/>
              </linearGradient>
            </defs>
          </svg>
        </div>
        <div class="logo-text">
          <span class="logo-name">RentFlow</span>
          <span class="logo-tagline">Аренда недвижимости</span>
        </div>
      </router-link>

      <!-- Mobile Menu Toggle -->
      <button class="mobile-menu-toggle" @click="mobileMenuOpen = !mobileMenuOpen">
        <span></span>
        <span></span>
        <span></span>
      </button>

      <!-- Navigation -->
      <nav :class="['nav-menu', { 'mobile-open': mobileMenuOpen }]">
        <router-link to="/properties" class="nav-link" @click="mobileMenuOpen = false">
          <span class="nav-icon">🏢</span>
          Объекты
        </router-link>

        <template v-if="authStore.isAuthenticated">
          <template v-if="authStore.isClient">
            <!-- Client Dropdown -->
            <div class="nav-dropdown" @mouseenter="clientDropdownOpen = true" @mouseleave="clientDropdownOpen = false">
              <button class="nav-link dropdown-trigger">
                <span class="nav-icon">👤</span>
                Личный кабинет
                <span class="dropdown-arrow">▼</span>
              </button>
              <div :class="['dropdown-menu', { 'show': clientDropdownOpen }]">
                <router-link to="/client/profile" class="dropdown-item" @click="mobileMenuOpen = false">
                  <span class="dropdown-icon">👤</span>
                  Профиль
                </router-link>
                <router-link to="/client/applications" class="dropdown-item" @click="mobileMenuOpen = false">
                  <span class="dropdown-icon">📝</span>
                  Заявки
                </router-link>
                <router-link to="/client/contracts" class="dropdown-item" @click="mobileMenuOpen = false">
                  <span class="dropdown-icon">📄</span>
                  Договоры
                </router-link>
                <router-link to="/client/payments" class="dropdown-item" @click="mobileMenuOpen = false">
                  <span class="dropdown-icon">💳</span>
                  Платежи
                </router-link>
                <router-link to="/client/reviews" class="dropdown-item" @click="mobileMenuOpen = false">
                  <span class="dropdown-icon">⭐</span>
                  Отзывы
                </router-link>
                <router-link to="/client/services" class="dropdown-item" @click="mobileMenuOpen = false">
                  <span class="dropdown-icon">🛠️</span>
                  Услуги
                </router-link>
              </div>
            </div>
          </template>

          <template v-if="authStore.isEmployee">
            <!-- Admin Dropdown -->
            <div class="nav-dropdown" @mouseenter="adminDropdownOpen = true" @mouseleave="adminDropdownOpen = false">
              <button class="nav-link dropdown-trigger">
                <span class="nav-icon">⚙️</span>
                Управление
                <span class="dropdown-arrow">▼</span>
              </button>
              <div :class="['dropdown-menu', { 'show': adminDropdownOpen }]">
                <router-link to="/admin/dashboard" class="dropdown-item" @click="mobileMenuOpen = false">
                  <span class="dropdown-icon">📊</span>
                  Дашборд
                </router-link>
                <router-link to="/admin/properties" class="dropdown-item" @click="mobileMenuOpen = false">
                  <span class="dropdown-icon">🏢</span>
                  Объекты
                </router-link>
                <router-link to="/admin/clients" class="dropdown-item" @click="mobileMenuOpen = false">
                  <span class="dropdown-icon">👥</span>
                  Клиенты
                </router-link>
                <router-link to="/admin/applications" class="dropdown-item" @click="mobileMenuOpen = false">
                  <span class="dropdown-icon">📝</span>
                  Заявки
                </router-link>
                <router-link to="/admin/payments" class="dropdown-item" @click="mobileMenuOpen = false">
                  <span class="dropdown-icon">💰</span>
                  Платежи
                </router-link>
                <router-link to="/admin/reviews" class="dropdown-item" @click="mobileMenuOpen = false">
                  <span class="dropdown-icon">⭐</span>
                  Отзывы
                </router-link>
              </div>
            </div>

            <div class="nav-dropdown" @mouseenter="settingsDropdownOpen = true" @mouseleave="settingsDropdownOpen = false">
              <button class="nav-link dropdown-trigger">
                <span class="nav-icon">🔧</span>
                Справочники
                <span class="dropdown-arrow">▼</span>
              </button>
              <div :class="['dropdown-menu', { 'show': settingsDropdownOpen }]">
                <router-link to="/admin/companies" class="dropdown-item" @click="mobileMenuOpen = false">
                  <span class="dropdown-icon">🏢</span>
                  Компании
                </router-link>
                <router-link to="/admin/positions" class="dropdown-item" @click="mobileMenuOpen = false">
                  <span class="dropdown-icon">💼</span>
                  Должности
                </router-link>
                <router-link to="/admin/employees" class="dropdown-item" @click="mobileMenuOpen = false">
                  <span class="dropdown-icon">👔</span>
                  Сотрудники
                </router-link>
                <router-link to="/admin/services" class="dropdown-item" @click="mobileMenuOpen = false">
                  <span class="dropdown-icon">🛠️</span>
                  Услуги
                </router-link>
                <router-link to="/admin/verifications" class="dropdown-item" @click="mobileMenuOpen = false">
                  <span class="dropdown-icon">✅</span>
                  Верификации
                </router-link>
              </div>
            </div>
          </template>

          <BaseButton variant="ghost" @click="handleLogout" class="logout-btn">
            <span class="logout-icon">🚪</span>
            Выйти
          </BaseButton>
        </template>

        <template v-else>
          <router-link to="/client/login" @click="mobileMenuOpen = false">
            <BaseButton variant="outline" size="small">Войти</BaseButton>
          </router-link>
          <router-link to="/client/register" @click="mobileMenuOpen = false">
            <BaseButton variant="primary" size="small">Регистрация</BaseButton>
          </router-link>
        </template>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import BaseButton from '@/components/common/BaseButton.vue'

const authStore = useAuthStore()
const router = useRouter()

const mobileMenuOpen = ref(false)
const clientDropdownOpen = ref(false)
const adminDropdownOpen = ref(false)
const settingsDropdownOpen = ref(false)

const handleLogout = () => {
  authStore.logout()
  mobileMenuOpen.value = false
  router.push('/')
}
</script>

<style scoped>
.app-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(15, 23, 42, 0.95);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(59, 130, 246, 0.2);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

.header-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 2rem;
  height: var(--header-height, 70px);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 2rem;
}

/* Logo */
.logo-section {
  display: flex;
  align-items: center;
  gap: 1rem;
  text-decoration: none;
  transition: transform 0.3s ease;
}

.logo-section:hover {
  transform: scale(1.02);
}

.logo-icon {
  filter: drop-shadow(0 0 12px rgba(59, 130, 246, 0.6));
  transition: filter 0.3s ease;
}

.logo-section:hover .logo-icon {
  filter: drop-shadow(0 0 16px rgba(59, 130, 246, 0.8));
}

.logo-text {
  display: flex;
  flex-direction: column;
  gap: 0.125rem;
}

.logo-name {
  font-size: 1.5rem;
  font-weight: 700;
  background: linear-gradient(135deg, #3b82f6 0%, #60a5fa 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.logo-tagline {
  font-size: 0.625rem;
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 1px;
}

/* Mobile Menu Toggle */
.mobile-menu-toggle {
  display: none;
  flex-direction: column;
  gap: 4px;
  background: none;
  border: none;
  padding: 0.5rem;
  cursor: pointer;
  z-index: 101;
}

.mobile-menu-toggle span {
  width: 24px;
  height: 2px;
  background: var(--primary-color);
  transition: all 0.3s ease;
}

/* Navigation */
.nav-menu {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.625rem 1rem;
  color: var(--text-secondary);
  font-weight: 500;
  font-size: 0.9375rem;
  text-decoration: none;
  border-radius: 8px;
  transition: all 0.3s ease;
  background: none;
  border: none;
  cursor: pointer;
  white-space: nowrap;
}

.nav-link:hover {
  color: var(--primary-color);
  background: rgba(59, 130, 246, 0.1);
}

.nav-link.router-link-active {
  color: var(--primary-color);
  background: rgba(59, 130, 246, 0.15);
}

.nav-icon {
  font-size: 1.125rem;
}

/* Dropdown */
.nav-dropdown {
  position: relative;
}

.dropdown-trigger {
  cursor: pointer;
}

.dropdown-arrow {
  font-size: 0.625rem;
  transition: transform 0.3s ease;
}

.nav-dropdown:hover .dropdown-arrow {
  transform: rotate(180deg);
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  margin-top: 0.5rem;
  min-width: 200px;
  background: rgba(30, 41, 59, 0.98);
  border: 1px solid rgba(59, 130, 246, 0.2);
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(12px);
  opacity: 0;
  visibility: hidden;
  transform: translateY(-10px);
  transition: all 0.3s ease;
  overflow: hidden;
}

.dropdown-menu.show {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.dropdown-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1rem;
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 0.9375rem;
  transition: all 0.3s ease;
}

.dropdown-item:hover {
  color: var(--primary-color);
  background: rgba(59, 130, 246, 0.1);
}

.dropdown-item.router-link-active {
  color: var(--primary-color);
  background: rgba(59, 130, 246, 0.15);
}

.dropdown-icon {
  font-size: 1rem;
}

/* Logout Button */
.logout-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.logout-icon {
  font-size: 1.125rem;
}

/* Responsive */
@media (max-width: 1024px) {
  .header-container {
    padding: 0 1rem;
  }

  .mobile-menu-toggle {
    display: flex;
  }

  .nav-menu {
    position: fixed;
    top: 70px;
    left: 0;
    right: 0;
    flex-direction: column;
    align-items: stretch;
    background: rgba(15, 23, 42, 0.98);
    backdrop-filter: blur(12px);
    padding: 1rem;
    gap: 0.5rem;
    max-height: 0;
    overflow: hidden;
    opacity: 0;
    transition: all 0.3s ease;
    border-bottom: 1px solid rgba(59, 130, 246, 0.2);
  }

  .nav-menu.mobile-open {
    max-height: calc(100vh - 70px);
    opacity: 1;
    overflow-y: auto;
  }

  .nav-link {
    justify-content: flex-start;
    width: 100%;
  }

  .nav-dropdown {
    width: 100%;
  }

  .dropdown-menu {
    position: static;
    margin-top: 0.25rem;
    margin-left: 1rem;
    box-shadow: none;
    border: none;
    border-left: 2px solid rgba(59, 130, 246, 0.3);
    border-radius: 0;
  }

  .nav-dropdown:hover .dropdown-menu {
    opacity: 1;
    visibility: visible;
    transform: none;
  }

  .logo-tagline {
    display: none;
  }
}

@media (max-width: 768px) {
  .header-container {
    height: 60px;
  }

  .logo-name {
    font-size: 1.25rem;
  }

  .logo-icon svg {
    width: 32px;
    height: 32px;
  }

  .nav-menu {
    top: 60px;
  }
}
</style>
