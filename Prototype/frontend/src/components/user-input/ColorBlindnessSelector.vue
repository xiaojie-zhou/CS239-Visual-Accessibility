<script setup>
import ColorBlindnessOption from './ColorBlindnessOption.vue'
import { ref, defineEmits } from 'vue';
const selectedType = ref('normal');
const emit = defineEmits(['update-selected']);
const handleSelection = (type) => {
  selectedType.value = type;
  console.log('[ColorblindnessSelector]: updated color type', type);
  emit('update-selected', type); // Emit event to the parent
};
</script>

<template>
    <div class="title">
        Choose the type of color blindness
    </div>
    <div>
        <ColorBlindnessOption type="normal" :selectedType="selectedType" @select="handleSelection"/>
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
    font-weight: 600;
}
</style>