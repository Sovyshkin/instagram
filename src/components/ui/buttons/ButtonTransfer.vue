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
    <button class="btn" @click="goTransfer()">
        <span>
            Start transfer
        </span>
        <img src="@/assets/btn-block.svg" alt="">
    </button>
</template>
<style scoped>
.btn {
    width: fit-content;
    border: 1px solid #fff;
    border-radius: 100px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 30px;
    position: relative;
    z-index: 10;
}

.btn span {
    padding: 10px 30px;
    font-family: "Manrope", sans-serif;
}
@media (max-width: 600px) {
  .btn {
    gap: 16px;
  }
  .btn span {
    padding: 8px 20px;
  }
}
</style>