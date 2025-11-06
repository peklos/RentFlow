<template>
  <div class="auth-page">
    <div class="auth-container">
      <BaseCard elevated>
        <div class="auth-header">
          <router-link to="/" class="logo">
            <span class="text-3xl font-bold text-gradient">RentFlow</span>
          </router-link>
          <h1 class="auth-title">Создать аккаунт</h1>
          <p class="text-secondary">Присоединяйтесь к RentFlow</p>
        </div>

        <form @submit.prevent="handleRegister" class="auth-form">
          <BaseInput
            v-model="form.phone"
            label="Номер телефона"
            type="tel"
            placeholder="+7 (999) 123-45-67"
            :error="errors.phone"
            required
          />

          <BaseInput
            v-model="form.email"
            label="Email (необязательно)"
            type="email"
            placeholder="your@email.com"
            :error="errors.email"
          />

          <BaseInput
            v-model="form.password"
            label="Пароль"
            type="password"
            placeholder="Минимум 6 символов"
            :error="errors.password"
            required
          />

          <div v-if="errors.general" class="alert alert-danger">
            {{ errors.general }}
          </div>

          <div v-if="success" class="alert alert-success">
            {{ success }}
          </div>

          <BaseButton
            type="submit"
            variant="primary"
            size="lg"
            :loading="loading"
            class="w-full"
          >
            Регистрация
          </BaseButton>
        </form>

        <div class="auth-footer">
          <p class="text-secondary">
            Уже есть аккаунт?
            <router-link to="/client/login" class="text-primary font-medium">
              Войти
            </router-link>
          </p>
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

const form = ref({
  phone: '',
  email: '',
  password: ''
})

const errors = ref({
  phone: '',
  email: '',
  password: '',
  general: ''
})

const success = ref('')
const loading = ref(false)

const handleRegister = async () => {
  // Reset errors
  errors.value = { phone: '', email: '', password: '', general: '' }
  success.value = ''

  // Validation
  if (!form.value.phone) {
    errors.value.phone = 'Введите номер телефона'
    return
  }
  if (!form.value.password || form.value.password.length < 6) {
    errors.value.password = 'Пароль должен содержать минимум 6 символов'
    return
  }

  loading.value = true
  try {
    await authStore.clientRegister({
      phone: form.value.phone,
      email: form.value.email || null,
      password: form.value.password
    })
    success.value = 'Регистрация успешна! Код подтверждения отправлен на ваш телефон.'
    setTimeout(() => {
      router.push('/client/login')
    }, 2000)
  } catch (error) {
    errors.value.general = error.response?.data?.detail || 'Ошибка регистрации. Попробуйте снова.'
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

.logo {
  display: inline-block;
  margin-bottom: var(--spacing-lg);
}

.text-gradient {
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.auth-title {
  font-size: var(--font-size-2xl);
  font-weight: var(--font-weight-bold);
  margin-bottom: var(--spacing-xs);
}

.auth-form {
  margin-bottom: var(--spacing-xl);
}

.auth-footer {
  text-align: center;
  padding-top: var(--spacing-lg);
  border-top: 1px solid var(--border-color);
}
</style>
