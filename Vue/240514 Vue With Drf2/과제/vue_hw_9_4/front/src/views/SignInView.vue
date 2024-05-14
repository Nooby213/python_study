<template>
  <div>
    <h1>로그인 페이지</h1>
    <form @submit.prevent="signin">
      <div>
        <label for="username">username : </label>
        <input type="text" name="username" id="username" v-model="username">
      </div>

      <div>
        <label for="password">password : </label>
        <input type="password" name="password" id="password" v-model="password">
      </div>

      <input type="submit" value="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()
const username = ref(null)
const password = ref(null)

const signin = function () {
  const payload = {
    username: username.value,
    password: password.value,
  }
  store.signin(payload)
}

</script>

<style scoped></style>
