<template>
    <button
      class="button"
      @click="handleClick">
      <img src="@/components/icons/trash-black.svg" class="icon" alt="Download Icon" />
    </button>
  </template>

<script setup>
import axios from "axios";
import API_URL from "@/config.js"; // Import API URL
    token:  String
  });
  const emit = defineEmits(["clear"]);
  const handleClick = async () => {
    try {
      await axios.post(`${API_URL}/clear?token=${props.token}`);
      console.log("Files cleared successfully.");
      emit("clear"); // Notify parent to clear UI
    } catch (error) {
      console.error("Error clearing files:", error);
    }
  };
</script>

  <style scoped>
   .button {
    width: 80px;
    height: 80px;
    font-size: 16px;
    border: 4px solid #3498db;
    background-color: white;
    border-radius: 50%;
    cursor: pointer;
    transition: background-color 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0;
    }
    .button:hover {
      background-color: #3498db;
    }
    .button:focus {
      outline: none;
    }
    .icon {
      width: 50px;
      height: 50px;
      filter: invert(29%) sepia(78%) saturate(925%) hue-rotate(180deg) brightness(96%) contrast(90%);
    }
    .button:hover .icon {
      filter: invert(100%) sepia(0%) saturate(0%) brightness(200%) contrast(100%);
    }
  </style>
