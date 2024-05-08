<template>
  <div>
    <RouterLink :to="{ name: 'home' }">Home</RouterLink> |
    <RouterLink :to="{ name: 'about' }">About</RouterLink>
  </div>
  <RouterView />
</template>

<script setup>
import { ref } from 'vue'


</script>

<style scoped></style>