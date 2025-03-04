<template>
  <div class="upload-box" @dragover.prevent @drop="handleDrop">
    <input type="file" id="fileInput" class="file-input" @change="handleUpload" accept=".png,.jpeg,.jpg" />
    <div>
      <label for="fileInput" class="upload-label">
        <p class="instruction">Drag & drop your image here or <span class="browse-text">browse</span></p>
        <p class="hint">Supported formats: .png, .jpeg, .jpg</p>
        <p class="hint">Maximum size: 500 MB</p>
      </label>
    </div>
    <div class="clear-btn-container">
      <ClearUploadBtn />
    </div>

    <!-- TODO -->
    <img v-if="processedImage" :src="processedImage" alt="Uploaded Image" /> 
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import ClearUploadBtn from "./ClearUploadBtn.vue";

const file = ref(null);
const processedImage = ref(null);

const handleUpload = async (event) => {
  file.value = event.target.files[0]; 
  console.log("Selected file:", file.value);
  if (file.value) await uploadFile();
};

const handleDrop = async (event) => {
  event.preventDefault();
  file.value = event.dataTransfer.files[0]; 
  console.log("Dropped file:", file.value);
  if (file.value) await uploadFile(); 
};
 
const uploadFile = async () => {
  if (!file.value) return;

  const formData = new FormData();
  formData.append("file", file.value);

  try {
    const response = await axios.post("http://127.0.0.1:5000/upload", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    if (!response.data.image) {
      alert("Upload failed. No token received.");
      return;
    }
    alert("File uploaded successfully!");

    const imageToken = response.data.image;
    const imageResponse = await axios.get(`http://127.0.0.1:5000/getImg/${imageToken}`, {
      responseType: "blob",
    });
    processedImage.value = URL.createObjectURL(imageResponse.data);
    alert("File rendered successfully!");
  } catch (error) {
    console.error("Upload error:", error);
    alert("Error.");
  }
};
</script>

<style scoped>
.upload-box {
  position: relative;
  width: 700px;
  height: 400px;
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

.instruction {
  font-size: 38px;
  color: black;
}
.hint {
  font-size: 30px;
}

.clear-btn-container {
  position: absolute;
  bottom: 10px;
  right: 10px;
}
</style>
