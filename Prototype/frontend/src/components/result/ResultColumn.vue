<script setup>
import NoAdjustment from './NoAdjustment.vue'
import AdjustmentApplied from './AdjustmentApplied.vue'
</script>

<template>
    <div class="right-column">
      <!-- TODO -->
      <AdjustmentApplied />
    </div>
</template>

<style scoped>
.right-column {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>