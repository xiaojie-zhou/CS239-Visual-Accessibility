<template>
    <div class="header-container">
      <div class="title">
        <img src="@/components/icons/logo.svg">
        <div class="title-text">Color Vision Diagram Converter</div>
      </div>
      <hr class="line" />
    </div>
  </template>

  <style scoped>
  .header-container {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .header {
    font-size: 70px;
    margin-top: 50px;
    margin-bottom: 50px;
  }

  .line {
    width: 100%;
    height: 2px;
    background-color: #ccc;
    border: none;
    margin-bottom: 30px;
  }

  img {
    height: 100px;
  }

  .title {
    display: flex;
    flex-direction: column;
    font-size: 65px;
    justify-content: baseline;
    align-content: center;
  }
  </style>
<script setup lang="ts">
</script>
