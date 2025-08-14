<script setup>
import { ref } from "vue";

const activeStep = ref(null);
const getStepName = (step) => {
  const names = {
    1: "Log in",
    2: "Select data",
    3: "Review & confirm",
    4: "Done",
  };
  return names[step] || "";
};

const getStepDescription = (step) => {
  const descriptions = {
    1: "Sign in to both your old and new Instagram accounts to confirm access.",
    2: "Choose what you want to transfer: photos, videos, followers, messages, and more.",
    3: "Check the selected data and confirm the transfer.",
    4: "We'll complete the transfer within 24 hours. You'll get a notification when it's finished.",
  };
  return descriptions[step] || "";
};
</script>

<template>
  <div class="block">
    <h1 class="title">How does data transfer happen?</h1>
    <ul class="steps-list">
      <li
        class="step-item"
        v-for="n in 4"
        :key="n"
        @mouseenter="activeStep = n"
        @mouseleave="activeStep = null"
        :class="{ active: activeStep === n }"
      >
        <h2 class="item-count">{{ n }}</h2>
        <div class="item-content">
          <h2 class="item-name">{{ getStepName(n) }}</h2>
          <p class="item-description">{{ getStepDescription(n) }}</p>
        </div>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.block {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.title {
  font-weight: 600;
  font-size: 40px;
  color: black;
  transition: all 0.3s ease;
  transform-origin: left;
}

.title:hover {
  transform: translateX(10px);
}

.steps-list {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.step-item {
  width: 100%;
  background-color: #f0fcff;
  display: flex;
  align-items: center;
  border-radius: 20px;
  padding-left: 100px;
  overflow: hidden;
  height: 180px;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  cursor: default;
  position: relative;
  cursor: pointer;
}

.step-item::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  width: 8px;
  height: 100%;
  background: linear-gradient(to bottom, #951AE8 0%, #FD01BC 50%, #FFC000 100%);
  transform: scaleY(0);
  transform-origin: top;
  transition: transform 0.4s ease;
}

.step-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.step-item.active::before {
  transform: scaleY(1);
}

.step-item:hover .item-count {
  color: #FD01BC;
}

.item-count {
  color: black;
  font-size: 190px;
  font-weight: 600;
  font-family: "Manrope", sans-serif;
  width: 15%;
  transform: translateY(15%);
  transition: all 0.3s ease;
}

.item-content {
  width: 75%;
  padding-right: 40px;
}

.item-name {
  color: black;
  font-size: 40px;
  font-weight: 600;
  margin-bottom: 10px;
  transition: all 0.3s ease;
}

.step-item:hover .item-name {
  color: #FD01BC;
}

.item-description {
  color: black;
  line-height: 1.5;
  transition: all 0.3s ease;
}

.step-item:hover .item-description {
  transform: translateX(5px);
}

/* Планшетная версия */
@media (max-width: 1024px) {
  .block {
    gap: 30px;
  }

  .title {
    font-size: 32px;
  }

  .step-item {
    height: 160px;
    padding-left: 60px;
  }

  .item-count {
    font-size: 120px;
    width: 20%;
  }

  .item-content {
    width: 70%;
  }

  .item-name {
    font-size: 28px;
  }
}

/* Мобильная версия */
@media (max-width: 600px) {
  .block {
    gap: 20px;
  }

  .title {
    font-size: 24px;
    text-align: center;
  }

  .title:hover {
    transform: none;
  }

  .step-item {
    flex-direction: column;
    align-items: flex-start;
    height: auto;
    padding: 25px;
    gap: 10px;
  }

  .step-item::before {
    width: 100%;
    height: 4px;
    transform: scaleX(0);
    transform-origin: left;
  }

  .step-item.active::before {
    transform: scaleX(1);
  }

  .item-count {
    font-size: 64px;
    width: auto;
    transform: none;
    order: -1;
  }

  .item-content {
    width: 100%;
    padding-right: 0;
  }

  .item-name {
    font-size: 22px;
  }

  .step-item:hover {
    transform: none;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  }
}
</style>
