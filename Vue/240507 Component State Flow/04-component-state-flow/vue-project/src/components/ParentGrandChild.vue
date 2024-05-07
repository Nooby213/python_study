<template>
  <div>
    <p>{{ myMsg }}</p>
    <button @click="updateName">이름 변경</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
defineProps({
  myMsg: String
})

const emit = defineEmits(['updateName'])

const updateName = function () {
  emit('updateName')
}
</script>

<style scoped></style>