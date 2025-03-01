<template>
    <button 
      class="button" 
      @click="handleClick" 
      :disabled="isDisabled" 
      :class="{ 'disabled': isDisabled }">
      <slot><p>Clear</p></slot>
    </button>
  </template>
  
  <script setup>
  import { defineProps } from 'vue';
  
  const props = defineProps({
    isDisabled: {
      type: Boolean,
      default: false, // TODO
    },
  });
  
  const handleClick = () => { // TODO
    console.log("clear btn clicked")
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
  
  .button:disabled {
    background-color: #ccc; /* Gray background when disabled */
    cursor: not-allowed; /* Change cursor to indicate it's not clickable */
  }
  
  .button.disabled {
    opacity: 0.6;
  }
  p {
    font-size: 30px;
  }
  </style>