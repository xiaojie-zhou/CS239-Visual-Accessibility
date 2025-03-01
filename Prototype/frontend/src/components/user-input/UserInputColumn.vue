<script setup>
import Uploader from './Uploader.vue'
import ColorBlindnessSelector from './ColorBlindnessSelector.vue'
import GenerateBtn from './GenerateBtn.vue'
</script>

<template>
    <div>
        <div class="uploader"><Uploader /></div>
        <div class="color-blindness-selector"><ColorBlindnessSelector /></div>
        <div class="generate-btn"><GenerateBtn /></div>
    </div>
</template>


<style scoped>
.color-blindness-selector{
 margin-top: 30px
}
.generate-btn {
    margin-top: 30px;
}
</style>
