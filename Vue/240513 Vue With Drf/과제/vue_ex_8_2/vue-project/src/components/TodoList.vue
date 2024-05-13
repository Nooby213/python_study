<template>
  <div>
    <TodoListItem v-for="todo in todos" :todo="todo"></TodoListItem>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import TodoListItem from './TodoListItem.vue';

defineProps({
  todos: Object
})
</script>

<style scoped></style>