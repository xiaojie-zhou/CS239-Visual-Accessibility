<template>
  <button 
    class="button" 
    :disabled="true">
    <slot>
      <p>
        Evaluate & Generate
      </p>
    </slot>
  </button>
</template>

<style scoped>
.error {
  color: red;
  font-weight: bold;
}
</style>

<style scoped>
.button {
  padding: 20px 30px;
  font-size: 16px;
  color: white;
  background-color: gray;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

p {
  font-size: 50px;
}
</style>