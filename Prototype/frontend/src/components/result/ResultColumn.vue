<script setup>
import AdjustmentNullState from './AdjustmentNullState.vue'
import AdjustmentLoadingState from './AdjustmentLoadingState.vue'
import AdjustmentInapplicable from './AdjustmentInapplicable.vue'
import AdjustmentApplied from './AdjustmentApplied.vue'
</script>

<template>
    <div class="right-column">
      <!-- TODO: display one of the four states -->
      <AdjustmentNullState />
      <!-- <AdjustmentLoadingState /> -->
      <!-- <AdjustmentApplied /> -->
      <!-- <AdjustmentInapplicable /> -->
    </div>
</template>

<style scoped>
.right-column {
  width: 700px;
}
</style>
