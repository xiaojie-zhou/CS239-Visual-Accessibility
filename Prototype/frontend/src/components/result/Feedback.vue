<script setup>
  import Downloader from './Downloader.vue'
  import Score from './Score.vue'
</script>
<template>
  <!-- TODO: do not display downloader if socre >= 95 -->
  <Downloader /> 
  <Score score="95"/>

</template>