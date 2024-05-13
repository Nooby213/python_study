<template>
  <div class="ctr">
    <nav class="nav-bar">
      <router-link to="/" class="nav-link">Home</router-link>
    </nav>
    <RouterView />

  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router';


</script>

<style scoped>
.ctr {
  display: flex;
  flex-wrap: wrap;
  text-align: center;
}

.nav-link {
  color: inherit;
  text-decoration: none;
}

.router-link-exact-active {
  color: inherit !important;
}

.nav-bar {
  background-color: #333333;
  justify-content: center;
  align-content: center;
  color: #FFFFFF;
  width: 100%;
  height: 50px;
}
</style>
