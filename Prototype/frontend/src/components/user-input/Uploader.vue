<template>
  <div v-if="!uploadedImage" class="upload-box" @dragover.prevent @drop="handleDrop">
    <input type="file" id="fileInput" class="file-input" @change="handleUpload" accept=".png,.jpeg,.jpg" />
    <div>
      <label for="fileInput" class="upload-label">
        <p class="instruction">Drag & drop your image here or <span class="browse-text">browse</span></p>
        <p class="hint">Supported formats: .png, .jpeg, .jpg</p>
        <p class="hint">Maximum size: 500 MB</p>
      </label>
    </div>
  </div>
  <div v-else class="upload-box">
    <img :src="uploadedImage" alt="Uploaded Image" />
    <div class="clear-btn-container">
      <ClearUploadBtn @clear="clearUpload" :token="imageToken"/>
    </div>
  </div>
</template>

<script setup>
import { ref, defineEmits } from "vue";
import axios from "axios";
import ClearUploadBtn from "./ClearUploadBtn.vue";
import API_URL from "@/config.js";
import * as Cronitor from "@cronitorio/cronitor-rum"; // Import API URL

const file = ref(null);
const uploadedImage = ref(null);
const imageToken = ref(null);
const emit = defineEmits(["image-uploaded"]);

const handleUpload = async (event) => {
  file.value = event.target.files[0];
  if (file.value) await uploadFile();
};

const handleDrop = async (event) => {
  event.preventDefault();
  file.value = event.dataTransfer.files[0];
  if (file.value) await uploadFile();
};

const uploadFile = async () => {
  if (!file.value) return;

  const formData = new FormData();
  formData.append("file", file.value);


  try {
    // post the image
    const response = await axios.post(`${API_URL}/upload`, formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    if (!response.data.image) {
      alert("Upload failed. No token received.");
      return;
    }
    // alert("File uploaded successfully!");
    Cronitor.track('Uploaded-Image');

    // get the preview
    const imageResponse = await axios.get(`${API_URL}/get-preview?token=${response.data.image}`, {
      responseType: "blob",
    });
    uploadedImage.value = URL.createObjectURL(imageResponse.data);

    // emit token after successful upload
    imageToken.value = response.data.image;
    emit("image-uploaded", imageToken.value);

  } catch (error) {
    console.error("Upload error:", error);
    alert("Upload error: "+error.response.data.error);
  }
};

const clearUpload = () => {
  uploadedImage.value = null;
  // emit null token when image is cleared
  imageToken.value = null;
  emit("image-uploaded", imageToken.value);
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
  bottom: 20px;
  right: 20px;
}

img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  border-radius: 5px;
}
</style>
