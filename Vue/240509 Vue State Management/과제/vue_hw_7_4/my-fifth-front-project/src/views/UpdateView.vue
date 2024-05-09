<template>
  <div>
    <p>이름: {{ accountBalance[0].name }}</p>
    <p>잔고: {{ accountBalance[0].balance }}</p>
    <button @click=upBalance>+</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useBalanceStore } from '@/stores/balance'
import { storeToRefs } from 'pinia'

const route = useRoute()
const name = ref(route.params.name)
const store = useBalanceStore()
const { balanceInfo } = storeToRefs(store)
const accountBalance = balanceInfo.value.filter((balance) => balance.name === name.value)
const upBalance = function () {
  accountBalance[0].balance += 1000
}
</script>

<style scoped></style>