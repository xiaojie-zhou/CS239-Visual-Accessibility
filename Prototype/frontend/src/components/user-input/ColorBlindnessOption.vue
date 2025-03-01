<template>
    <div class="option-container" @click="toggleSelect">
      <div class="circle" :class="{ selected: isSelected }"></div>
      <p>{{ typeName }} Color Blindness</p>
      <a :href="hlink" target="_blank">
        <img src="../icons/external-link.svg" alt="Learn More"/>
      </a>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  
  const props = defineProps({
    type: String,
  });
  
  const isSelected = ref(false); // Track the selected state
  
  const toggleSelect = () => {
    isSelected.value = !isSelected.value; 
  };
  
  const typeName = computed(() => {
    switch (props.type) {
      case 'rg':
        return 'Red-Green';
      case 'by':
        return 'Blue-Yellow';
      case 'complete':
        return 'Complete';
      default:
        return '';
    }
  });

  const hlink = computed(() => { // TODO: link to info page
    switch (props.type) {
      case 'rg':
        return 'https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/color-blindness/types-color-vision-deficiency#:~:text=seeing%20different%20colors.-,Red%2Dgreen%20color%20vision%20deficiency,-The%20most%20common';
      case 'by':
        return 'https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/color-blindness/types-color-vision-deficiency#:~:text=green%20at%20all.-,Blue%2Dyellow%20color%20vision%20deficiency,-This%20less%2Dcommon';
      case 'complete':
        return 'https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/color-blindness/types-color-vision-deficiency#:~:text=look%20less%20bright.-,Complete%20color%20vision%20deficiency,-If%20you%20have';
    }
  });
  </script>
  
  <style scoped>
  .option-container {
    display: flex;
    align-items: center;
    margin: 10px 0;
  }
  
  .circle {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    border: 2px solid #3498db;
    margin-right: 10px;
    transition: background-color 0.3s ease;
    cursor: pointer;
  }
  
  .circle.selected {
    background-color: #3498db;
  }
  
  img {
    height: 35px;
    margin-left: 10px
  }

  p {
    font-size: 40px;
  }
  </style>
  