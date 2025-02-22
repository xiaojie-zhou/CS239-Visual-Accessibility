<script setup>
import UserInputColumn from './user-input/UserInputColumn.vue'
import ResultColumn from './result/ResultColumn.vue'
</script>

<template>
  <div class="body-container">
    <UserInputColumn />
    <div class="separator"></div>
    <ResultColumn />
  </div>
</template>

<style scoped>
.body-container {
  display: flex;
  width: 100%;
  height: 100vh;
}

.separator {
  width: 2px;
  background-color: #ccc;
}
</style>