<script setup>
  import Downloader from './Downloader.vue'
  import Score from './Score.vue'
  import { defineProps} from 'vue';
  const props = defineProps({
    score: Number,
    imageURL: String
  });
  console.log("[Feedback]: score="+props.score)
</script>
<template>
    <Downloader v-if="props.imageURL" :url="props.imageURL"/> 
    <Score :score="props.score"/>
</template>