<template>
    <button 
      class="button" 
      @click="handleClick" >
      <slot><p>Clear</p></slot>
    </button>
  </template>
  
<script setup>
import axios from "axios"; 
  const emit = defineEmits(["clear"]);
  const handleClick = async () => {
    try {
      await axios.post("http://127.0.0.1:5000/clear");
      console.log("Files cleared successfully.");
      emit("clear"); // Notify parent to clear UI
    } catch (error) {
      console.error("Error clearing files:", error);
    }
  };
</script>
  
  <style scoped>
  .button {
    width: 150px;
    height: 70px;
    padding: 20px;
    font-size: 16px;
    color: white;
    background-color: #3498db;
    border: none;
    border-radius: 5px;
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
    font-size: 30px;
  }
  </style>