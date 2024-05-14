import axios from 'axios'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const BASE_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  }
  )
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${BASE_URL}/api/v1/articles/`
    })
      .then(res => articles.value = res.data)
  }

  const createArticle = function (article) {
    const router = useRouter()
    const { title, content } = article
    axios({
      method: 'post',
      url: `${BASE_URL}/api/v1/articles/`,
      data: {
        title,
        content
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(() => router.push({ name: 'home' }))
  }

  const signup = function (payload) {
    const { username, password1, password2 } = payload
    axios({
      method: 'post',
      url: `${BASE_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2
      }
    })
      .then((response) => {
        console.log('회원가입성공')
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const signin = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${BASE_URL}/accounts/login/`,
      data: {
        username,
        password
      }
    })
      .then((response) => {
        console.log('로그인 성공')
        token.value = response.data.key
        router.push('/')
      })
      .catch((error) => {
        console.log(error)
      })
  }
  return {
    articles, token, isLogin,
    getArticles, createArticle, signup, signin
  }
}, { persist: true })
