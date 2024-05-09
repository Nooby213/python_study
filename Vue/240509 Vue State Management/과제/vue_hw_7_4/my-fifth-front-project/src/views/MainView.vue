<template>
  <div>
    <h1>메인 페이지</h1>
    <MainPage v-for="account in store.balanceInfo" :account="account" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import MainPage from '@/components/MainPage.vue'
import { useBalanceStore } from '@/stores/balance'

const store = useBalanceStore()

</script>

<style scoped></style>