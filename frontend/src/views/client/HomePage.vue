<template>
  <div>
    <AppHeader />

    <!-- Hero Section -->
    <section class="hero-section">
      <div class="container">
        <div class="hero-content">
          <h1 class="hero-title">
            Find Your Perfect
            <span class="text-gradient">Rental Property</span>
          </h1>
          <p class="hero-subtitle">
            Discover thousands of properties available for rent. Modern, convenient, and hassle-free.
          </p>
          <div class="hero-actions">
            <router-link to="/properties">
              <BaseButton variant="primary" size="lg">Browse Properties</BaseButton>
            </router-link>
            <router-link to="/client/register">
              <BaseButton variant="outline" size="lg">Get Started</BaseButton>
            </router-link>
          </div>
        </div>

        <!-- Search Box -->
        <div class="search-box card-elevated">
          <div class="grid grid-cols-4 gap-md">
            <BaseInput placeholder="Location" label="Location" />
            <BaseInput placeholder="Min Price" label="Price Range" type="number" />
            <BaseInput placeholder="Rooms" label="Bedrooms" type="number" />
            <BaseButton variant="primary" style="margin-top: 1.5rem;">
              Search
            </BaseButton>
          </div>
        </div>
      </div>
    </section>

    <!-- Features -->
    <section class="features-section">
      <div class="container">
        <h2 class="section-title text-center">Why Choose RentFlow?</h2>
        <div class="grid grid-cols-3 gap-lg">
          <BaseCard elevated>
            <div class="feature-icon">🏠</div>
            <h3 class="text-xl font-semibold mb-sm">Wide Selection</h3>
            <p class="text-secondary">
              Browse through thousands of verified properties across different locations.
            </p>
          </BaseCard>
          <BaseCard elevated>
            <div class="feature-icon">⚡</div>
            <h3 class="text-xl font-semibold mb-sm">Quick Process</h3>
            <p class="text-secondary">
              Apply online and get approved within 24 hours. Simple and fast.
            </p>
          </BaseCard>
          <BaseCard elevated>
            <div class="feature-icon">🔒</div>
            <h3 class="text-xl font-semibold mb-sm">Secure & Safe</h3>
            <p class="text-secondary">
              All properties are verified. Your data and payments are completely secure.
            </p>
          </BaseCard>
        </div>
      </div>
    </section>

    <footer class="app-footer text-center">
      <p class="text-secondary">&copy; 2024 RentFlow by Samolet Plus. All rights reserved.</p>
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
}

.hero-content {
  text-align: center;
  margin-bottom: 3rem;
}

.hero-title {
  font-size: var(--font-size-5xl);
  font-weight: var(--font-weight-bold);
  margin-bottom: var(--spacing-lg);
  line-height: 1.2;
}

.text-gradient {
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: var(--font-size-xl);
  color: var(--text-secondary);
  max-width: 600px;
  margin: 0 auto var(--spacing-2xl);
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
}

.features-section {
  padding: 4rem 0;
  background: var(--bg-primary);
}

.section-title {
  font-size: var(--font-size-3xl);
  font-weight: var(--font-weight-bold);
  margin-bottom: var(--spacing-2xl);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: var(--spacing-md);
}

@media (max-width: 768px) {
  .hero-title {
    font-size: var(--font-size-3xl);
  }

  .grid-cols-3,
  .grid-cols-4 {
    grid-template-columns: 1fr;
  }
}
</style>
