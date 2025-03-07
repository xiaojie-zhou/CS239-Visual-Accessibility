<template>
    <button 
      class="button" 
      @click="downloadImage">
      <img src="@/components/icons/download-black-edited.svg" class="icon" alt="Download Icon" />
    </button>
</template>
  
<script setup>
    const props = defineProps({
        imageURL: String,
    }); 
    const downloadImage = () => {
        const link = document.createElement('a');
        link.href = props.imageURL;
        link.download = 'downloaded-image.jpg'; // Specify the name of the downloaded file
        document.body.appendChild(link); // Append link to the document
        link.click(); // Simulate a click to trigger download
        document.body.removeChild(link); // Remove the link from the document
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
        width: 40px;
        height: 40px;
        filter: invert(29%) sepia(78%) saturate(925%) hue-rotate(180deg) brightness(96%) contrast(90%);
    }

    .button:hover .icon {
        filter: invert(100%) sepia(0%) saturate(0%) brightness(200%) contrast(100%);
    }

</style>