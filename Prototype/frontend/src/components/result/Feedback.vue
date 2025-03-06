<script setup>
  import Downloader from './Downloader.vue'
  import Score from './Score.vue'
  import { defineProps} from 'vue';
  const props = defineProps({
    score: {
      type: Number,
      require: true,
    }
  });
  console.log("[Feedback]: score="+props.score)
</script>
<template>
  <!-- TODO: do not display downloader if score >= 95 -->
    <Downloader /> 
    <Score :score="props.score"/>
</template>