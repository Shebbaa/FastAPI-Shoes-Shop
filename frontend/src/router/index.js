// frontend/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import ProductDetailPage from '@/views/ProductDetailPage.vue'
import CartPage from '@/views/CartPage.vue'
import LoginPage from '@/views/LoginPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage,
      meta: { title: 'Shop - Home' },
    },
    {
      path: '/product/:id',
      name: 'product-detail',
      component: ProductDetailPage,
      meta: { title: 'Product Details' },
    },
    {
      path: '/cart',
      name: 'cart',
      component: CartPage,
      meta: { title: 'Shopping Cart' },
    },
    {
      path: '/login',
      name: 'login',
      component: LoginPage,
      meta: { title: 'Войти', guestOnly: true },
    },
    {
      path: '/admin',
      name: 'admin',
      component: () => import('@/views/AdminPage.vue'),
      meta: { title: 'Admin Panel', requiresAdmin: true },
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { top: 0 }
  },
})

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'FastAPI Shop'

  // Динамически импортируем store чтобы избежать circular deps
  import('@/stores/auth').then(({ useAuthStore }) => {
    const authStore = useAuthStore()

    // Страница только для гостей (логин/регистрация)
    if (to.meta.guestOnly && authStore.isLoggedIn) {
      return next('/')
    }

    // Страница требует роль admin
    if (to.meta.requiresAdmin) {
      if (!authStore.isLoggedIn) {
        return next({ name: 'login', query: { redirect: to.fullPath } })
      }
      if (!authStore.isAdmin) {
        return next({ name: 'home' })
      }
    }

    next()
  })
})

export default router
