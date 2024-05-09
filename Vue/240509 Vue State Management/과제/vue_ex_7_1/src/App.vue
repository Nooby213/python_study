<template>
  <div>
    <h1>Product List</h1>
    <ul>
      <h2>
        <ProductList v-for="product in products" :product="product"></ProductList>
      </h2>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useProductStore } from '@/stores/product';
import ProductList from '@/components/ProductList.vue'

const store = useProductStore()
const products = store.products
</script>

<style scoped></style>