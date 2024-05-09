<template>
  <div>
    <form @submit.prevent="addTodo(todoText)" ref="formElem">
      <input type="text" v-model="todoText">
      <input type="submit" value="작성">
      <input type="reset" value="리셋">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useMyCounterStore } from '@/stores/counter'

const store = useMyCounterStore()
const todoText = ref('')
const formElem = ref('null')
console.log(formElem)

const addTodo = function (todoText) {
  store.addTodo(todoText)
  console.log(formElem.value)
  formElem.value.reset()
  console.log(formElem.value)

}

</script>

<style scoped></style>