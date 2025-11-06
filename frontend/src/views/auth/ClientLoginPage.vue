<template>
  <div class="auth-page">
    <div class="auth-container">
      <BaseCard elevated>
        <div class="auth-header">
          <router-link to="/" class="logo">
            <span class="text-3xl font-bold text-gradient">RentFlow</span>
          </router-link>
          <h1 class="auth-title">Welcome Back</h1>
          <p class="text-secondary">Sign in to your account</p>
        </div>

        <form @submit.prevent="handleLogin" class="auth-form">
          <BaseInput
            v-model="form.phone"
            label="Phone Number"
            type="tel"
            placeholder="+7 (999) 123-45-67"
            :error="errors.phone"
            required
          />

          <BaseInput
            v-model="form.password"
            label="Password"
            type="password"
            placeholder="Enter your password"
            :error="errors.password"
            required
          />

          <div v-if="errors.general" class="alert alert-danger">
            {{ errors.general }}
          </div>

          <BaseButton
            type="submit"
            variant="primary"
            size="lg"
            :loading="loading"
            class="w-full"
          >
            Sign In
          </BaseButton>
        </form>

        <div class="auth-footer">
          <p class="text-secondary">
            Don't have an account?
            <router-link to="/client/register" class="text-primary font-medium">
              Sign Up
            </router-link>
          </p>
          <p class="text-tertiary mt-md">
            Are you an employee?
            <router-link to="/employee/login" class="text-secondary font-medium">
              Employee Login
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
  password: ''
})

const errors = ref({
  phone: '',
  password: '',
  general: ''
})

const loading = ref(false)

const handleLogin = async () => {
  // Reset errors
  errors.value = { phone: '', password: '', general: '' }

  // Validation
  if (!form.value.phone) {
    errors.value.phone = 'Phone number is required'
    return
  }
  if (!form.value.password) {
    errors.value.password = 'Password is required'
    return
  }

  loading.value = true
  try {
    await authStore.clientLogin({
      phone: form.value.phone,
      password: form.value.password
    })
    router.push('/client/profile')
  } catch (error) {
    errors.value.general = error.response?.data?.detail || 'Login failed. Please try again.'
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
