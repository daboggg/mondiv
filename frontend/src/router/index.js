import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'
import store from "@/store";
import Dividends from "@/views/Dividends";

const routes = [
  {
    path: '/',
    name: 'home',
    meta: {layout: 'main', auth: true},
    component: () => import('../views/Home')
  },
  {
    path: '/dividends',
    name: 'dividends',
    meta: {layout: 'main', auth: true},
    component: Dividends
  },
  {
    path: '/login',
    name: 'login',
    meta: {layout: 'empty'},
    component: () => import('../views/Login')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.afterEach((to,from)=>{
  document.title = to.name + ' | MD'
})

router.beforeEach((to, from, next) => {

  const usernameFromSessionStorage = sessionStorage.getItem('username')
  const tokenFromSessionStorage = sessionStorage.getItem('token')

  const currentUser = store.getters.token

  const requireAuth = to.matched.some(record => record.meta.auth)

  if (requireAuth && !currentUser && !tokenFromSessionStorage) {
    next('/login');
  } else {
    if (tokenFromSessionStorage) {
      store.commit('login', {
        username: usernameFromSessionStorage,
        token: tokenFromSessionStorage
      })
    }
    next()
  }
})

export default router
