<template>
  <div>
    <h1>router 연습하기</h1>
    <RouterLink :to="{ name: 'some' }">Some</RouterLink> |
    <RouterLink :to="{ name: 'other' }">Other</RouterLink> |
    <RouterLink :to="{ name: 'students' }">Students</RouterLink>

    <RouterView />
  </div>
</template>

<script setup>
import { ref } from 'vue'


</script>

<style scoped></style>