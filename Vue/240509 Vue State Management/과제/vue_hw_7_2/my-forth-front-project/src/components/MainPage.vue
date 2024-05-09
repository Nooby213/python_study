<template>
  <div>
    <ParentPage v-for="family in store.families" :family="family" class="parent-container" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ParentPage from '@/components/ParentPage.vue';
import { useFamilyInfoStore } from '@/stores/familyInfos'

const store = useFamilyInfoStore()

</script>

<style scoped>
.parent-container {
  background-color: #F9F9F9;
  text-align: center;
  padding: 15px;
  border: 1px solid #CCCCCC;
  margin-bottom: 20px;
  margin-left: 40px;
  margin-right: 40px;
}
</style>