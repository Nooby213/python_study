<template>
  <li>
    <RouterLink :to="{ name: 'post-detail', params: { id: post.id } }">제목 : {{ post.id + 1 }}</RouterLink>
  </li>
</template>

<script setup>
import { ref } from 'vue'
import PostDetail from '@/components/PostDetail.vue';


const props = defineProps({
  post: Object
})


</script>

<style scoped></style>