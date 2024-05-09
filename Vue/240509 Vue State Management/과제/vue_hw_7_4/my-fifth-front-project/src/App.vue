<template>
  <RouterLink :to="main">main</RouterLink>
  <div>
    <h1>pinia + router 연습하기</h1>
  </div>
  <RouterView />
</template>

<script setup>
import { ref } from 'vue'
import MainView from '@/views/MainView.vue';


</script>

<style scoped></style>