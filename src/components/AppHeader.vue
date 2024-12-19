<script>
export default {
  name: "AppHeader",
  data() {
    return {};
  },
  methods: {},
  mounted() {},
};
</script>
<template>
  <header>
    <span class="name" @click="$router.push({ name: 'main' })">IGShift</span>
    <span class="terms" @click="$router.push({ name: 'terms' })"
      >Terms and conditions</span
    >
  </header>
</template>
<style scoped>
header {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  background-color: #1f1f1f;
  padding: 20px 30px;
  border-radius: 20px;
}

span {
  cursor: pointer;
}

.name {
  font-weight: 700;
  font-size: 16px;
  line-height: 20px;
}

.terms {
  font-weight: 400;
  font-size: 12px;
  line-height: 15px;
}
</style>
