<template>
  <div class="container">
    <p>이름: {{ account.name }}</p>
    <p>잔고: {{ account.balance }}</p>
    <RouterLink :to="{ name: 'update', params: { name: account.name } }"><button class="button">updateBalance</button>
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { ref, defineProps } from 'vue'

defineProps({
  account: Object
})


</script>

<style scoped>
.container {
  margin-left: 20px;
  margin-top: 40px;
}

.button {
  background-color: #007BFF;
  border: 1px solid #007BFF;
  border-radius: 10%;
  color: white;
}
</style>