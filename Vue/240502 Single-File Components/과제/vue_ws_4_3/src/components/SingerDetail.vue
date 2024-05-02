<template>
  <div class="singer">
    <h2>가수 이름</h2>
    <img class="img" src="/src/assets/singer.jpg" alt="">
    <p>가수 소개글</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'


</script>

<style scoped>
.singer {
  border: 1px solid black;
  text-align: center;
}

.img {
  width: 200px;
  border-radius: 70%;
}
</style>