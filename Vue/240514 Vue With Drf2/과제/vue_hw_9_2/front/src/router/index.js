import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArticleCreateView from '../views/ArticleCreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import SignInView from '@/views/SignInView.vue'
import { useArticleStore } from '@/stores/articles'


// const routerUser = useRouter()
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/create',
      name: 'create',
      component: ArticleCreateView
    },
    {
      path: '/signup',
      name: 'signup',
      beforeEnter: () => {
        const store = useArticleStore()
        if (store.isLogin === true) {
          window.alert('로그인 되있음')
          router.push('/')
        }
      },
      component: SignUpView
    },
    {
      path: '/signin',
      name: 'signin',
      beforeEnter: () => {
        const store = useArticleStore()
        if (store.isLogin === true) {
          window.alert('로그인 되있음')
          router.push('/')
        }
      },
      component: SignInView
    }
  ]
})

export default router
