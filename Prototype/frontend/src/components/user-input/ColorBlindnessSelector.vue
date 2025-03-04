<script setup>
import ColorBlindnessOption from './ColorBlindnessOption.vue'
import { ref } from 'vue';
const selectedType = ref(null);
const handleSelection = (type) => {
  selectedType.value = type;
};
</script>

<template>
    <div class="title">
        Choose the type of color blindness:
    </div>
    <div>
        <ColorBlindnessOption type="rg" :selectedType="selectedType" @select="handleSelection"/>
        <ColorBlindnessOption type="by" :selectedType="selectedType" @select="handleSelection"/>
        <ColorBlindnessOption type="complete" :selectedType="selectedType" @select="handleSelection"/>
    </div>
</template>

<style scoped>
.title {
    color: black;
    font-size: 40px;
}
</style>