<template>
  <main>
    <h1>할 일 목록</h1>
    <p>{{ todoStore.todos }}</p>
  </main>
</template>

<script setup>
import { onMounted } from 'vue';
import { useTodoStore } from '@/stores/todoStore'

const todoStore = useTodoStore()
onMounted(() => {
  todoStore.getTodos()
})
</script>

<style></style>
