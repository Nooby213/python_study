<template>
  <li>
    {{ product.id }} - {{ product.title }} - {{ product.body }}
  </li>
</template>

<script setup>
import { ref, defineProps } from 'vue'

defineProps({
  product: Object
})


</script>

<style scoped></style>