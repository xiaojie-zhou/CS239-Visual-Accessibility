<script setup>
import Header from '@/components/Header.vue'
import Body from '@/components/Body.vue'
import * as Cronitor from "@cronitorio/cronitor-rum";

Cronitor.track("Pageview");
this.$gtag.event()
</script>

<template>
  <div>
    <Header />
    <Body />
  </div>

</template>

<style scoped>
</style>
