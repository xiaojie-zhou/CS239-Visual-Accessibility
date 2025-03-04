<script setup>
import ColorBlindnessOption from './ColorBlindnessOption.vue'
import { ref } from 'vue';
const selectedType = ref('default');
const handleSelection = (type) => {
  selectedType.value = type;
};
</script>

<template>
    <div class="title">
        Choose the type of color blindness:
    </div>
    <div>
        <ColorBlindnessOption type="default" :selectedType="selectedType" @select="handleSelection"/>
        <ColorBlindnessOption type="prot" :selectedType="selectedType" @select="handleSelection"/>
        <ColorBlindnessOption type="deut" :selectedType="selectedType" @select="handleSelection"/>
        <ColorBlindnessOption type="trit" :selectedType="selectedType" @select="handleSelection"/>
        <ColorBlindnessOption type="gray" :selectedType="selectedType" @select="handleSelection"/>
    </div>
</template>

<style scoped>
.title {
    color: black;
    font-size: 40px;
}
</style>