<script setup>
  import DownloadBtn from './DownloadBtn.vue'
  import SimulationBtn from './SimulationBtn.vue'
  const props = defineProps({
    protImageURL: String,
    deutImageURL: String,
    tritImageURL: String
  });
</script>

<template>
<div class="buttons">
    <SimulationBtn 
      :protImageURL="props.protImageURL"
      :deutImageURL="props.deutImageURL"
      :tritImageURL="props.tritImageURL"
    />
    <DownloadBtn />
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
  }
  .buttons {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    gap: 10px;
    margin-top: 20px;
  }
</style>