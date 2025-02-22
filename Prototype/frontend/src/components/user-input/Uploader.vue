<template>
    <div class="upload-box" @dragover.prevent @drop="handleDrop">
      <input type="file" id="fileInput" class="file-input" @change="handleUpload" />
      <label for="fileInput" class="upload-label">
        <p>Drag & drop your image here or <span class="browse-text">browse</span></p>
        <p>Supported formats: .png, .jpeg, .jpg</p>
        <p>Maximum size: 500 MB</p>
      </label>
    </div>
    <div>

    </div>
  </template>
  
  <script setup> 
  // TODO
  const handleUpload = (event) => {
    const files = event.target.files;
    console.log("Selected files:", files);
  };
  const handleDrop = (event) => {
    const files = event.dataTransfer.files;
    console.log("Dropped files:", files);
  };
  </script>
  
  <style scoped>
  .upload-box {
    width: 300px;
    height: 150px;
    border: 2px dashed #3498db;
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    cursor: pointer;
    color: #555;
    font-size: 16px;
    background-color: #f9f9f9;
    transition: background-color 0.2s ease-in-out;
  }
  
  .upload-box:hover {
    background-color: #f1f1f1;
  }
  
  .file-input {
    display: none;
  }
  
  .upload-label {
    cursor: pointer;
  }
  
  .browse-text {
    color: #3498db;
    font-weight: bold;
    text-decoration: underline;
  }
  </style>
  