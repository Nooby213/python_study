<template>
  <div>
    <!-- <p>{{ number }}</p>
    <p>{{ store.count }}</p>
    <p>{{ store.doubleCount }}</p>
    <button @click="store.increment()">+</button> -->
    <h1>Todo Pjt</h1>
    <h2>완료된 todo : {{ store.doneTodoCount }}</h2>
    <TodoForm />
    <TodoList />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import TodoForm from '@/components/TodoForm.vue';
import TodoList from '@/components/TodoList.vue';
import { useMyCounterStore } from '@/stores/counter';

const store = useMyCounterStore()


/*
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()

// state
const number = store.count
// getters
console.log(store.doubleCount)
// actions 호출
*/

</script>

<style scoped></style>