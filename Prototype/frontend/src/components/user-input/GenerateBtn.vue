<template>
    <button 
      class="button" 
      @click="handleClick" 
      :disabled="isDisabled" 
      :class="{ 'disabled': isDisabled }">
      <slot>
        <p>
          Evaluate & Generate
        </p>
      </slot>
    </button>
  </template>
  
  <script setup>
  const handleClick = () => {
    console.log("Generate btn clicked")
  };
  </script>
  
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