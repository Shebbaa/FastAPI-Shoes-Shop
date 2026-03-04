<!-- Убрана кнопка "Управление товарами" для всех — теперь она только в Header для админов -->
<template>
  <div class="min-h-screen bg-white">
    <div class="max-w-7xl mx-auto px-4 py-8">
      <div class="mb-8">
        <h1 class="text-4xl font-extrabold text-black mb-2">Каталог обуви</h1>
        <p class="text-gray-500">Откройте для себя наши удивительные товары</p>
      </div>

      <div class="flex gap-8">
        <aside class="w-64 flex-shrink-0">
          <CategoryFilter />
        </aside>

        <main class="flex-grow">
          <div class="mb-6 flex items-center justify-between">
            <p class="text-gray-700">
              <span class="font-bold">{{ productsStore.productsCount }}</span>
              {{ productsStore.productsCount === 1 ? 'продукт' : 'продуктов' }} найдено
            </p>
            <button
              v-if="productsStore.selectedCategory"
              @click="productsStore.clearCategoryFilter"
              class="text-sm text-gray-500 hover:text-black transition-colors font-medium"
            >
              Сбросить фильтр
            </button>
          </div>

          <div v-if="productsStore.loading" class="text-center py-12">
            <div class="inline-block animate-spin rounded-none h-12 w-12 border-b-2 border-black"></div>
            <p class="mt-4 text-gray-500">Загрузка...</p>
          </div>

          <div v-else-if="productsStore.error" class="text-center py-12">
            <p class="text-red-600 font-medium">{{ productsStore.error }}</p>
          </div>

          <div
            v-else-if="productsStore.filteredProducts.length > 0"
            class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
          >
            <ProductCard
              v-for="product in productsStore.filteredProducts"
              :key="product.id"
              :product="product"
            />
          </div>

          <div v-else class="text-center py-12">
            <p class="text-gray-500 text-lg font-medium">Продуктов не найдено</p>
            <button @click="productsStore.clearCategoryFilter" class="mt-4 text-black hover:underline font-medium">
              Показать все
            </button>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useProductsStore } from '@/stores/products'
import ProductCard from '@/components/ProductCard.vue'
import CategoryFilter from '@/components/CategoryFilter.vue'

const productsStore = useProductsStore()

onMounted(async () => {
  await Promise.all([productsStore.fetchProducts(), productsStore.fetchCategories()])
})
</script>
