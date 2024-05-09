<template>
  <li>
    {{ product.id }} - {{ product.title }} - {{ product.body }} <button
      @click="store.deleteProduct(product.id)">Delete</button>
  </li>
</template>

<script setup>
import { ref, defineProps } from 'vue'
import { useProductStore } from '@/stores/product'

defineProps({
  product: Object
})
const store = useProductStore()

</script>

<style scoped></style>