<template>
  <header>
    <nav>
    </nav>
  </header>
  <h1>할 일 목록</h1>
  <TodoList :todos="todoStore.todos"></TodoList>
  <RouterView />
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterView } from 'vue-router'
import { useTodoStore } from './stores/todoStore';
import TodoList from '@/components/TodoList.vue';
import TodoListItem from '@/components/TodoListItem.vue';

const todoStore = useTodoStore()
onMounted(() => {
  todoStore.getTodos()
})

</script>

<style scoped></style>
