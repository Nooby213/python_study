import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000/api/v1/articles/'
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}`
    })
      .then((res) => {
        articles.value = res.data
        console.log(res)
      })
  }

  return {
    articles, API_URL,
    getArticles
  }
})
