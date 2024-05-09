<template>
  <div>
    <h4>자식 페이지</h4>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
import { ref, defineProps } from 'vue'

defineProps({
  child: Object
})
</script>

<style scoped></style>