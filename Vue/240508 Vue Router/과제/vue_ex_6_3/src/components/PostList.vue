<template>
  <div>
    <ol>
      <PostListItem v-for="post in posts" :key="id" :post="post" />
    </ol>
  </div>
  <hr>
  <RouterView />
</template>

<script setup>
import { ref } from 'vue'
import PostListItem from '@/components/PostListItem.vue';

let id = 0
const posts = ref([
  { id: id++, title: '1번', content: '게시글1' },
  { id: id++, title: '2번', content: '게시글2' },
  { id: id++, title: '3번', content: '게시글3' }
])
</script>

<style scoped></style>