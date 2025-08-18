<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goTransfer = () => {
    try {
        router.push({ name: "transfer" })
    } catch (err) {
        console.log(err);
        
    }
}
</script>
<template>
    <header>
        <div class="wrap-logo">
            <img src="@/assets/instagram.png" alt="">
            <span>IGshift</span>
        </div>
        <button class="btn" @click="goTransfer">Start transfer</button>
    </header>
</template>
<style scoped>
header {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    z-index: 3;
}

.wrap-logo {
    display: flex;
    align-items: center;
    gap: 10px;
}

.wrap-logo span {
    font-weight: 600;
    font-size: 24px;
    color: #fff;
}

.wrap-logo img {
    height: 40px;
    width: 40px;
}

.btn {
    background: linear-gradient(90deg, #951AE8 0%, #FD01BC 50%, #FFC000 100%);
    padding: 15px 30px;
    border-radius: 100px;
    font-family: "Manrope", sans-serif;
}
@media (max-width: 1024px) {
  .wrap-logo span {
    font-size: 20px;
  }
  .btn {
    padding: 12px 22px;
  }
}
@media (max-width: 600px) {
  header {
    gap: 12px;
  }
  .wrap-logo img {
    height: 32px;
    width: 32px;
  }
  .wrap-logo span {
    font-size: 18px;
  }
  .btn {
    padding: 10px 18px;
  }
}
</style>