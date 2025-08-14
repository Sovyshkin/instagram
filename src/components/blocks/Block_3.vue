<script setup>
import ButtonTransfer from '@/components/ui/buttons/ButtonTransfer.vue'
import { ref } from 'vue'

const isHovered = ref(false)
</script>

<template>
    <div 
        class="block"
        @mouseenter="isHovered = true"
        @mouseleave="isHovered = false"
    >
        <div class="content">
            <h1 :class="{ 'hover-effect': isHovered }">Start your transfer now</h1>
            <ButtonTransfer class="transfer-btn" :class="{ 'hover-effect': isHovered }"/>
        </div>
        <div class="wrap-img">
            <img 
                src="@/assets/block_3.png" 
                alt=""
                :class="{ 'hover-effect': isHovered }"
            >
        </div>
    </div>
</template>

<style scoped>
.block {
    position: relative;
    width: 100%;
    background-color: #8920B4;
    border-radius: 30px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-left: 40px;
    gap: 50px;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.block:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(137, 32, 180, 0.3);
}

.content {
    display: flex;
    flex-direction: column;
    gap: 50px;
    z-index: 2;
}

h1 {
    font-weight: 700;
    font-size: 64px;
    transition: all 0.3s ease;
    transform-origin: left;
}

h1.hover-effect {
    transform: translateX(10px);
    text-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
}

.wrap-img {
    position: relative;
    transition: all 0.4s ease;
    z-index: 1;
}

.wrap-img img {
    display: block;
    transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    transform-origin: bottom right;
}

.wrap-img img.hover-effect {
    transform: scale(1.05) rotate(2deg);
}

.transfer-btn {
    transition: all 0.3s ease;
}

.transfer-btn.hover-effect {
    transform: scale(1.05);
    filter: drop-shadow(0 5px 15px rgba(0, 0, 0, 0.2));
}

@media (max-width: 1024px) {
    .block {
        padding-left: 24px;
        gap: 24px;
    }
    h1 {
        font-size: 44px;
    }
    .wrap-img img.hover-effect {
        transform: scale(1.03);
    }
}

@media (max-width: 600px) {
    .block {
        flex-direction: column;
        align-items: flex-start;
        padding-left: 16px;
        gap: 30px;
    }
    .block:hover {
        transform: none;
    }
    h1 {
        font-size: 28px;
    }
    .wrap-img {
        width: 100%;
        text-align: center;
    }
    .wrap-img img {
        max-width: 100%;
        height: auto;
    }
    h1.hover-effect,
    .transfer-btn.hover-effect {
        transform: none;
    }
}
</style>