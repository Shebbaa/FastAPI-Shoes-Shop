// frontend/src/stores/auth.js
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'

const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api'
const TOKEN_KEY = 'auth_token'
const USER_KEY = 'auth_user'

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem(TOKEN_KEY) || null)
  const user = ref(JSON.parse(localStorage.getItem(USER_KEY) || 'null'))

  const isLoggedIn = computed(() => !!token.value)
  const isAdmin = computed(() => user.value?.is_admin === true)

  function setAuth(data) {
    token.value = data.access_token
    user.value = data.user
    localStorage.setItem(TOKEN_KEY, data.access_token)
    localStorage.setItem(USER_KEY, JSON.stringify(data.user))
  }

  function logout() {
    token.value = null
    user.value = null
    localStorage.removeItem(TOKEN_KEY)
    localStorage.removeItem(USER_KEY)
  }

  async function register(email, username, password) {
    const res = await axios.post(`${API_BASE}/auth/register`, { email, username, password })
    setAuth(res.data)
    return res.data
  }

  async function login(email, password) {
    const res = await axios.post(`${API_BASE}/auth/login`, { email, password })
    setAuth(res.data)
    return res.data
  }

  return { token, user, isLoggedIn, isAdmin, register, login, logout }
})
