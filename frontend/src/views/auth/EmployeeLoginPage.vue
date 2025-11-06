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
</style>
