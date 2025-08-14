<script setup>
import AppHeader from '../AppHeader.vue'
import ButtonTransfer from '@/components/ui/buttons/ButtonTransfer.vue'
import { ref } from 'vue'

const isHovered = ref(false)
</script>

<template>
    <div class="block">
        <AppHeader class="header-content"/>
        
        <img 
            class="circle circle-1" 
            src="../../assets/circle.png" 
            alt=""
            :style="{ transform: isHovered ? 'scale(1.05) rotate(5deg)' : 'scale(1)' }"
        >
        <img 
            class="circle circle-2" 
            src="../../assets/circle.png" 
            alt=""
            :style="{ transform: isHovered ? 'scale(1.05) rotate(-5deg)' : 'scale(1)' }"
        >
        
        <h1 
            @mouseenter="isHovered = true"
            @mouseleave="isHovered = false"
        >Transferring data between Instagram accounts</h1>
        
        <ButtonTransfer 
            class="transfer-btn"
            @mouseenter="isHovered = true"
            @mouseleave="isHovered = false"
        />
    </div>
</template>

<style scoped>
.block {
    position: relative;
    width: 100%;
    background-color: #171717;
    border-radius: 30px;
    overflow: hidden;
    padding: 30px 40px 130px 40px;
    display: flex;
    flex-direction: column;
    gap: 50px;
    transition: all 0.3s ease;
}

.block:hover {
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.header-content {
    position: relative;
    z-index: 10;
}

.circle {
    filter: blur(5px);
    opacity: 0.9;
    z-index: 1;
    transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    will-change: transform;
}

.circle-1 {
    position: absolute;
    width: 453px;
    height: 437px;
    top: -200px;
    left: -175px;
}

.circle-2 {
    width: 557px;
    height: 537px;
    position: absolute;
    bottom: -200px;
    right: -175px;
}

h1 {
    font-weight: 700;
    font-size: 64px;
    position: relative;
    z-index: 10;
    transition: all 0.3s ease;
    cursor: default;
}

h1:hover {
    text-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
    transform: translateY(-2px);
}

.transfer-btn {
    transition: all 0.3s ease;
    transform-origin: center;
}

.transfer-btn:hover {
    transform: scale(1.05);
}

@media (max-width: 1024px) {
    .block {
        padding: 24px 24px 80px 24px;
        gap: 30px;
    }
    h1 {
        font-size: 44px;
    }
    .circle-1 {
        width: 360px;
        height: 340px;
    }
    .circle-2 {
        width: 420px;
        height: 400px;
    }
}

@media (max-width: 600px) {
    .block {
        padding: 16px 16px 56px 16px;
        gap: 24px;
    }
    h1 {
        font-size: 28px;
    }
    .transfer-btn:hover {
        transform: none;
    }
}
</style>