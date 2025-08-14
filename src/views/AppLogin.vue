<script setup>
import LeftLogin from "@/components/LeftLogin.vue";
import RightLogin from "@/components/RightLogin2.vue";
</script>
<template>
  <div class="wrap">
    <LeftLogin />
    <RightLogin />
  </div>
</template>
<style scoped>
.wrap {
  display: flex;
  justify-content: space-evenly;
  gap: 10px;
  width: 100%;
}
</style>
