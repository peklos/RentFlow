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
            <!-- Для залогиненных пользователей -->
            <template v-if="authStore.isAuthenticated">
              <router-link to="/properties">
                <BaseButton variant="primary" size="lg">Все объекты</BaseButton>
              </router-link>
              <router-link to="/client/applications">
                <BaseButton variant="outline" size="lg">Мои заявки</BaseButton>
              </router-link>
            </template>
            <!-- Для незалогиненных -->
            <template v-else>
              <router-link to="/client/login">
                <BaseButton variant="primary" size="lg">Вход для клиентов</BaseButton>
              </router-link>
              <router-link to="/employee/login">
                <BaseButton variant="outline" size="lg">Вход для сотрудников</BaseButton>
              </router-link>
            </template>
          </div>

          <div class="help-button-container">
            <BaseButton variant="secondary" size="md" @click="showGuideModal = true">
              📖 Справочник
            </BaseButton>
          </div>
        </div>
      </div>
    </section>

    <!-- Guide Modal -->
    <div v-if="showGuideModal" class="modal-overlay" @click.self="showGuideModal = false">
      <div class="modal-guide">
        <div class="modal-header">
          <h2>📖 Справочник по использованию RentFlow</h2>
          <button class="close-btn" @click="showGuideModal = false">×</button>
        </div>
        <div class="modal-body">
          <div class="guide-section">
            <h3>👋 Добро пожаловать!</h3>
            <p>Этот справочник поможет вам быстро разобраться в работе с нашим сайтом. Мы подготовили пошаговые инструкции для каждого действия.</p>
          </div>

          <div class="guide-section">
            <h3>🚀 Начало работы</h3>
            <div class="guide-step">
              <div class="step-number">1</div>
              <div class="step-content">
                <h4>Регистрация на сайте</h4>
                <p>Нажмите кнопку "Вход для клиентов" на главной странице, затем выберите "Регистрация". Заполните форму с вашими данными: телефон, email и придумайте пароль.</p>
              </div>
            </div>
            <div class="guide-step">
              <div class="step-number">2</div>
              <div class="step-content">
                <h4>Вход в систему</h4>
                <p>После регистрации введите ваш номер телефона и пароль на странице входа. Нажмите кнопку "Войти".</p>
              </div>
            </div>
          </div>

          <div class="guide-section">
            <h3>🏠 Поиск и аренда недвижимости</h3>
            <div class="guide-step">
              <div class="step-number">3</div>
              <div class="step-content">
                <h4>Просмотр объектов</h4>
                <p>Перейдите в раздел "Все объекты" через главное меню. Вы увидите список доступной недвижимости с фотографиями и ценами.</p>
              </div>
            </div>
            <div class="guide-step">
              <div class="step-number">4</div>
              <div class="step-content">
                <h4>Детали объекта</h4>
                <p>Нажмите на любой объект, чтобы увидеть подробную информацию: количество комнат, площадь, этаж, удобства и стоимость аренды.</p>
              </div>
            </div>
            <div class="guide-step">
              <div class="step-number">5</div>
              <div class="step-content">
                <h4>Подача заявки</h4>
                <p>Если объект вам подходит, нажмите кнопку "Подать заявку на аренду". Заполните форму с датой заселения и сроком аренды.</p>
              </div>
            </div>
          </div>

          <div class="guide-section">
            <h3>📋 Управление заявками и договорами</h3>
            <div class="guide-step">
              <div class="step-number">6</div>
              <div class="step-content">
                <h4>Отслеживание заявок</h4>
                <p>В разделе "Мои заявки" вы можете видеть статус всех ваших заявок: на рассмотрении, одобрена или отклонена.</p>
              </div>
            </div>
            <div class="guide-step">
              <div class="step-number">7</div>
              <div class="step-content">
                <h4>Просмотр договоров</h4>
                <p>После одобрения заявки в разделе "Мои договоры" появится договор аренды. Здесь вы найдете все условия аренды и сроки оплаты.</p>
              </div>
            </div>
          </div>

          <div class="guide-section">
            <h3>💳 Оплата и платежи</h3>
            <div class="guide-step">
              <div class="step-number">8</div>
              <div class="step-content">
                <h4>Оплата аренды</h4>
                <p>В разделе "Платежи" вы можете оплатить арендную плату. Выберите договор и нажмите "Оплатить". Оплата проходит безопасно через защищенный канал.</p>
              </div>
            </div>
          </div>

          <div class="guide-section">
            <h3>⭐ Дополнительные возможности</h3>
            <div class="guide-step">
              <div class="step-number">9</div>
              <div class="step-content">
                <h4>Дополнительные услуги</h4>
                <p>В разделе "Услуги" можно заказать дополнительные услуги: уборку, парковку, интернет и другие удобства.</p>
              </div>
            </div>
            <div class="guide-step">
              <div class="step-number">10</div>
              <div class="step-content">
                <h4>Оставить отзыв</h4>
                <p>После проживания вы можете оставить отзыв в разделе "Отзывы". Это поможет другим клиентам сделать выбор.</p>
              </div>
            </div>
            <div class="guide-step">
              <div class="step-number">11</div>
              <div class="step-content">
                <h4>Профиль</h4>
                <p>В разделе "Профиль" вы можете обновить свои личные данные, контакты и информацию о работе.</p>
              </div>
            </div>
          </div>

          <div class="guide-section help-section">
            <h3>💡 Нужна помощь?</h3>
            <p>Если у вас возникли вопросы или трудности, наша служба поддержки работает 24/7. Мы всегда рады помочь!</p>
            <p class="contact-info">📞 Телефон: +7 (999) 123-45-67</p>
            <p class="contact-info">📧 Email: support@rentflow.com</p>
          </div>
        </div>
      </div>
    </div>

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
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import AppHeader from '@/components/layout/AppHeader.vue'
import BaseButton from '@/components/common/BaseButton.vue'
import BaseInput from '@/components/common/BaseInput.vue'
import BaseCard from '@/components/common/BaseCard.vue'

const authStore = useAuthStore()
const showGuideModal = ref(false)
</script>

<style scoped>
.hero-section {
  padding: 4rem 0 8rem;
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
  padding: 6rem 0;
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

.help-button-container {
  margin-top: var(--spacing-lg);
  text-align: center;
}

/* Guide Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.85);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 1rem;
  backdrop-filter: blur(4px);
}

.modal-guide {
  background: var(--bg-secondary);
  border-radius: 16px;
  max-width: 900px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(6, 182, 212, 0.1));
}

.modal-header h2 {
  font-size: 1.75rem;
  color: var(--text-primary);
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2.5rem;
  color: var(--text-secondary);
  cursor: pointer;
  padding: 0;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  border-radius: 50%;
}

.close-btn:hover {
  color: var(--text-primary);
  background: rgba(255, 255, 255, 0.1);
}

.modal-body {
  padding: 2rem;
}

.guide-section {
  margin-bottom: 2.5rem;
}

.guide-section h3 {
  font-size: 1.5rem;
  color: var(--primary-color);
  margin-bottom: 1rem;
  font-weight: 700;
}

.guide-section p {
  color: var(--text-secondary);
  line-height: 1.7;
  font-size: 1.0625rem;
}

.guide-step {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
  padding: 1.25rem;
  background: rgba(255, 255, 255, 0.03);
  border-radius: 12px;
  border-left: 3px solid var(--primary-color);
  transition: all 0.3s ease;
}

.guide-step:hover {
  background: rgba(59, 130, 246, 0.08);
  transform: translateX(4px);
}

.step-number {
  flex-shrink: 0;
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  font-weight: 700;
  color: white;
}

.step-content h4 {
  font-size: 1.125rem;
  color: var(--text-primary);
  margin: 0 0 0.5rem 0;
  font-weight: 600;
}

.step-content p {
  margin: 0;
  font-size: 1rem;
  line-height: 1.6;
}

.help-section {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.15), rgba(6, 182, 212, 0.15));
  padding: 1.5rem;
  border-radius: 12px;
  border: 1px solid rgba(59, 130, 246, 0.3);
}

.help-section h3 {
  color: var(--text-primary);
}

.contact-info {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0.5rem 0;
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 2.5rem;
  }

  .hero-subtitle {
    font-size: 1.125rem;
  }

  .hero-actions {
    flex-direction: column;
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

  .modal-guide {
    max-width: 100%;
    max-height: 95vh;
  }

  .modal-header {
    padding: 1.5rem;
  }

  .modal-header h2 {
    font-size: 1.25rem;
  }

  .modal-body {
    padding: 1.5rem;
  }

  .guide-step {
    flex-direction: column;
    gap: 1rem;
  }

  .step-number {
    align-self: flex-start;
  }
}
</style>
