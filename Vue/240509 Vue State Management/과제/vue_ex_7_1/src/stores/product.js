import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('product', () => {
  let id = 1
  const products = ref([
    { id: id++, title: 'Product 1', body: '똠양꿍' },
    { id: id++, title: 'Product 2', body: '쌀국수' },
    { id: id++, title: 'Product 3', body: '푸팟퐁커리' }
  ])
  return {
    products,
  }
})
