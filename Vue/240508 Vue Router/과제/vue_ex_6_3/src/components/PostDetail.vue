<template>
  <div>
    <h1>{{ posts[idx].id }}</h1>
    <h1>{{ posts[idx].title }}</h1>
    <h1>{{ posts[idx].content }}</h1>

  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, onBeforeRouteUpdate } from 'vue-router';
const route = useRoute()
const idx = ref(route.params.id)
let id = 1
const posts = ref([
  { id: id++, title: '1번', content: '게시글1' },
  { id: id++, title: '2번', content: '게시글2' },
  { id: id++, title: '3번', content: '게시글3' }
])

onBeforeRouteUpdate((to, from) => {
  idx.value = to.params.id
})
</script>

<style scoped></style>