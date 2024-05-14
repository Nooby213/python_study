<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useArticleStore } from './stores/articles';
const store = useArticleStore()
</script>

<template>
  <header>
    <div class="wrapper">
      <nav v-if="store.isLogin === true">
        <RouterLink to="/">Home</RouterLink>
      </nav>
      <nav v-else>
        <RouterLink :to="{ name: 'signup' }">Signup</RouterLink> |
        <RouterLink :to="{ name: 'signin' }">singin</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped></style>
