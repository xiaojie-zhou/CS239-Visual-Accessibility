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
  const handleClick = async () => {
    console.log("Generate btn clicked")
    try {
      const response = await axios.get("http://127.0.0.1:5000/get-result?token=${imageToken}", formData, {
        responseType: "blob",
      });
    uploadedImage.value = URL.createObjectURL(imageResponse.data);
  } catch (error) {
    console.error("Fetch result error:", error);
  }


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