<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const goRoute = (name) => {
    try {
        router.push({ name })
    } catch (err) {
        console.log(err);
        
    }
}
</script>
<template>
  <footer>
    <div class="logo" @click="goRoute('main')">
      <img src="@/assets/instagram.png" alt="" />
      <span>IGShift</span>
    </div>
    <span class="terms" @click="goRoute('terms')"
      >Terms and conditions</span
    >
  </footer>
</template>
<style scoped>
footer {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  background-color: #171717;
  padding: 30px;
  border-radius: 20px;
}

span {
  cursor: pointer;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.logo span {
  font-weight: 600;
  font-size: 24px;
  color: #fff;
}

.logo img {
  height: 40px;
  width: 40px;
}

.terms {
  font-weight: 400;
  font-size: 16px;
}
@media (max-width: 600px) {
  footer {
    padding: 20px;
  }
  .logo span {
    font-size: 18px;
  }
  .terms {
    font-size: 14px;
  }
}
</style>
