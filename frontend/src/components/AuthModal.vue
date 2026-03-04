<template>
  <div v-if="isOpen" class="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm">
    <div class="bg-white w-full max-w-md border-4 border-black p-8 relative shadow-[10px_10px_0px_0px_rgba(0,0,0,1)]">
      <button @click="close" class="absolute top-4 right-4 text-2xl font-bold hover:rotate-90 transition-transform">✕</button>
      
      <h2 class="text-3xl font-black uppercase mb-6">
        {{ isLoginView ? 'Вход' : 'Регистрация' }}
      </h2>

      <form @submit.prevent="handleSubmit" class="space-y-4">
        <div>
          <label class="block font-bold mb-1">Никнейм</label>
          <input v-model="form.name" type="text" required class="w-full border-2 border-black p-3 outline-none focus:bg-yellow-50">
        </div>
        
        <div>
          <label class="block font-bold mb-1">Пароль</label>
          <input v-model="form.password" type="password" required class="w-full border-2 border-black p-3 outline-none focus:bg-yellow-50">
        </div>

        <p v-if="error" class="text-red-600 font-bold text-sm">{{ error }}</p>

        <button type="submit" :disabled="loading" class="w-full bg-black text-white py-4 font-bold text-xl hover:bg-gray-800 transition-colors disabled:opacity-50">
          {{ loading ? 'Загрузка...' : (isLoginView ? 'ВОЙТИ' : 'СОЗДАТЬ АККАУНТ') }}
        </button>
      </form>

      <div class="mt-6 text-center">
        <button @click="isLoginView = !isLoginView" class="text-sm border-b-2 border-black font-bold">
          {{ isLoginView ? 'Нет аккаунта? Зарегистрируйся' : 'Уже есть аккаунт? Войди' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useAuthStore } from '@/stores/auth'

const props = defineProps(['isOpen'])
const emit = defineEmits(['close'])

const authStore = useAuthStore()
const isLoginView = ref(true)
const loading = ref(false)
const error = ref('')
const form = reactive({ name: '', password: '' })

const close = () => {
  error.value = ''
  emit('close')
}

const handleSubmit = async () => {
  loading.value = true
  error.value = ''
  
  const result = isLoginView.value 
    ? await authStore.login(form.name, form.password)
    : await authStore.register(form.name, form.password)

  if (result.success) {
    close()
  } else {
    error.value = result.error
  }
  loading.value = false
}
</script>