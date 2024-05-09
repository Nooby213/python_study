<template>
  <div>
    <TodoListItem v-for="todo in store.todos" :key="todo.id" :todo="todo" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import TodoListItem from '@/components/TodoListItem.vue';
import { useMyCounterStore } from '@/stores/counter';

const store = useMyCounterStore()
</script>

<style scoped></style>