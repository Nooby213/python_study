<template>
  <header>
    <h1 class="title green">My Gallery</h1>
  </header>
  <section class="container">
    <div class="row">
      <MyComponent v-for="index in numberOfItems" :key="index" />
    </div>
  </section>
</template>

<script setup>
import MyComponent from '@/components/MyComponent.vue'
import { ref } from 'vue'
const numberOfItems = ref(4)
</script>

<style scoped>
.green {
  background-color: #D1E7DE;
}

.title {
  display: flex;
  justify-content: center;
  align-items: center;
  position: sticky;
  height: 100px;
  font-weight: bold;
  font-size: 50px;
}
</style>
