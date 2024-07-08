main_ts = """
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
"""

app_vue = """
<template>
  <router-view></router-view>
</template>
<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'App'
})
</script>
<style>
/* 可以加入一些全局样式 */
</style>
"""

router_index_ts = """
import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'

const routes: Array<RouteRecordRaw> = [
  { path: '/', name: 'Login', component: Login },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const loggedIn = localStorage.getItem('user')
  if (to.name !== 'Login' && !loggedIn) next({ name: 'Login' })
  else if (to.name === 'Login' && loggedIn) next({ name: 'Dashboard' })
  else next()
})

export default router
"""

store_index_ts = """
import { defineStore } from 'pinia'

export const useUserStore = defineStore({
  id: 'user',
  state: () => ({
    user: localStorage.getItem('user') || null,
    lastActive: Date.now()
  }),
  actions: {
    login(user: string) {
      this.user = user
      localStorage.setItem('user', user)
      this.resetTimer()
    },
    logout() {
      this.user = null
      localStorage.removeItem('user')
    },
    resetTimer() {
      this.lastActive = Date.now()
    },
    checkActivity() {
      if (Date.now() - this.lastActive > 30 * 60 * 1000) {
        this.logout()
      }
    }
  }
})
"""

login_vue = """
<template>
  <div>
    <h1>Login</h1>
    <input v-model="username" placeholder="Username" />
    <button @click="login">Login</button>
  </div>
</template>
<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '../store'

export default defineComponent({
  name: 'Login',
  setup() {
    const username = ref('')
    const router = useRouter()
    const userStore = useUserStore()

    const login = () => {
      userStore.login(username.value)
      router.push('/dashboard')
    }

    return { username, login }
  }
})
</script>
"""

dashboard_vue = """
<template>
  <div>
    <h1>Dashboard</h1>
    <p>Welcome, {{ user }}</p>
    <button @click="logout">Logout</button>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '../store'

export default defineComponent({
  name: 'Dashboard',
  setup() {
    const userStore = useUserStore()
    const router = useRouter()

    const logout = () => {
      userStore.logout()
      router.push('/')
    }

    return { user: userStore.user, logout }
  }
})
</script>
"""

vite_config_ts = """
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  }
})
"""
