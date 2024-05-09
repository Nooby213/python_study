<template>
  <div>
    <Notice />
    <ProductList />
  </div>
</template>

<script setup>
import ProductList from '@/components/ProductList.vue'
import Notice from '@/components/Notice.vue'
import { useProductStore } from '@/stores/product'
import { onMounted } from 'vue';

const store = useProductStore()
onMounted(() => {
  // store.goAxios()
})
</script>

<style scoped></style>
