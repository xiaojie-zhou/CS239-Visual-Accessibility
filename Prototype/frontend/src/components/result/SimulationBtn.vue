<script setup>
  import {ref} from "vue";
  import * as Cronitor from "@cronitorio/cronitor-rum";
  const props = defineProps({
    protImageURL: String,
    deutImageURL: String,
    tritImageURL: String
  });
  const isActive = ref(false);
  const toggle = () => {
    isActive.value = !isActive.value;
    Cronitor.track('toggle-simulation');
  };
</script>

<template>
    <div class="button-container">
      <button class="button"
        @click="toggle" :class="{ active: isActive }">
        <img src="@/components/icons/glasses-black.svg" class="icon" alt="Simulation Icon" />
      </button>

      <!-- tooltip  -->
      <div v-show="isActive" class="tooltip">
        <div class="tooltip-title">
          Color Blind Simulations of the Original Diagram
        </div>
        <div class="tooltip-content-container">
          <div class="sim-container">
          Red Color Blindness
          <img class="sim-img" :src="props.protImageURL"/>
          </div>
          <div class="sim-container">
            Green Color Blindness
            <img class="sim-img" :src="props.deutImageURL"/>
          </div>
          <div class="sim-container">
            Blue Color Blindness
            <img class="sim-img" :src="props.tritImageURL"/>
          </div>
        </div>
      </div>
   </div>
</template>

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

  .button:hover {
    background-color: #3498db;
  }
  .button:hover .icon {
      filter: invert(100%) sepia(0%) saturate(0%) brightness(200%) contrast(100%);
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
    top: 100%; /* Position it directly below the button */
    left: 50%;
    transform: translateX(-50%);
    background-color: #3498db;
    color: white;
    padding: 6px 12px;
    border-radius: 10px;
    font-size: 12px;
    white-space: nowrap;
    opacity: 1;
    z-index: 10; /* Ensure it's above other elements */
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    padding: 30px;
  }

  .tooltip-title {
    font-size: 40px;
    font-weight: 600;
    text-align: center;
  }

  .tooltip-content-container {
    display: flex;
    flex-direction:row;
  }

  .sim-container {
    display: flex;
    flex-direction: column;
    font-size: 30px;
    padding: 10px;
    text-align: center;
  }
  .sim-img {
    height: 300px;
  }
</style>
