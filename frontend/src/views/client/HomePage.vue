<template>
  <div>
    <AppHeader />

    <!-- Hero Section -->
    <section class="hero-section">
      <div class="container">
        <div class="hero-content">
          <h1 class="hero-title">
            Найдите идеальную
            <span class="text-gradient">недвижимость для аренды</span>
          </h1>
          <p class="hero-subtitle">
            Тысячи проверенных объектов для аренды. Современно, удобно и без лишних хлопот.
          </p>
          <div class="hero-actions">
            <router-link to="/properties">
              <BaseButton variant="primary" size="lg">Смотреть объекты</BaseButton>
            </router-link>
            <router-link to="/client/register">
              <BaseButton variant="outline" size="lg">Начать</BaseButton>
            </router-link>
          </div>
        </div>

        <!-- Search Box -->
        <div class="search-box card-elevated">
          <div class="grid grid-cols-4 gap-md">
            <div class="filter-group">
              <label class="filter-label">Локация</label>
              <select class="filter-select">
                <option value="">Все локации</option>
                <option value="Москва, Арбат">Москва, Арбат</option>
                <option value="Москва, Ленинский проспект">Москва, Ленинский проспект</option>
                <option value="Москва, Бауманская">Москва, Бауманская</option>
                <option value="Москва, Кутузовский проспект">Москва, Кутузовский проспект</option>
                <option value="Москва, Проспект Мира">Москва, Проспект Мира</option>
                <option value="Москва, Москва-Сити">Москва, Москва-Сити</option>
              </select>
            </div>
            <BaseInput placeholder="50 000" label="Мин. цена" type="number" />
            <BaseInput placeholder="2" label="Комнат" type="number" />
            <BaseButton variant="primary" style="margin-top: 1.5rem;">
              Искать
            </BaseButton>
          </div>
        </div>
      </div>
    </section>

    <!-- Features -->
    <section class="features-section">
      <div class="container">
        <h2 class="section-title text-center">Почему выбирают RentFlow?</h2>
        <div class="grid grid-cols-3 gap-lg">
          <BaseCard elevated>
            <div class="feature-icon">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 9L12 2L21 9V20C21 20.5304 20.7893 21.0391 20.4142 21.4142C20.0391 21.7893 19.5304 22 19 22H5C4.46957 22 3.96086 21.7893 3.58579 21.4142C3.21071 21.0391 3 20.5304 3 20V9Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M9 22V12H15V22" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold mb-sm">Широкий выбор</h3>
            <p class="text-secondary">
              Тысячи проверенных объектов недвижимости в разных локациях. От студий до элитных квартир.
            </p>
          </BaseCard>
          <BaseCard elevated>
            <div class="feature-icon">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold mb-sm">Быстрое одобрение</h3>
            <p class="text-secondary">
              Подайте заявку онлайн и получите одобрение в течение 24 часов. Просто и быстро.
            </p>
          </BaseCard>
          <BaseCard elevated>
            <div class="feature-icon">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M7 11V7C7 5.67392 7.52678 4.40215 8.46447 3.46447C9.40215 2.52678 10.6739 2 12 2C13.3261 2 14.5979 2.52678 15.5355 3.46447C16.4732 4.40215 17 5.67392 17 7V11" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold mb-sm">Безопасно</h3>
            <p class="text-secondary">
              Все объекты проверены. Ваши данные и платежи полностью защищены.
            </p>
          </BaseCard>
        </div>
      </div>
    </section>

    <!-- Stats Section with Wave -->
    <section class="stats-section">
      <!-- Wave SVG -->
      <div class="wave-top">
        <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
          <path d="M0,0V46.29c47.79,22.2,103.59,32.17,158,28,70.36-5.37,136.33-33.31,206.8-37.5C438.64,32.43,512.34,53.67,583,72.05c69.27,18,138.3,24.88,209.4,13.08,36.15-6,69.85-17.84,104.45-29.34C989.49,25,1113-14.29,1200,52.47V0Z" fill="currentColor"></path>
        </svg>
      </div>

      <div class="container stats-container">
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-number">1000+</div>
            <div class="stat-label">Объектов недвижимости</div>
          </div>
          <div class="stat-card">
            <div class="stat-number">5000+</div>
            <div class="stat-label">Довольных клиентов</div>
          </div>
          <div class="stat-card">
            <div class="stat-number">98%</div>
            <div class="stat-label">Положительных отзывов</div>
          </div>
          <div class="stat-card">
            <div class="stat-number">24/7</div>
            <div class="stat-label">Поддержка клиентов</div>
          </div>
        </div>
      </div>

      <!-- Wave SVG Bottom -->
      <div class="wave-bottom">
        <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
          <path d="M0,0V46.29c47.79,22.2,103.59,32.17,158,28,70.36-5.37,136.33-33.31,206.8-37.5C438.64,32.43,512.34,53.67,583,72.05c69.27,18,138.3,24.88,209.4,13.08,36.15-6,69.85-17.84,104.45-29.34C989.49,25,1113-14.29,1200,52.47V0Z" fill="currentColor"></path>
        </svg>
      </div>
    </section>

    <footer class="app-footer text-center">
      <p class="text-secondary">&copy; 2025 RentFlow. Все права защищены.</p>
    </footer>
  </div>
</template>

<script setup>
import AppHeader from '@/components/layout/AppHeader.vue'
import BaseButton from '@/components/common/BaseButton.vue'
import BaseInput from '@/components/common/BaseInput.vue'
import BaseCard from '@/components/common/BaseCard.vue'
</script>

<style scoped>
.hero-section {
  padding: 4rem 0 6rem;
  background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
  position: relative;
  overflow: hidden;
}

.hero-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at 20% 50%, rgba(59, 130, 246, 0.1) 0%, transparent 50%),
              radial-gradient(circle at 80% 80%, rgba(6, 182, 212, 0.1) 0%, transparent 50%);
  pointer-events: none;
}

.hero-content {
  text-align: center;
  margin-bottom: 3rem;
  position: relative;
  z-index: 1;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 800;
  margin-bottom: var(--spacing-lg);
  line-height: 1.1;
  letter-spacing: -0.02em;
}

.text-gradient {
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  display: inline-block;
}

.hero-subtitle {
  font-size: 1.25rem;
  color: var(--text-secondary);
  max-width: 650px;
  margin: 0 auto var(--spacing-2xl);
  line-height: 1.6;
}

.hero-actions {
  display: flex;
  gap: var(--spacing-md);
  justify-content: center;
}

.search-box {
  max-width: 900px;
  margin: 0 auto;
  padding: var(--spacing-xl);
  position: relative;
  z-index: 1;
  background: rgba(30, 41, 59, 0.8);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.features-section {
  padding: 5rem 0;
  background: var(--bg-primary);
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: var(--spacing-2xl);
  letter-spacing: -0.01em;
}

.feature-icon {
  width: 64px;
  height: 64px;
  margin: 0 auto var(--spacing-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  border-radius: var(--radius-xl);
  color: white;
  box-shadow: 0 8px 16px rgba(59, 130, 246, 0.3);
}

/* Stats Section with Waves */
.stats-section {
  position: relative;
  background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
  padding: 0;
  overflow: hidden;
}

.wave-top {
  position: relative;
  width: 100%;
  height: 120px;
  color: var(--bg-primary);
  margin-bottom: -1px;
}

.wave-top svg {
  width: 100%;
  height: 100%;
  display: block;
}

.wave-bottom {
  position: relative;
  width: 100%;
  height: 120px;
  color: var(--bg-primary);
  transform: rotate(180deg);
  margin-top: -1px;
}

.wave-bottom svg {
  width: 100%;
  height: 100%;
  display: block;
}

.stats-container {
  padding: 4rem 0;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
}

.stat-card {
  text-align: center;
  padding: 2rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: var(--radius-xl);
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-8px);
  background: rgba(255, 255, 255, 0.08);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
}

.stat-number {
  font-size: 3rem;
  font-weight: 800;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.5rem;
  line-height: 1;
}

.stat-label {
  font-size: 1rem;
  color: var(--text-secondary);
  font-weight: 500;
}

@media (max-width: 1024px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
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
  border: 1px solid rgba(255, 255, 255, 0.1);
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

@media (max-width: 768px) {
  .hero-title {
    font-size: 2.5rem;
  }

  .hero-subtitle {
    font-size: 1.125rem;
  }

  .grid-cols-3,
  .grid-cols-4 {
    grid-template-columns: 1fr;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .stat-card {
    padding: 1.5rem;
  }

  .stat-number {
    font-size: 2.5rem;
  }

  .wave-top,
  .wave-bottom {
    height: 60px;
  }
}
</style>
