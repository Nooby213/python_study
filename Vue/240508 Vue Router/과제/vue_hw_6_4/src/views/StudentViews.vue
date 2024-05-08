<template>
  <div>
    <h1>학생 상세 정보 목록 입니다.</h1>
    <p v-for="student in students" :key="id" :student="student" @click="callDetail(student)">
      {{ student.name }} 학생 정보 보기
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import StudentDetailView from '@/views/StudentDetailView.vue';

let id = 0
const students = ref([
  { id: id++, name: '김하나' },
  { id: id++, name: '김두리' },
  { id: id++, name: '김서이' }
])
const router = useRouter()
const callDetail = function (student) {
  // router.push(`/students/${student.name}`)
  router.push({ name: 'student-detail', params: { studentName: student.name } })
}
</script>

<style scoped></style>