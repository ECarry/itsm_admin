import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/login/index.vue')
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: () => import('../views/login/components/SignUp.vue')
  },
  {
    path: '/',
    name: 'Home',
    component: () => import('../layouts/index.vue'),
    children: [
      {
        path: '/contract',
        name: 'Contract',
        component: () => import('../views/contract/contracts/index.vue')
      },
      {
        path: '/server',
        name: 'Server',
        component: () => import('../views/contract/servers/index.vue')
      },
      {
        path: '/product',
        name: 'Product',
        component: () => import('../views/spare/product/index.vue')
      },
      {
        path: '/spare',
        name: 'Spare',
        component: () => import('../views/spare/spares/index.vue')
      },
      {
        path: '/user',
        name: 'User',
        component: () => import('../views/user/index.vue')
      }
    ]
  }

]

const router = new VueRouter({
  linkExactActiveClass: 'active',
  routes
})

export default router
