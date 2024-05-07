<template>
  <div>
    <p>{{ myMsg }}</p>
    {{ dynamicProps }}
    <ParentGrandChild :my-msg="myMsg" @update-name="updateName" />
    <button @click="$emit('someEvent')">전송</button>
    <button @click="buttonClick">버튼 2</button>
    <button @click="emitArgs">추가 인자 전달</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ParentGrandChild from '@/components/ParentGrandChild.vue';
// 내려받은 props를 선언
// 1. 문자열 배열을 사용한 선언.
// defineProps(['myMsg'])

// 2. 객체를 사용한 선언 * 사용 권장
// defineProps({
//   myMsg: String
// })

const props = defineProps({
  // myMsg: String,
  myMsg: {
    type: String,
    required: true
  },
  dynamicProps: String
})
console.log(props)
console.log(props.myMsg)

const emit = defineEmits(['myFocus', 'emitArgs', 'updateName'])

const buttonClick = function () {
  emit('myFocus')
}

const emitArgs = function () {
  emit('emitArgs', 1, 2, 3)
}

const updateName = function () {
  emit('updateName')
}
</script>

<style scoped></style>