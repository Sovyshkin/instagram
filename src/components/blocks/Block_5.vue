<script setup>
import { ref } from 'vue'

const formData = ref({
  name: '',
  email: '',
  question: ''
})

const isHovered = ref(false)
const isFocused = ref(false)
</script>

<template>
    <div class="block">
        <h1 class="title" :class="{ 'title-hover': isHovered }">Need help? Get in touch!</h1>
        <div 
            class="content"
            @mouseenter="isHovered = true"
            @mouseleave="isHovered = false"
        >
            <form class="form">
                <div class="input-group">
                    <input 
                        type="text" 
                        placeholder="Name"
                        v-model="formData.name"
                        @focus="isFocused = true"
                        @blur="isFocused = false"
                        :class="{ 'input-focus': isFocused }"
                    >
                </div>
                <div class="input-group">
                    <input 
                        type="email" 
                        placeholder="Email"
                        v-model="formData.email"
                        @focus="isFocused = true"
                        @blur="isFocused = false"
                        :class="{ 'input-focus': isFocused }"
                    >
                </div>
                <div class="input-group">
                    <textarea 
                        placeholder="Question"
                        v-model="formData.question"
                        @focus="isFocused = true"
                        @blur="isFocused = false"
                        :class="{ 'input-focus': isFocused }"
                    ></textarea>
                </div>
                <button class="btn" :class="{ 'btn-hover': isHovered }">
                    <span>Send request</span>
                </button>
            </form>
            <img 
                src="@/assets/block_5.png" 
                alt="Contact us illustration"
                class="contact-img"
                :class="{ 'img-hover': isHovered }"
            >
        </div>
    </div>
</template>

<style scoped>
.block {
    width: 100%;
    border-radius: 20px;
    background-color: #FF00DD;
    padding: 100px 40px;
    display: flex;
    flex-direction: column;
    gap: 25px;
    transition: all 0.3s ease;
}

.block:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(255, 0, 221, 0.3);
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: 600;
    transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.title-hover {
    transform: scale(1.02);
    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.content {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: stretch;
    gap: 25px;
}

.form {
    width: 45%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 25px;
}

.input-group {
    position: relative;
    transition: all 0.3s ease;
}

.input-group:hover {
    transform: translateX(5px);
}

input, textarea {
    font-family: "Manrope", sans-serif;
    width: 100%;
    background-color: #FFFFFE;
    border-radius: 30px;
    border: 2px solid transparent;
    outline: none;
    padding: 15px 30px;
    color: black;
    transition: all 0.3s ease;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
}

.input-focus {
    border-color: #FFC000;
    box-shadow: 0 5px 15px rgba(255, 192, 0, 0.2);
}

textarea {
    min-height: 141px;
    resize: vertical;
}

input::placeholder, textarea::placeholder {
    color: #848484;
    transition: all 0.2s ease;
}

input:focus::placeholder, textarea:focus::placeholder {
    opacity: 0.5;
}

.btn {
    position: relative;
    background: linear-gradient(90deg, #951AE8 0%, #FD01BC 50%, #FFC000 100%);
    padding: 15px 30px;
    border-radius: 100px;
    font-family: "Manrope", sans-serif;
    border: none;
    cursor: pointer;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    z-index: 1;
}

.btn span {
    position: relative;
    z-index: 2;
    transition: all 0.3s ease;
}

.btn-hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.btn-hover span {
    color: white;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

.btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, #FFC000 0%, #FD01BC 50%, #951AE8 100%);
    opacity: 0;
    transition: all 0.4s ease;
    z-index: 1;
}

.btn-hover::before {
    opacity: 1;
}

.contact-img {
    border-radius: 20px;
    width: 55%;
    max-height: 413px;
    object-fit: cover;
    transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
    transform-origin: center;
}

.img-hover {
    transform: scale(1.03) rotate(1deg);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

/* Планшетная версия */
@media (max-width: 1024px) {
    .block {
        padding: 60px 24px;
    }
    
    .form {
        width: 50%;
    }
    
    .contact-img {
        width: 50%;
    }
    
    .img-hover {
        transform: scale(1.02);
    }
    
    .btn-hover {
        transform: translateY(-2px);
    }
}

/* Мобильная версия */
@media (max-width: 600px) {
    .content {
        flex-direction: column;
    }
    
    .form, .contact-img {
        width: 100%;
    }
    
    .block {
        padding: 40px 16px;
    }
    
    .title {
        font-size: 32px;
    }
    
    .title-hover,
    .img-hover,
    .btn-hover {
        transform: none !important;
    }
    
    .input-group:hover {
        transform: none;
    }
}
</style>