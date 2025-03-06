<script setup>
import { ref, defineEmits } from 'vue';
import Uploader from './Uploader.vue'
import ColorBlindnessSelector from './ColorBlindnessSelector.vue'
import InactiveGenerateBtn from './InactiveGenerateBtn.vue'
import GenerateBtn from './GenerateBtn.vue'

const imageToken = ref(null);
const selectedColorBlindType = ref('normal');
const emit = defineEmits(["result-fetched-parent"]);

// receive selected color type from ColorBlindnessSelector
const handleColorUpdate = (colorBlindType) => {
  selectedColorBlindType.value = colorBlindType;
  console.log('[UserInput]updated color type '+ colorBlindType);
};

// receive token from Uploader
const handleImageToken = (token) => {
  imageToken.value = token; 
  console.log("[UserInput]token received from Uploader="+ token);
};

// receive score and new image URL from GenerateBtn
// then emit them to parent component
const handleResultFetched = (result) => {
    emit("result-fetched-parent", {
        score: result.score,
        newImageURL: result.newImageURL,
    });
    console.log("[UserInput]score received from GenerateBtn="+result.score);
}
</script>

<template>
    <div>
        <div class="uploader"><Uploader @image-uploaded="handleImageToken"/></div>
        <div class="color-blindness-selector"><ColorBlindnessSelector @update-selected="handleColorUpdate"/></div>
        <div v-if="imageToken" class="generate-btn"><GenerateBtn :token="imageToken" :color="selectedColorBlindType" @result-fetched="handleResultFetched"/></div>
        <div v-if="!imageToken" class="generate-btn"><InactiveGenerateBtn /></div>
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
