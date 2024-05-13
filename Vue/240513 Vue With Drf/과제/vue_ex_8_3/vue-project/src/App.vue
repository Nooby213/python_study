<template>
  <RouterLink to="/">할 일 목록</RouterLink>
  <header>
    <nav>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped></style>
