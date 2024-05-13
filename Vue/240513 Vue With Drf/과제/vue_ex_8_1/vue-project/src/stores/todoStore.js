import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useTodoStore = defineStore('todo', () => {
  const todos = ref()
  const BASE_URL = 'http://127.0.0.1:8000/api/v1/todos/'
  const getTodos = function () {
    axios({
      method: 'get',
      url: `${BASE_URL}`
    })
      .then((response) => {
        todos.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }
  return {
    todos,
    getTodos
  }
}, { persist: true })
