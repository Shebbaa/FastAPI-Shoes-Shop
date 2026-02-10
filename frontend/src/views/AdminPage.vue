<template>
  <div class="min-h-screen bg-gray-50 py-12">
    <div class="max-w-4xl mx-auto px-4">
      
      <div class="flex items-center justify-between mb-8">
        <h1 class="text-3xl font-extrabold text-gray-900">Панель администратора</h1>
        <RouterLink to="/" class="text-gray-600 hover:text-black underline">
          ← Вернуться в магазин
        </RouterLink>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        
        <div class="bg-white p-6 rounded-xl shadow-md border border-gray-100 h-fit">
          <h2 class="text-xl font-bold text-gray-900 mb-6 border-b pb-2">📂 Добавить категорию</h2>
          
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Название категории</label>
              <input 
                v-model="newCategory.name" 
                placeholder="Например: Кеды" 
                class="w-full p-3 border border-gray-300 rounded-lg text-gray-900 bg-white placeholder-gray-400 focus:ring-2 focus:ring-black focus:border-transparent outline-none transition-all" 
              />
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Slug (URL)</label>
              <input 
                v-model="newCategory.slug" 
                placeholder="Например: kedy" 
                class="w-full p-3 border border-gray-300 rounded-lg text-gray-900 bg-white placeholder-gray-400 focus:ring-2 focus:ring-black focus:border-transparent outline-none transition-all" 
              />
              <p class="text-xs text-gray-500 mt-1">Используйте английские буквы, без пробелов.</p>
            </div>
            
            <button 
              @click="addCategory" 
              class="w-full bg-gray-900 text-white font-bold py-3 px-4 rounded-lg hover:bg-black transition-colors mt-2"
            >
              Создать категорию
            </button>
          </div>
        </div>

        <div class="bg-white p-6 rounded-xl shadow-md border border-gray-100">
          <h2 class="text-xl font-bold text-gray-900 mb-6 border-b pb-2">👟 Добавить товар</h2>
          
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Название модели</label>
              <input 
                v-model="newProduct.name" 
                placeholder="Nike Air Force 1" 
                class="w-full p-3 border border-gray-300 rounded-lg text-gray-900 bg-white placeholder-gray-400 focus:ring-2 focus:ring-black focus:border-transparent outline-none" 
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Описание</label>
              <textarea 
                v-model="newProduct.description" 
                placeholder="Краткое описание товара..." 
                rows="3"
                class="w-full p-3 border border-gray-300 rounded-lg text-gray-900 bg-white placeholder-gray-400 focus:ring-2 focus:ring-black focus:border-transparent outline-none"
              ></textarea>
            </div>

            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Цена (₽)</label>
                <input 
                  v-model.number="newProduct.price" 
                  type="number" 
                  placeholder="0" 
                  class="w-full p-3 border border-gray-300 rounded-lg text-gray-900 bg-white placeholder-gray-400 focus:ring-2 focus:ring-black focus:border-transparent outline-none" 
                />
              </div>
              
              <div>
                 <label class="block text-sm font-medium text-gray-700 mb-1">Категория</label>
                 <select 
                   v-model="newProduct.category_id" 
                   class="w-full p-3 border border-gray-300 rounded-lg text-gray-900 bg-white focus:ring-2 focus:ring-black focus:border-transparent outline-none"
                 >
                  <option disabled value="">Выбрать...</option>
                  <option v-for="cat in productsStore.categories" :key="cat.id" :value="cat.id">
                    {{ cat.name }}
                  </option>
                </select>
              </div>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">URL картинки</label>
              <input 
                v-model="newProduct.image_url" 
                placeholder="https://..." 
                class="w-full p-3 border border-gray-300 rounded-lg text-gray-900 bg-white placeholder-gray-400 focus:ring-2 focus:ring-black focus:border-transparent outline-none" 
              />
            </div>
            
            <button 
              @click="addProduct" 
              class="w-full bg-black text-white font-bold py-3 px-4 rounded-lg hover:bg-gray-800 transition-colors shadow-lg mt-4"
            >
              Добавить кроссовки
            </button>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useProductsStore } from '@/stores/products'

const productsStore = useProductsStore()

// Данные для форм
const newCategory = ref({ name: '', slug: '' })
const newProduct = ref({ 
  name: '', 
  description: '', 
  price: null, // null чтобы поле было пустым, а не 0
  category_id: '', 
  image_url: '' 
})

// Загружаем существующие категории при открытии страницы, 
// чтобы работал выпадающий список
onMounted(async () => {
  await productsStore.fetchCategories()
})

// Логика добавления категории
const addCategory = async () => {
  if (!newCategory.value.name || !newCategory.value.slug) {
    alert('Заполните все поля категории!')
    return
  }
  
  try {
    await productsStore.createCategory(newCategory.value)
    alert('Категория успешно создана! 🎉')
    newCategory.value = { name: '', slug: '' } // Очистка формы
  } catch (e) {
    alert('Ошибка! Возможно, такой slug уже существует.')
  }
}

// Логика добавления товара
const addProduct = async () => {
  // Простая валидация
  if (!newProduct.value.name || !newProduct.value.price || !newProduct.value.category_id) {
    alert('Заполните обязательные поля (Название, Цена, Категория)!')
    return
  }

  try {
    await productsStore.createProduct(newProduct.value)
    alert('Товар успешно добавлен! 👟')
    // Очистка формы
    newProduct.value = { name: '', description: '', price: null, category_id: '', image_url: '' }
  } catch (e) {
    alert('Ошибка при создании товара.')
  }
}
</script>