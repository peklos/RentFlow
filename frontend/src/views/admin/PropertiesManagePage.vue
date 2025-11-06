<template>
  <div class="properties-manage">
    <div class="page-header">
      <div>
        <h1>Properties Management</h1>
        <p class="subtitle">Manage all rental properties</p>
      </div>
      <BaseButton variant="primary" @click="showCreateModal = true">
        + Add Property
      </BaseButton>
    </div>

    <!-- Stats -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-label">Total Properties</div>
        <div class="stat-value">{{ stats.total }}</div>
      </div>
      <div class="stat-card available">
        <div class="stat-label">Available</div>
        <div class="stat-value">{{ stats.available }}</div>
      </div>
      <div class="stat-card rented">
        <div class="stat-label">Rented</div>
        <div class="stat-value">{{ stats.rented }}</div>
      </div>
      <div class="stat-card maintenance">
        <div class="stat-label">Maintenance</div>
        <div class="stat-value">{{ stats.maintenance }}</div>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="loading-state">
      <div class="spinner"></div>
      <p>Loading properties...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="error-state">
      <p>{{ error }}</p>
      <BaseButton @click="loadProperties">Retry</BaseButton>
    </div>

    <!-- Properties Grid -->
    <div v-else-if="properties.length > 0" class="properties-grid">
      <BaseCard v-for="property in properties" :key="property.id" elevated class="property-card">
        <div class="property-image">
          <div class="image-placeholder">
            <span class="icon">🏢</span>
          </div>
          <span :class="['status-badge', property.status]">
            {{ property.status }}
          </span>
        </div>

        <div class="property-content">
          <h3 class="property-title">{{ property.subtype }}</h3>
          <p class="property-address">{{ property.address }}</p>

          <div class="property-details">
            <div class="detail-item">
              <span class="icon">📏</span>
              <span>{{ property.area }} m²</span>
            </div>
            <div class="detail-item" v-if="property.rooms_count">
              <span class="icon">🛏️</span>
              <span>{{ property.rooms_count }} rooms</span>
            </div>
            <div class="detail-item">
              <span class="icon">🏢</span>
              <span>Floor {{ property.floor }}/{{ property.total_floors }}</span>
            </div>
          </div>

          <div class="property-price">
            {{ formatPrice(property.monthly_rent) }} / month
          </div>

          <div class="property-actions">
            <BaseButton variant="secondary" size="small" @click="editProperty(property)">
              Edit
            </BaseButton>
            <BaseButton
              variant="danger"
              size="small"
              @click="confirmDelete(property)"
              :disabled="deletingId === property.id"
            >
              Delete
            </BaseButton>
          </div>
        </div>
      </BaseCard>
    </div>

    <!-- Empty State -->
    <div v-else class="empty-state">
      <p>No properties found</p>
      <BaseButton variant="primary" @click="showCreateModal = true">
        Add Your First Property
      </BaseButton>
    </div>

    <!-- Create/Edit Modal -->
    <div v-if="showCreateModal || editingProperty" class="modal-overlay" @click.self="closeModal">
      <div class="modal">
        <div class="modal-header">
          <h2>{{ editingProperty ? 'Edit Property' : 'Add New Property' }}</h2>
          <button class="close-btn" @click="closeModal">×</button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="submitProperty" class="property-form">
            <div class="form-group">
              <label>Type *</label>
              <select v-model="propertyForm.type" required>
                <option value="residential">Residential</option>
                <option value="commercial">Commercial</option>
              </select>
            </div>

            <div class="form-group">
              <label>Subtype *</label>
              <select v-model="propertyForm.subtype" required>
                <option value="">Выберите подтип</option>
                <option value="Квартира">Квартира</option>
                <option value="Студия">Студия</option>
                <option value="Пентхаус">Пентхаус</option>
                <option value="Таунхаус">Таунхаус</option>
                <option value="Коттедж">Коттедж</option>
                <option value="Офис">Офис</option>
                <option value="Торговое помещение">Торговое помещение</option>
                <option value="Склад">Склад</option>
              </select>
            </div>

            <div class="form-group">
              <label>Address *</label>
              <input v-model="propertyForm.address" required placeholder="Full address" />
            </div>

            <div class="form-row">
              <div class="form-group">
                <label>Area (m²) *</label>
                <input v-model.number="propertyForm.area" type="number" step="0.1" required />
              </div>
              <div class="form-group">
                <label>Rooms</label>
                <input v-model.number="propertyForm.rooms_count" type="number" />
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label>Floor *</label>
                <input v-model.number="propertyForm.floor" type="number" required />
              </div>
              <div class="form-group">
                <label>Total Floors *</label>
                <input v-model.number="propertyForm.total_floors" type="number" required />
              </div>
            </div>

            <div class="form-group">
              <label>Monthly Rent (₽) *</label>
              <input v-model.number="propertyForm.monthly_rent" type="number" step="0.01" required />
            </div>

            <div class="form-group">
              <label>Status *</label>
              <select v-model="propertyForm.status" required>
                <option value="available">Available</option>
                <option value="rented">Rented</option>
                <option value="maintenance">Maintenance</option>
              </select>
            </div>

            <div class="form-group">
              <label>Description</label>
              <textarea v-model="propertyForm.description" rows="3" placeholder="Property description"></textarea>
            </div>

            <div class="form-group">
              <label>Amenities</label>
              <textarea v-model="propertyForm.amenities" rows="2" placeholder="List amenities"></textarea>
            </div>

            <div class="form-group checkbox">
              <label>
                <input type="checkbox" v-model="propertyForm.is_furnished" />
                <span>Furnished</span>
              </label>
            </div>

            <div class="form-actions">
              <BaseButton type="button" variant="secondary" @click="closeModal">Cancel</BaseButton>
              <BaseButton type="submit" variant="primary" :disabled="submitting">
                {{ submitting ? 'Saving...' : (editingProperty ? 'Update' : 'Create') }}
              </BaseButton>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { propertiesAPI } from '@/api/services/properties'
import BaseCard from '@/components/common/BaseCard.vue'
import BaseButton from '@/components/common/BaseButton.vue'

const properties = ref([])
const loading = ref(true)
const error = ref(null)
const showCreateModal = ref(false)
const editingProperty = ref(null)
const submitting = ref(false)
const deletingId = ref(null)

const propertyForm = ref({
  type: 'residential',
  subtype: '',
  address: '',
  area: null,
  rooms_count: null,
  floor: null,
  total_floors: null,
  monthly_rent: null,
  status: 'available',
  description: '',
  amenities: '',
  is_furnished: false
})

const stats = computed(() => {
  return {
    total: properties.value.length,
    available: properties.value.filter(p => p.status === 'available').length,
    rented: properties.value.filter(p => p.status === 'rented').length,
    maintenance: properties.value.filter(p => p.status === 'maintenance').length
  }
})

const loadProperties = async () => {
  loading.value = true
  error.value = null
  try {
    const response = await propertiesAPI.getAllAdmin()
    properties.value = response.data
  } catch (err) {
    error.value = err.response?.data?.detail || 'Failed to load properties'
    console.error('Error loading properties:', err)
  } finally {
    loading.value = false
  }
}

const editProperty = (property) => {
  editingProperty.value = property
  propertyForm.value = { ...property }
}

const closeModal = () => {
  showCreateModal.value = false
  editingProperty.value = null
  resetForm()
}

const resetForm = () => {
  propertyForm.value = {
    type: 'residential',
    subtype: '',
    address: '',
    area: null,
    rooms_count: null,
    floor: null,
    total_floors: null,
    monthly_rent: null,
    status: 'available',
    description: '',
    amenities: '',
    is_furnished: false
  }
}

const submitProperty = async () => {
  submitting.value = true
  error.value = null
  try {
    if (editingProperty.value) {
      await propertiesAPI.update(editingProperty.value.id, propertyForm.value)
    } else {
      await propertiesAPI.create(propertyForm.value)
    }
    await loadProperties()
    closeModal()
  } catch (err) {
    error.value = err.response?.data?.detail || 'Failed to save property'
    console.error('Error saving property:', err)
  } finally {
    submitting.value = false
  }
}

const confirmDelete = async (property) => {
  if (!confirm(`Are you sure you want to delete "${property.subtype}" at ${property.address}?`)) {
    return
  }

  deletingId.value = property.id
  try {
    await propertiesAPI.delete(property.id)
    await loadProperties()
  } catch (err) {
    error.value = err.response?.data?.detail || 'Failed to delete property'
    console.error('Error deleting property:', err)
  } finally {
    deletingId.value = null
  }
}

const formatPrice = (price) => {
  return new Intl.NumberFormat('ru-RU', {
    style: 'currency',
    currency: 'RUB',
    maximumFractionDigits: 0
  }).format(price)
}

onMounted(() => {
  loadProperties()
})
</script>

<style scoped>
.properties-manage {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.page-header h1 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  color: var(--text-primary);
}

.subtitle {
  color: var(--text-secondary);
  font-size: 1rem;
}

/* Stats */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: var(--bg-secondary);
  padding: 1.5rem;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.stat-card.available {
  border-color: rgba(34, 197, 94, 0.3);
}

.stat-card.rented {
  border-color: rgba(59, 130, 246, 0.3);
}

.stat-card.maintenance {
  border-color: rgba(250, 204, 21, 0.3);
}

.stat-label {
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin-bottom: 0.5rem;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: var(--text-primary);
}

/* Loading & Error States */
.loading-state,
.error-state,
.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  color: var(--text-secondary);
}

.spinner {
  width: 50px;
  height: 50px;
  margin: 0 auto 1rem;
  border: 3px solid var(--bg-tertiary);
  border-top-color: var(--primary-color);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Properties Grid */
.properties-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
}

.property-card {
  overflow: hidden;
  transition: transform 0.3s ease;
}

.property-card:hover {
  transform: translateY(-4px);
}

.property-image {
  position: relative;
  height: 180px;
  background: linear-gradient(135deg, var(--bg-tertiary) 0%, var(--bg-secondary) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
}

.image-placeholder {
  font-size: 4rem;
  opacity: 0.5;
}

.status-badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  padding: 0.375rem 0.875rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: capitalize;
}

.status-badge.available {
  background: rgba(34, 197, 94, 0.15);
  color: #22c55e;
}

.status-badge.rented {
  background: rgba(59, 130, 246, 0.15);
  color: #3b82f6;
}

.status-badge.maintenance {
  background: rgba(250, 204, 21, 0.15);
  color: #facc15;
}

.property-content {
  padding: 1.5rem;
}

.property-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}

.property-address {
  color: var(--text-secondary);
  font-size: 0.875rem;
  margin-bottom: 1rem;
}

.property-details {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 1rem;
}

.detail-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: var(--text-secondary);
}

.property-price {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary-color);
  margin-bottom: 1rem;
}

.property-actions {
  display: flex;
  gap: 0.75rem;
}

/* Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 1rem;
}

.modal {
  background: var(--bg-secondary);
  border-radius: 16px;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.modal-header h2 {
  font-size: 1.5rem;
  color: var(--text-primary);
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  color: var(--text-secondary);
  cursor: pointer;
  padding: 0;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.3s ease;
}

.close-btn:hover {
  color: var(--text-primary);
}

.modal-body {
  padding: 1.5rem;
}

/* Form */
.property-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group label {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--text-secondary);
}

.form-group input,
.form-group select,
.form-group textarea {
  padding: 0.75rem;
  background: var(--bg-tertiary);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  color: var(--text-primary);
  font-size: 1rem;
  transition: all 0.3s ease;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px var(--primary-glow);
}

.form-group.checkbox {
  flex-direction: row;
  align-items: center;
}

.form-group.checkbox label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
}

.form-group.checkbox input[type="checkbox"] {
  width: auto;
  cursor: pointer;
}

.form-actions {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

.form-actions button {
  flex: 1;
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

/* Responsive */
@media (max-width: 768px) {
  .properties-manage {
    padding: 1rem;
  }

  .page-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

  .properties-grid {
    grid-template-columns: 1fr;
  }

  .form-row {
    grid-template-columns: 1fr;
  }
}
</style>
