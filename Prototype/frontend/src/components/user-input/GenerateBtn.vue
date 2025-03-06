<template>
    <button 
      class="button" 
      @click="fetchData">
      <slot>
        <p>
          Evaluate & Generate
        </p>
      </slot>
    </button>
    <div v-if="loading">Loading...</div>
    <div v-if="error" class="error">{{ error }}</div>
  </template>
  
<script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  
  // Props
  const props = defineProps({
    token:  String
  });

  console.log("[GenerateBtn] image token received from UserInputCol:"+props.token);
  
  // Emits
  const emit = defineEmits(["result-fetched"]);
  
  // Reactive variables
  const loading = ref(false);
  const error = ref(null);
  
  // Function to fetch score and images
  const fetchData = async () => {
    if (!props.token) {
      error.value = "Token is required";
      return;
    }
  
    loading.value = true;
    error.value = null;

  
    try {
      // Fetch Score 
      
      // TODO: fix the issue of infinite wait
      // const scoreResponse = await axios.get(`http://127.0.0.1:5000/get-score?token=${props.token}`);
      // if (!scoreResponse.ok) {
      //   throw new Error("Failed to fetch score");
      // }
      // const calculatedScore = scoreResponse.data.score;
      const calculatedScore = 55;
      console.log("[GenerateBtn]: fetched score = "+calculatedScore);

      // TODO: do not fetch images if score > 95
    
      // TODO: pass in color param
      // // Fetch Images
      // const imageResponse = await axios.get(`http://127.0.0.1:5000/get-result?token=${props.token}`, {
      //   responseType: "blob",
      // });
  
      // Convert images to Object URLs
      // const imageURL = URL.createObjectURL(imageResponse.data);
  
  
      // Emit score and images
      emit("result-fetched", {
        score: calculatedScore,
        newImageURL: '',
      });
    } catch (err) {
      error.value = err.message;
    } finally {
      loading.value = false;
    }
  };
  </script>
  
  <style scoped>
  .error {
    color: red;
    font-weight: bold;
  }
  </style>
  
  
  <style scoped>
  .button {
    padding: 20px 30px;
    font-size: 16px;
    color: white;
    background-color: #3498db;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .button:hover {
    background-color: #2980b9;
  }
  
  .button:focus {
    outline: none;
  }

  p {
    font-size: 50px;
  }
  </style>