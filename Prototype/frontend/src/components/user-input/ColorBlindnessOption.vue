<template>
    <div class="option-container" @click="toggleSelect">
      <div class="circle-container">
        <div class="circle" :class="{ selected: isSelected }"></div>
      </div>
      <div class="option-text">
        <div class="option-title">
          {{ optionTitle }} 
          <a v-if="showLink" :href="hlink" target="_blank">
            <img src="../icons/external-link.svg" alt="Learn More"/>
          </a>
        </div>
        <div class="option-subtitle">{{ optionSubtitle }}</div>
      </div>
    </div>
  </template>
  
<script setup>
  import { computed, defineEmits} from 'vue';
  
  const props = defineProps({
    type: String,
    selectedType: String,
  });
  const isSelected = computed(() => props.selectedType === props.type);
  const showLink = computed(() => props.type !== "normal");
  const emit = defineEmits(["select"]);
  const toggleSelect = () => { // notify parent when clicked
    emit("select", props.type); 
  };
  
  const optionTitle = computed(() => {
    switch (props.type) {
      case 'normal':
        return 'Default';
      case 'prot':
        return 'Red Color Blindness';
      case 'deut':
        return 'Green Color Blindness';
      case 'trit':
        return 'Blue Color Blindness';
      case 'gray':
        return 'Complete Color Blindness';
    }
  });

  const optionSubtitle = computed(() => {
    switch (props.type) {
      case 'normal':
        return 'Generally accessible to most people';
      case 'prot':
        return 'Protanopia / Protanomaly';
      case 'deut':
        return 'Deuteranopia / Deuteranomaly';
      case 'trit':
        return 'Tritanopia / Tritanomaly';
      case 'gray':
        return '';
    }
  });

  const hlink = computed(() => {
    switch (props.type) {
      case 'prot':
        return 'https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/color-blindness/types-color-vision-deficiency#:~:text=color%20vision%20deficiency%3A-,Deuteranomaly,-is%20the%20most';
      case 'deut':
        return 'https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/color-blindness/types-color-vision-deficiency#:~:text=of%20normal%20activities.-,Protanomaly,-makes%20certain%20shades';
      case 'trit':
        return 'https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/color-blindness/types-color-vision-deficiency#:~:text=color%20vision%20deficiency%3A-,Tritanomaly,-makes%20it%20hard';
      case 'complete':
        return 'https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/color-blindness/types-color-vision-deficiency#:~:text=look%20less%20bright.-,Complete%20color%20vision%20deficiency,-If%20you%20have';
    }
  });
</script>
  
<style scoped>
  .option-container {
    display: flex;
    flex-direction: row;
    margin: 10px 0;
  }

  .circle-container {
    padding-top: 10px;
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
    padding-top: 10px;
    height: 35px;
    margin-left: 10px;
    transition: filter 0.3s ease;
  }

  img:hover {
    filter: brightness(0) saturate(100%) invert(40%) sepia(100%) saturate(200%) hue-rotate(180deg);
  }

  .option-text {
    display: flex;
    flex-direction: column;
  }
  .option-title {
    font-size: 30px;
  }
  .option-subtitle {
    font-size: 25px;
    color: gray;
  }

</style>
  