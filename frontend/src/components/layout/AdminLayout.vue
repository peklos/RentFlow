<template>
  <div class="admin-layout">
    <AppHeader />
    <div class="admin-container">
      <!-- Sidebar -->
      <aside class="admin-sidebar">
        <div class="sidebar-header">
          <h2>Панель администратора</h2>
        </div>

        <nav class="sidebar-nav">
          <router-link to="/admin/dashboard" class="nav-item">
            <span class="nav-icon">📊</span>
            <span class="nav-text">Дашборд</span>
          </router-link>

          <div class="nav-section">
            <div class="section-title">Управление</div>
            <router-link to="/admin/properties" class="nav-item">
              <span class="nav-icon">🏢</span>
              <span class="nav-text">Объекты</span>
            </router-link>
            <router-link to="/admin/clients" class="nav-item">
              <span class="nav-icon">👥</span>
              <span class="nav-text">Клиенты</span>
            </router-link>
            <router-link to="/admin/applications" class="nav-item">
              <span class="nav-icon">📝</span>
              <span class="nav-text">Заявки</span>
            </router-link>
            <router-link to="/admin/payments" class="nav-item">
              <span class="nav-icon">💰</span>
              <span class="nav-text">Платежи</span>
            </router-link>
            <router-link to="/admin/reviews" class="nav-item">
              <span class="nav-icon">⭐</span>
              <span class="nav-text">Отзывы</span>
            </router-link>
          </div>

          <div class="nav-section">
            <div class="section-title">Справочники</div>
            <router-link to="/admin/companies" class="nav-item">
              <span class="nav-icon">🏢</span>
              <span class="nav-text">Компании</span>
            </router-link>
            <router-link to="/admin/positions" class="nav-item">
              <span class="nav-icon">💼</span>
              <span class="nav-text">Должности</span>
            </router-link>
            <router-link to="/admin/employees" class="nav-item">
              <span class="nav-icon">👔</span>
              <span class="nav-text">Сотрудники</span>
            </router-link>
            <router-link to="/admin/services" class="nav-item">
              <span class="nav-icon">🛠️</span>
              <span class="nav-text">Услуги</span>
            </router-link>
            <router-link to="/admin/verifications" class="nav-item">
              <span class="nav-icon">✅</span>
              <span class="nav-text">Верификации</span>
            </router-link>
          </div>
        </nav>
      </aside>

      <!-- Main Content -->
      <main class="admin-content">
        <slot />
      </main>
    </div>
  </div>
</template>

<script setup>
import AppHeader from './AppHeader.vue'
</script>

<style scoped>
.admin-layout {
  min-height: 100vh;
  background: var(--bg-primary);
}

.admin-container {
  display: flex;
  min-height: calc(100vh - var(--header-height, 70px));
}

/* Sidebar */
.admin-sidebar {
  width: 260px;
  background: var(--bg-secondary);
  border-right: 1px solid rgba(255, 255, 255, 0.1);
  padding: 1.5rem 0;
  position: sticky;
  top: var(--header-height, 70px);
  height: calc(100vh - var(--header-height, 70px));
  overflow-y: auto;
}

.sidebar-header {
  padding: 0 1.5rem 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.sidebar-header h2 {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0;
}

.sidebar-nav {
  padding: 1rem 0;
}

.nav-section {
  margin-bottom: 1.5rem;
}

.section-title {
  padding: 0.5rem 1.5rem;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--text-tertiary);
  margin-bottom: 0.5rem;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1.5rem;
  color: var(--text-secondary);
  text-decoration: none;
  transition: all 0.3s ease;
  border-left: 3px solid transparent;
}

.nav-item:hover {
  background: rgba(59, 130, 246, 0.1);
  color: var(--primary-color);
  border-left-color: var(--primary-color);
}

.nav-item.router-link-active {
  background: rgba(59, 130, 246, 0.15);
  color: var(--primary-color);
  border-left-color: var(--primary-color);
  font-weight: 600;
}

.nav-icon {
  font-size: 1.25rem;
  width: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.nav-text {
  font-size: 0.9375rem;
}

/* Main Content */
.admin-content {
  flex: 1;
  padding: 2rem;
  overflow-x: hidden;
}

/* Scrollbar */
.admin-sidebar::-webkit-scrollbar {
  width: 6px;
}

.admin-sidebar::-webkit-scrollbar-track {
  background: transparent;
}

.admin-sidebar::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 3px;
}

.admin-sidebar::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.2);
}

/* Responsive */
@media (max-width: 1024px) {
  .admin-sidebar {
    width: 220px;
  }

  .admin-content {
    padding: 1.5rem;
  }
}

@media (max-width: 768px) {
  .admin-container {
    flex-direction: column;
  }

  .admin-sidebar {
    width: 100%;
    height: auto;
    position: static;
    border-right: none;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  }

  .admin-content {
    padding: 1rem;
  }

  .nav-item {
    padding: 0.625rem 1rem;
  }

  .section-title {
    padding: 0.5rem 1rem;
  }
}
</style>
