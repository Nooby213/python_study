<template>
  <div>
    <RouterLink :to="{ name: 'user-profile' }">Profile</RouterLink>
    <RouterLink :to="{ name: 'user-posts' }">Posts</RouterLink>
    <h1>UserView</h1>
    <!-- route객체 직접 접근 -->
    <h2>{{ $route.params.id }}번 유저 페이지</h2>
    <h2>{{ userId }}번 User 페이지</h2>
    <button @click="goHome">홈으로</button>
    <button @click="routeUpdate">100번 유저 페이지로!</button>
    <hr>
    <RouterView />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

// JS를 이용한 route객체값 접근
const route = useRoute()
const userId = ref(route.params.id)

const router = useRouter()
const goHome = function () {
  // router.push({ name: 'home' })

  // 뒤로 가기 안됌 현재 위치 바꾸기
  router.replace({ name: 'home' })
}

onBeforeRouteLeave((to, from) => {
  const answer = window.confirm('정말 떠나실 건가요?')
  if (!answer) {
    return false
  }
  // return 이 생략되어 있으면 to로 간다.
})

const routeUpdate = function () {
  router.push({ name: 'user', params: { id: 100 } })
}

onBeforeRouteUpdate((to, from) => {
  userId.value = to.params.id
})
</script>

<style scoped></style>