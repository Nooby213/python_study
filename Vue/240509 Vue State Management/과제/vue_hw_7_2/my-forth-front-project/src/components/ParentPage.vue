<template>
  <div>
    <h2>부모 컴포넌트</h2>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>
    <ChildPage v-for="child in family.children" :child="child" class="child-container" />
  </div>
</template>

<script setup>
import { ref, defineProps } from 'vue'
import ChildPage from '@/components/ChildPage.vue'

defineProps({
  family: Object
})

</script>

<style scoped>
.child-container {
  background-color: white;
  padding: 15px;
  border: 1px solid #CCCCCC;
  margin-bottom: 20px;
  margin-left: 40px;
  margin-right: 40px;
}
</style>