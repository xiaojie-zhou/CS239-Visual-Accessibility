<template>
    <div class="option-container" @click="toggleSelect">
      <div class="circle" :class="{ selected: isSelected }"></div>
      <p>{{ typeName }} Color Blindness</p>
      <a :href="hlink" target="_blank">
        <img src="../icons/external-link-svgrepo-com.svg"/>
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
        return 'https://www.google.com';
      case 'by':
        return 'https://www.google.com';
      case 'complete':
        return 'https://www.google.com';
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
    width: 20px;
    height: 20px;
    border-radius: 50%; /* circle */
    border: 2px solid #3498db;
    margin-right: 10px;
    transition: background-color 0.3s ease;
    cursor: pointer;
  }
  
  .circle.selected {
    background-color: #3498db;
  }
  
  img {
    height: 15px;
  }
  </style>
  