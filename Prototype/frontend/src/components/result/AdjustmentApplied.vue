<script setup>
import DownloadBtn from './DownloadBtn.vue'
import InfoBtn from './InfoBtn.vue'
</script>

<template>
  <div class="feedback-container">
    <div class="new-diagram">
        <!-- generated diagram here -->
    </div>
    <div class="buttons">
        <DownloadBtn />
        <InfoBtn />
    </div>
  </div>  
</template>

<style scoped>
.feedback-container {
    display: flex;
    flex-direction: column;
}
 .new-diagram {
    width: 300px;
    height: 150px;
    border: 2px dashed #3498db;
    border-radius: 5px;
    background-color: #f9f9f9;
  }
  .buttons {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
  }
</style>