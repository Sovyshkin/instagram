<script setup>
import LeftScreen from "@/components/LeftScreen.vue";
import RightScreen from "@/components/RightScreen2.vue";
import AppHeader2 from "@/components/AppHeader2.vue";
</script>
<template>
  <AppHeader2 />
  <div class="wrap">
    <LeftScreen />
    <RightScreen />
  </div>
</template>
<style scoped>
.wrap {
  display: flex;
  justify-content: space-evenly;
  gap: 10px;
  width: 100%;
  background-color: #111328;
  min-height: 100vh;
  padding-top: 90px;
}
</style>
