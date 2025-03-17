<template>
    <button
      class="button"
      @click="fetchData">
      <div v-if="loading" class="spinner-container">
        <div class="spinner"></div>
      </div>
      <slot v-else>
        <p>
          Evaluate & Generate
        </p>
      </slot>
    </button>

    <div v-if="error" class="error">{{ error }}</div>
  </template>

<script setup>
  import { ref, watch } from 'vue';
  import axios from 'axios';
  import API_URL from "@/config.js";
  import * as Cronitor from "@cronitorio/cronitor-rum"; // Import API URL

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
    Cronitor.track('generate-result');
    try {
      // Fetch Score
      const scoreResponse = await axios.get(`${API_URL}/get-score?token=${props.token}`);
      const calculatedScore = scoreResponse.data.score;
      console.log("[GenerateBtn]: fetched score = "+calculatedScore);

      // fetch result only if score < 90
      if (calculatedScore < 90) {
        const [imageResponse, protResponse, deutResponse, tritResponse] = await Promise.all([
          axios.get(`${API_URL}/get-result?token=${props.token}&color=${currentColor.value}`, {
            responseType: "blob",
          }),
          axios.get(`${API_URL}/get-simulation?token=${props.token}&color=prot`, {
            responseType: "blob",
          }),
          axios.get(`${API_URL}/get-simulation?token=${props.token}&color=deut`, {
            responseType: "blob",
          }),
          axios.get(`${API_URL}/get-simulation?token=${props.token}&color=trit`, {
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

  .button {
    padding: 20px 30px;
    font-size: 16px;
    color: white;
    background-color: #3498db;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    width: 550px;
    height: 120px;
    display: flex;
    justify-content: center;
    align-items: center;
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

  .spinner {
    border: 10px solid #66addd;
    border-top: 10px solid white;

    border-radius: 50%;
    width: 80px;
    height: 80px;
    animation: spin 2s linear infinite;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
</style>
