<script setup>
  import Downloader from './Downloader.vue'
  import Score from './Score.vue'
  import { defineProps} from 'vue';
  const props = defineProps({
    score: Number,
    imageURL: String,
    protImageURL: String,
    deutImageURL: String,
    tritImageURL: String
  });
  console.log("[Feedback]: score="+props.score)
</script>
<template>
    <Downloader 
      v-if="props.imageURL" 
      :imageURL="props.imageURL" 
      :protImageURL="protImageURL"
      :deutImageURL="deutImageURL"
      :tritImageURL="tritImageURL"
    /> 
    <Score :score="props.score"/>
</template>