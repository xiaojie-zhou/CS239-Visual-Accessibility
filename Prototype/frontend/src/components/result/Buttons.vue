<script setup>
  import DownloadBtn from './DownloadBtn.vue'
  import SimulationBtn from './SimulationBtn.vue'
  import InfoBtn from './InfoBtn.vue'
  import { ref } from 'vue';
  const activeTooltip = ref(null);
  const toggleTooltip = (tooltip) => {
    activeTooltip.value = activeTooltip.value === tooltip ? null : tooltip;
  };
</script>

<template>
<div class="buttons">
    <SimulationBtn 
        :isActive="activeTooltip === 'simulation'" 
        @toggle="toggleTooltip('simulation')" 
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