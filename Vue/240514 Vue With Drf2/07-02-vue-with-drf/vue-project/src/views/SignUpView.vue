<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signup">
      <div>
        <label for="username">username : </label>
        <input type="text" v-model.trim="username" id="username">
      </div>
      <div>
        <label for="password1">password : </label>
        <input type="password" v-model.trim="password1" id="password1">
      </div>
      <div>
        <label for="password2">password certification : </label>
        <input type="password" v-model.trim="password2" id="password2">
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const username = ref('')
const password1 = ref('')
const password2 = ref('')
const store = useCounterStore()

const signup = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signup(payload)
}
</script>

<style></style>
