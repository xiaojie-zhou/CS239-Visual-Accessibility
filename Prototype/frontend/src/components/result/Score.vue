<template>
  <div class="score-rating-container">
    <div class="score-container">
      <div class="circle-container">
        <svg width="120" height="120" viewBox="0 0 120 120">
          <circle cx="60" cy="60" r="50" stroke="#e6e6e6" stroke-width="10" fill="none" />
          <circle
              :stroke-dasharray="circumference"
              :stroke-dashoffset="strokeOffset"
              cx="60"
              cy="60"
              r="50"
              :stroke="color"
              stroke-width="10"
              fill="none"
              transform="rotate(-90 60 60)"
          />
        </svg>
        <div class="score-number">{{ displayScore }}</div>
      </div>
    </div>
    <div class="rating-container">
      <div class="rating">{{rating}}</div>
      <div class="text">{{ratingString}}</div>
    </div>
  </div>
</template>

<script setup>
  import { defineProps, computed } from 'vue';
  const props = defineProps({
    score: Number
  });
  const circumference = computed(() => 2 * Math.PI * 50); // r = 50
  const minScore = 0;
  const maxScore = 100;
  const displayScore = computed(() => { // display 100 for scores>= 90
      return props.score >= 90 ? 100 :props.score;
  });
  const strokeOffset = computed(() => {
      return circumference.value - ((displayScore - minScore) / (maxScore - minScore)) * circumference.value;
  });
  const color = computed(() => {
    if (props.score >= 90) {
      return '#1e8449';
    } else if (props.score >= 80) {
      return'#2ecc71';
    } else if (props.score >= 60) {
      return '#2196f3';
    } else if (props.score >= 40) {
      return '#e67e22';
    } else {
      return '#e74c3c';
    }
  });
  const rating = computed(() => {
    if (props.score >= 90) {
      return "Excellent";
    } else if (props.score >= 80) {
      return "Good";
    } else if (props.score >= 60) {
      return "Moderate";
    } else if (props.score >= 40) {
      return "Poor";
    } else {
      return "Very Poor";
    }

  });
  const ratingString = computed(() => {
    if (props.score >= 90) {
      return "No modification required. This graph is accessible!";
    } else if (props.score >= 80) {
      return "The original graph is already highly accessible, and here is the new version with minor improvements.";
    } else if (props.score >= 60) {
      return "The original graph is generally accessible, and here is the new version with minor improvements.";
    } else if (props.score >= 40) {
      return "Some users may struggle interpreting the original graph. Here's the enhanced version.";
    } else {
      return "Most users with color vision deficiency may find it hard to interpret the original graph. Here's the enhanced version with significant improvements.";
    }
  });
</script>

<style scoped>
.score-rating-container {
  margin-top: 30px;
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 700px;
}

.score-container {
  text-align: center;
}

.circle-container {
  position: relative;
  display: inline-block;
}

.rating-container {
  margin-left: 20px;
  display: flex;
  flex-direction: column;
}

.score-number {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 36px;
  font-weight: bold;
}

.rating {
  font-size: 40px;
  font-weight: 600;
}

.text {
  font-size: 30px;
}
</style>
