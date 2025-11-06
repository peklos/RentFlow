<template>
  <div class="auth-page">
    <div class="auth-container">
      <BaseCard elevated>
        <div class="auth-header">
          <h1 class="auth-title">Вход для сотрудников</h1>
          <p class="text-secondary">Войдите в панель администратора</p>
        </div>

        <form @submit.prevent="handleLogin" class="auth-form">
          <BaseInput
            v-model="form.login"
            label="Логин"
            placeholder="Введите логин"
            required
          />

          <BaseInput
            v-model="form.password"
            label="Пароль"
            type="password"
            placeholder="Введите пароль"
            required
          />

          <BaseButton
            type="submit"
            variant="primary"
            size="lg"
            :loading="loading"
            class="w-full"
          >
            Войти
          </BaseButton>
        </form>

        <div class="test-credentials">
          <div class="test-header">Тестовые данные для входа:</div>
          <div class="test-item">
            <span class="test-label">Логин:</span>
            <code class="test-value" @click="copyToClipboard('admin')">admin</code>
          </div>
          <div class="test-item">
            <span class="test-label">Пароль:</span>
            <code class="test-value" @click="copyToClipboard('admin123')">admin123</code>
          </div>
          <button class="test-fill-btn" @click="fillTestData" type="button">
            Заполнить автоматически
          </button>
        </div>
      </BaseCard>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import BaseCard from '@/components/common/BaseCard.vue'
import BaseInput from '@/components/common/BaseInput.vue'
import BaseButton from '@/components/common/BaseButton.vue'

const router = useRouter()
const authStore = useAuthStore()

const form = ref({ login: '', password: '' })
const loading = ref(false)

const handleLogin = async () => {
  loading.value = true
  try {
    await authStore.employeeLogin(form.value)
    router.push('/admin/dashboard')
  } catch (error) {
    alert('Ошибка входа')
  } finally {
    loading.value = false
  }
}

const fillTestData = () => {
  form.value.login = 'admin'
  form.value.password = 'admin123'
}

const copyToClipboard = (text) => {
  navigator.clipboard.writeText(text).then(() => {
    alert('Скопировано: ' + text)
  })
}
</script>

<style scoped>
.auth-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
  padding: var(--spacing-lg);
}

.auth-container {
  width: 100%;
  max-width: 450px;
}

.auth-header {
  text-align: center;
  margin-bottom: var(--spacing-2xl);
}

.auth-title {
  font-size: var(--font-size-2xl);
  font-weight: var(--font-weight-bold);
  margin-bottom: var(--spacing-xs);
}

.auth-form {
  margin-bottom: var(--spacing-xl);
}

.test-credentials {
  background: rgba(59, 130, 246, 0.1);
  border: 1px solid rgba(59, 130, 246, 0.3);
  border-radius: var(--radius-md);
  padding: var(--spacing-md);
  margin-top: var(--spacing-lg);
}

.test-header {
  font-weight: var(--font-weight-semibold);
  color: var(--primary-color);
  margin-bottom: var(--spacing-sm);
  font-size: 0.875rem;
}

.test-item {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  margin-bottom: var(--spacing-xs);
}

.test-label {
  color: var(--text-secondary);
  font-size: 0.875rem;
}

.test-value {
  background: var(--bg-tertiary);
  padding: 0.25rem 0.5rem;
  border-radius: var(--radius-sm);
  font-family: monospace;
  cursor: pointer;
  transition: all 0.2s ease;
  color: var(--text-primary);
}

.test-value:hover {
  background: var(--primary-color);
  color: white;
}

.test-fill-btn {
  width: 100%;
  margin-top: var(--spacing-sm);
  padding: 0.5rem;
  background: var(--primary-color);
  color: white;
  border: none;
  border-radius: var(--radius-sm);
  cursor: pointer;
  font-size: 0.875rem;
  font-weight: var(--font-weight-medium);
  transition: all 0.2s ease;
}

.test-fill-btn:hover {
  background: var(--primary-hover);
}
</style>
