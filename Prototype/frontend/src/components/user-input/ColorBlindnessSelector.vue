<script setup>
import ColorBlindnessOption from './ColorBlindnessOption.vue'
</script>
<template>
    <div>
        Choose the type of color blindness
    </div>
    <div>
        <ColorBlindnessOption type="rg"/>
        <ColorBlindnessOption type="by"/>
        <ColorBlindnessOption type="complete"/>
    </div>
</template>