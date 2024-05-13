<template>
  <div>
    <h1>DetailView</h1>
    <div v-if="article !== null">
      <p>{{ article.id }}</p>
      <p>{{ article.title }}</p>
      <p>{{ article.content }}</p>
      <p>{{ article.created_at }}</p>
      <p>{{ article.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
const route = useRoute()
const article = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
    .then((response) => {
      console.log(response)
      article.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})
</script>

<style></style>
