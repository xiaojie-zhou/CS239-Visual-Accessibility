<script setup>
import Uploader from './Uploader.vue'
import ColorBlindnessSelector from './ColorBlindnessSelector.vue'
import GenerateBtn from './GenerateBtn.vue'
</script>

<template>
    <div class="left-column">
        <div class="uploader"><Uploader /></div>
        <div class="color-blindness-selector"><ColorBlindnessSelector /></div>
        <div><GenerateBtn /></div>
    </div>
</template>


<style scoped>
.left-column {
    flex: 1;
    flex-direction: column;
    display: flex;
    align-items: center;
  }
</style>
