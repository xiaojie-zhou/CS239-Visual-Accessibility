<script setup>
import UserInputColumn from './user-input/UserInputColumn.vue'
import ResultColumn from './result/ResultColumn.vue'
</script>

<template>
  <div class="body-container">
    <UserInputColumn class="column"/>
    <div class="column separator-container">
      <div class="separator">
      </div>
    </div>
    <ResultColumn class="column"/>
  </div>
</template>

<style scoped>
.body-container {
  display: flex; 
  flex-direction: row;
  justify-content: center; 
  width: 100%;
  height: 100vh;
  margin-top: 30px;
}
.separator {
  height: 60%; /* Restore the height */
  width: 2px;
  background-color: #ccc;
}
.column {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.separator-container {
  margin: 30px;
}
</style>