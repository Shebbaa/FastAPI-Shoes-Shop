<template>
  <div class="min-h-screen bg-gray-50 flex items-center justify-center px-4">
    <div class="w-full max-w-md">

      <!-- Логотип / заголовок -->
      <div class="text-center mb-8">
        <router-link to="/" class="inline-flex items-center space-x-2 group">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 group-hover:scale-110 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/>
          </svg>
          <span class="text-3xl font-extrabold text-black">Shoes Shop</span>
        </router-link>
      </div>

      <!-- Карточка формы -->
      <div class="bg-white border-2 border-gray-200 rounded-xl p-8 shadow-sm">

        <!-- Переключатель вкладок -->
        <div class="flex mb-8 border-2 border-gray-100 rounded-lg overflow-hidden">
          <button
            @click="mode = 'login'"
            :class="['flex-1 py-3 text-sm font-bold transition-colors', mode === 'login' ? 'bg-black text-white' : 'bg-white text-gray-500 hover:bg-gray-50']"
          >
            Войти
          </button>
          <button
            @click="mode = 'register'"
            :class="['flex-1 py-3 text-sm font-bold transition-colors', mode === 'register' ? 'bg-black text-white' : 'bg-white text-gray-500 hover:bg-gray-50']"
          >
            Регистрация
          </button>
        </div>

        <!-- Форма входа -->
        <form v-if="mode === 'login'" @submit.prevent="handleLogin" class="space-y-4">
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-1">Email</label>
            <input
              v-model="loginForm.email"
              type="email"
              placeholder="you@example.com"
              required
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-lg text-gray-900 focus:border-black focus:outline-none transition-colors"
            />
          </div>
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-1">Пароль</label>
            <input
              v-model="loginForm.password"
              type="password"
              placeholder="••••••••"
              required
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-lg text-gray-900 focus:border-black focus:outline-none transition-colors"
            />
          </div>

          <!-- Ошибка -->
          <div v-if="error" class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg text-sm">
            {{ error }}
          </div>

          <button
            type="submit"
            :disabled="loading"
            class="w-full bg-black text-white py-3 rounded-lg font-bold hover:bg-gray-800 transition-colors disabled:opacity-50"
          >
            {{ loading ? 'Входим...' : 'Войти' }}
          </button>
        </form>

        <!-- Форма регистрации -->
        <form v-else @submit.prevent="handleRegister" class="space-y-4">
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-1">Email</label>
            <input
              v-model="registerForm.email"
              type="email"
              placeholder="you@example.com"
              required
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-lg text-gray-900 focus:border-black focus:outline-none transition-colors"
            />
          </div>
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-1">Имя пользователя</label>
            <input
              v-model="registerForm.username"
              type="text"
              placeholder="username"
              required
              minlength="3"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-lg text-gray-900 focus:border-black focus:outline-none transition-colors"
            />
          </div>
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-1">Пароль</label>
            <input
              v-model="registerForm.password"
              type="password"
              placeholder="Минимум 6 символов"
              required
              minlength="6"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-lg text-gray-900 focus:border-black focus:outline-none transition-colors"
            />
          </div>

          <!-- Ошибка -->
          <div v-if="error" class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg text-sm">
            {{ error }}
          </div>

          <button
            type="submit"
            :disabled="loading"
            class="w-full bg-black text-white py-3 rounded-lg font-bold hover:bg-gray-800 transition-colors disabled:opacity-50"
          >
            {{ loading ? 'Регистрируем...' : 'Создать аккаунт' }}
          </button>
        </form>

      </div>

      <!-- Ссылка назад -->
      <p class="text-center mt-6 text-sm text-gray-500">
        <router-link to="/" class="text-black font-semibold hover:underline">← Вернуться в магазин</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const mode = ref(route.query.mode === 'register' ? 'register' : 'login')
const loading = ref(false)
const error = ref('')

const loginForm = ref({ email: '', password: '' })
const registerForm = ref({ email: '', username: '', password: '' })

async function handleLogin() {
  error.value = ''
  loading.value = true
  try {
    await authStore.login(loginForm.value.email, loginForm.value.password)
    router.push(route.query.redirect || '/')
  } catch (e) {
    error.value = e.response?.data?.detail || 'Ошибка входа'
  } finally {
    loading.value = false
  }
}

async function handleRegister() {
  error.value = ''
  loading.value = true
  try {
    await authStore.register(
      registerForm.value.email,
      registerForm.value.username,
      registerForm.value.password
    )
    router.push('/')
  } catch (e) {
    error.value = e.response?.data?.detail || 'Ошибка регистрации'
  } finally {
    loading.value = false
  }
}
</script>
