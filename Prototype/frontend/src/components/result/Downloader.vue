<script setup>
  import Buttons from './Buttons.vue';
</script>

<template>
  <div class="feedback-container">
    <div class="new-diagram">
      <!-- generated diagram here -->
      <div class="buttons">
        <Buttons />
      </div>
    </div>
  </div>  
</template>

<style scoped>
  .feedback-container {
    margin-top: 0px;
    display: flex;
    flex-direction: column;
  }
 .new-diagram {
    width: 700px;
    height: 400px;
    border: 2px dashed #3498db;
    border-radius: 5px;
    background-color: #f9f9f9;
    position: relative;
  }
  .buttons {
    position: absolute;
    bottom: 10px;
    right: 10px;
  }
</style>