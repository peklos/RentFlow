<template>
  <div id="app" class="app-layout">
    <router-view />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()

onMounted(() => {
  // Any initialization logic
  console.log('RentFlow App initialized')
})
</script>

<style>
@import './styles/main.css';
</style>
