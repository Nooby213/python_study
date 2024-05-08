import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import UserView from '@/views/UserView.vue'
import UserProfile from '@/components/UserProfile.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/user',
      name: 'user',
      beforeEnter: (to, from) => {
        if (to.params.user !== 'admin') {
          window.confirm('관리자 계정만 접근 가능합니다.')
          // return { name: from }
          return { name: 'home' }
        }
      },
      children: [
        { path: '/', name: 'user', component: UserView },
        { path: ':user', name: 'user-profile', component: UserProfile }
      ]
    }
  ]
})

export default router
