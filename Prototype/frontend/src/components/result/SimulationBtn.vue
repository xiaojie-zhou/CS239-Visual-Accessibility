<template>
    <div class="button-container">
      <button class="button" 
        @click="toggle" 
        :class="{ 'active': isActive }">
        <img src="@/components/icons/glasses-black.svg" class="icon" alt="Simulation Icon" />
      </button>
      <div v-if="isActive" class="tooltip">
          <SimulationTooltip />
      </div>
   </div>
  </template>

<script setup>
  import SimulationTooltip from './SimulationTooltip.vue';
  defineProps({ isActive: Boolean });
  const emit = defineEmits(['toggle']);
  const toggle = () => emit('toggle');
</script>
    
<style scoped>
  .button-container {
    position: relative;
    display: inline-block;
  }

  .button {
    width: 80px;
    height: 80px;
    font-size: 16px;
    border: 4px solid #3498db;
    background-color: white;
    border-radius: 50%;
    cursor: pointer;
    transition: background-color 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0;
  }

  .button.active{
    background-color: #3498db;
  }

  .button:focus {
    outline: none;
  }

  .icon {
    width: 45px;
    height: 45px;
    filter: invert(29%) sepia(78%) saturate(925%) hue-rotate(180deg) brightness(96%) contrast(90%);
  }

  .button.active .icon {
    filter: invert(100%) sepia(0%) saturate(0%) brightness(200%) contrast(100%);
  }

  .tooltip {
    position: absolute;
    margin-top: 20px;
    height: 100px;
    width: 200px;
    transform: translateX(-50%);
    background-color: #3498db;
    color: white;
    padding: 6px 12px;
    border-radius: 5px;
    font-size: 12px;
    white-space: nowrap;
    opacity: 0.9;
    transition: opacity 0.3s ease-in-out;
  }
</style>