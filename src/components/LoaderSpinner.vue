<template>
  <div class="wrapper-load">
    <swapping-squares-spinner
      :animation-duration="700"
      :size="50"
      color="#ff5f21"
    />
  </div>
</template>

<script>
import { SwappingSquaresSpinner } from "epic-spinners";
export default {
  name: "LoadingSpinner",
  components: {
    SwappingSquaresSpinner,
  },
};
</script>

<style scoped>
.wrapper-load {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
