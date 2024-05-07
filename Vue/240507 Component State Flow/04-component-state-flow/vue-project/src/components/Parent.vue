<template>
  <div>
    <ParentChild my-msg="message" :dynamic-props="name" @some-event="someCallback" @my-focus="someCallback2"
      @emitArgs="getNumbers" @update-name="updateName" />
  </div>
  <ParentItem v-for="item in items" :key="item.id" :my-prop="item" />
</template>

<script setup>
import { ref } from 'vue'
import ParentChild from '@/components/ParentChild.vue'
import ParentItem from '@/components/ParentItem.vue'
const name = ref('Alice')

const items = ref([
  { id: 1, name: '사과' },
  { id: 2, name: '바나나' },
  { id: 3, name: '딸기' }
])

const someCallback = function () {
  console.log('ParentChild가 발신한 이벤트를 수신했다.')
}

const someCallback2 = function () {
  console.log('defineEmits 방식으로 발신한 이벤트를 수신했다.')
}

const getNumbers = function (...args) {
  args.forEach((num) => {
    console.log(num)
  })
}

const updateName = function () {
  name.value = 'Bella'
}
</script>

<style scoped></style>