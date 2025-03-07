<script setup>
  import Buttons from './Buttons.vue';
  import { defineProps} from 'vue';
  const props = defineProps({
    imageURL: String,
    protImageURL: String,
    deutImageURL: String,
    tritImageURL: String
  });
  console.log("[Downloader] imageURL: "+props.imageURL);
  console.log("[Downloader] protImageURL: "+props.protImageURL);
</script>

<template>
  <div class="feedback-container">
    <div class="new-diagram">
      <img :src="props.imageURL" alt="Uploaded Image" />
      <div class="buttons">
        <Buttons 
          :protImageURL="props.protImageURL"
          :deutImageURL="props.deutImageURL"
          :tritImageURL="props.tritImageURL"
        />
      </div>
    </div>
  </div> 
</template>

<style scoped>
  .feedback-container {
    margin-top: 0px;
    display: flex;
    flex-direction: column;
  }
 .new-diagram {
    width: 700px;
    height: 400px;
    border: 2px dashed #3498db;
    border-radius: 5px;
    background-color: #f9f9f9;
    position: relative;
    display: flex;
    justify-content: center;  
    align-items: center;    
  }
  .buttons {
    position: absolute;
    bottom: 10px;
    right: 10px;
  }
  img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    border-radius: 5px;
  }
</style>