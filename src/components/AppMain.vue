<script>
import LeftScreen from "./LeftScreen.vue";
import RightScreen from "./RightScreen2.vue";
export default {
  name: "AppMain",
  components: {
    LeftScreen,
    RightScreen,
  },
};
</script>
<template>
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
}
</style>
