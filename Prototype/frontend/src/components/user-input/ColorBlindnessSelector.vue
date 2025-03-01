<script setup>
import ColorBlindnessOption from './ColorBlindnessOption.vue'
</script>
<template>
    <div class="title">
        Choose the type of color blindness:
    </div>
    <div>
        <ColorBlindnessOption type="rg"/>
        <ColorBlindnessOption type="by"/>
        <ColorBlindnessOption type="complete"/>
    </div>
</template>

<style scoped>
.title {
    color: black;
    font-size: 40px;
}
</style>