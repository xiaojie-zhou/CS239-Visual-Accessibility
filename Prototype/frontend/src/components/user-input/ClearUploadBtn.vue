<template>
    <button 
      class="button" 
      @click="handleClick" >
      <slot><p>Clear</p></slot>
    </button>
  </template>
  
  <script setup>
  
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
  
  p {
    font-size: 30px;
  }
  </style>