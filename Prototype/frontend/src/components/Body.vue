<script setup>
  import UserInputColumn from './user-input/UserInputColumn.vue'
  import { ref } from 'vue'
  import Feedback from './result/Feedback.vue'
  import NullState from './result/NullState.vue'
  
  const fetchedScore = ref(null);
  const newImageURL = ref(null);

  const handleResultFetchParent = (result) => {
    fetchedScore.value = result.score;
    newImageURL.value = result.newImageURL;
    console.log("[Body]score received from UserInputCol="+result.score);
  }
</script>

<template>
  <div class="body-container">
    <UserInputColumn class="column" @result-fetched-parent="handleResultFetchParent"/>
    <div class="column separator-container">
      <div class="separator"></div>
    </div>
    <div class="result-container">
      <NullState v-if="!fetchedScore" />
      <Feedback  v-if="fetchedScore" :score="fetchedScore" :imageURL="newImageURL"/>
    </div>
  </div>
</template>

<style scoped>
.body-container {
  display: flex; 
  flex-direction: row;
  justify-content: center; 
  width: 100%;
  height: 100vh;
  margin-top: 30px;
}
.separator {
  height: 60%; /* Restore the height */
  width: 2px;
  background-color: #ccc;
}
.column {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.separator-container {
  margin: 30px;
}
.result-container {
  width: 700px;
}
</style>