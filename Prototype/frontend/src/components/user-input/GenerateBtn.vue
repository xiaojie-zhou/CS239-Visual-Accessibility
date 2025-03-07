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
  import { ref, watch } from 'vue';
  import axios from 'axios';

  // Props
  const props = defineProps({
    token:  String,
    color: String
  });

  // watch for color update
  const currentColor = ref(props.color);
  watch(() => props.color, (newColor) => {
    console.log("[GenerateBtn] Color updated:", newColor);
    currentColor.value = newColor;
  });

  // no need to watch for token update
  // because the generateBtn is only active each time a new image is uploaded by the user
  console.log("[GenerateBtn] image token received from UserInputCol:"+props.token);

  // Emits
  const emit = defineEmits(["result-fetched"]);

  // Reactive variables
  const loading = ref(false);
  const error = ref(null);
  const generatedImage = ref(null);
  const simuProtImage = ref(null);
  const simuDeutImage = ref(null);
  const simuTritImage = ref(null);
  
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
      // const calculatedScore = scoreResponse.data.score;
      const calculatedScore = 39;
      console.log("[GenerateBtn]: fetched score = "+calculatedScore);


      // fetch result only if score < 95
      if (calculatedScore < 95) {
        const [imageResponse, protResponse, deutResponse, tritResponse] = await Promise.all([
          axios.get(`http://127.0.0.1:5000/get-result?token=${props.token}&color=${currentColor.value}`, {
            responseType: "blob",
          }),
          axios.get(`http://127.0.0.1:5000/get-simulation?token=${props.token}&color=prot`, {
            responseType: "blob",
          }),
          axios.get(`http://127.0.0.1:5000/get-simulation?token=${props.token}&color=deut`, {
            responseType: "blob",
          }),
          axios.get(`http://127.0.0.1:5000/get-simulation?token=${props.token}&color=trit`, {
            responseType: "blob",
          })
        ]);
        generatedImage.value = URL.createObjectURL(imageResponse.data);
        simuProtImage.value = URL.createObjectURL(protResponse.data);
        simuDeutImage.value = URL.createObjectURL(deutResponse.data);
        simuTritImage.value = URL.createObjectURL(tritResponse.data);
      } else {
        generatedImage.value, simuProtImage.value, simuDeutImage.value, simuTritImage.value = null;
      }
      // Emit score and images
      emit("result-fetched", {
        score: calculatedScore,
        newImageURL: generatedImage.value,
        protImageURL: simuProtImage.value,
        deutImageURL: simuDeutImage.value,
        tritImageURL: simuTritImage.value
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
