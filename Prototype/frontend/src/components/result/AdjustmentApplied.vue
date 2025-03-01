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
  <div class="feedback-container">
    <div class="new-diagram">
        <!-- generated diagram here -->
    </div>
    <div class="buttons">
        <SimulationBtn 
          :isActive="activeTooltip === 'simulation'" 
          @toggle="toggleTooltip('simulation')" 
        />
        <InfoBtn 
          :isActive="activeTooltip === 'info'" 
          @toggle="toggleTooltip('info')" 
        />
        <DownloadBtn />
    </div>
  </div>  
</template>

<style scoped>
  .feedback-container {
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