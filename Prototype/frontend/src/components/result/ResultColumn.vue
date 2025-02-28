<script setup>
import AdjustmentNullState from './AdjustmentNullState.vue'
import AdjustmentLoadingState from './AdjustmentLoadingState.vue'
import AdjustmentInapplicable from './AdjustmentInapplicable.vue'
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