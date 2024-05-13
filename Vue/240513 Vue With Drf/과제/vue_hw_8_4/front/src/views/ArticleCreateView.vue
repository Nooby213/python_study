<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="createArticle">
      <p>제목 : <input type="text" v-model="title"></p>
      <p>내용 : <input type="text" v-model="content"></p>
      <input type="submit" value="create">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';
import { useArticleStore } from '@/stores/articles'
import axios from 'axios'

const title = ref(null)
const content = ref(null)
const articleStore = useArticleStore()
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${articleStore.API_URL}`,
    data: {
      title: title.value,
      content: content.value
    }
  })
    .then((response) => {
      router.push('/')
    })
    .catch((error) => {
      console.log(error)
    })
}


</script>

<style scoped></style>