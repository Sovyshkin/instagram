<script setup>
import { ref } from 'vue'

const isHovered = ref(false)
</script>

<template>
    <div 
        class="block"
        @mouseenter="isHovered = true"
        @mouseleave="isHovered = false"
        :class="{ 'hovered': isHovered }"
    >
        <div class="content">
            <h1 :class="{ 'text-pop': isHovered }">Use Shift for safe account transfers</h1>
            <p :class="{ 'slide-up': isHovered }">Shift ensures the safety and privacy of your data. Move your content between accounts anytime without the risk of losing anything.</p>
        </div>
        <div class="wrap-img">
            <img 
                src="@/assets/block_4.png" 
                alt="Secure transfer illustration"
                :class="{ 'scale-up': isHovered }"
            >
        </div>
        <div class="shine-effect" :class="{ 'active': isHovered }"></div>
    </div>
</template>

<style scoped>
.block {
    position: relative;
    width: 100%;
    background-color: #FAC12C;
    border-radius: 30px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0;
    gap: 0;
    height: 600px;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.block.hovered {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(250, 193, 44, 0.3);
}

.content {
    display: flex;
    flex-direction: column;
    gap: 50px;
    padding-left: 40px;
    flex: 1;
    z-index: 2;
}

h1 {
    font-weight: 700;
    font-size: 64px;
    transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    transform-origin: left;
}

h1.text-pop {
    transform: scale(1.02);
    text-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
}

p {
    font-family: "Manrope", sans-serif;
    transition: all 0.4s ease;
    transform: translateY(10px);
    opacity: 0.9;
    max-width: 90%;
}

p.slide-up {
    transform: translateY(0);
    opacity: 1;
}

.wrap-img {
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    width: 40%;
    overflow: hidden;
    transition: all 0.4s ease;
}

img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    transform-origin: center right;
}

img.scale-up {
    transform: scale(1.05);
}

.shine-effect {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(
        135deg,
        rgba(255, 255, 255, 0) 0%,
        rgba(255, 255, 255, 0.2) 50%,
        rgba(255, 255, 255, 0) 100%
    );
    transform: translateX(-100%);
    transition: transform 0.6s ease;
    z-index: 1;
}

.shine-effect.active {
    transform: translateX(100%);
}

/* Планшетная версия */
@media (max-width: 1024px) {
    .block {
        height: auto;
        min-height: 500px;
        flex-direction: column;
    }
    
    .content {
        gap: 24px;
        padding: 24px;
    }
    
    h1 {
        font-size: 44px;
    }
    
    .wrap-img {
        width: 100%;
        max-height: 300px;
    }
    
    img.scale-up {
        transform: scale(1.03);
    }
}

/* Мобильная версия */
@media (max-width: 600px) {
    .block {
        flex-direction: column;
        height: auto;
    }
    
    .block.hovered {
        transform: none;
    }
    
    .wrap-img {
        width: 100%;
        height: 240px;
        order: -1;
    }
    
    .content {
        padding: 16px;
    }
    
    h1 {
        font-size: 28px;
    }
    
    h1.text-pop,
    img.scale-up {
        transform: none;
    }
    
    p {
        max-width: 100%;
        transform: none !important;
    }
    
    .shine-effect {
        display: none;
    }
}
</style>