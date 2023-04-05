import {createRouter, createWebHistory} from 'vue-router'
import store from "@/store";
import Dividends from "@/views/Dividends";

const routes = [
  {
    path: '/',
    name: 'home',
    meta: {layout: 'main'},
    component: () => import('../views/Home')
  },
  {
    path: '/charts',
    name: 'charts',
    meta: {layout: 'main', auth: true},
    component: () => import('../views/Charts')
  },
  {
    path: '/dividends',
    name: 'dividends',
    meta: {layout: 'main', auth: true},
    component: Dividends
  },
  {
    path: '/edit_dividend/:id',
    name: 'edit_dividend',
    meta: {layout: 'main', auth: true},
    props: true,
    component: () => import('../views/AddOrEditDividend')
  },
  {
    path: '/add_dividend',
    name: 'add_dividend',
    meta: {layout: 'main', auth: true},
    component: () => import('../views/AddOrEditDividend')
  },
  {
    path: '/company/:id',
    name: 'company',
    meta: {layout: 'main', auth: true},
    props: true,
    component: () => import('../views/Company')
  },
  {
    path: '/add_company',
    name: 'add_company',
    meta: {layout: 'main', auth: true},
    component: () => import('../views/AddCompany')
  },
  {
    path: '/reports',
    name: 'reports',
    meta: {layout: 'main', auth: true},
    component: () => import('../views/Reports')
  },
  {
    path: '/edit_report/:id',
    name: 'edit_report',
    meta: {layout: 'main', auth: true},
    props: true,
    component: () => import('../views/AddOrEditReport')
  },
  {
    path: '/add_report',
    name: 'add_report',
    meta: {layout: 'main', auth: true},
    component: () => import('../views/AddOrEditReport')
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
  routes,
  linkExactActiveClass: "active"
})

router.afterEach((to, from) => {
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
