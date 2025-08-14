<script setup>
import Block_1 from "@/components/blocks/Block_1.vue";
import Block_2 from "@/components/blocks/Block_2.vue";
import Block_3 from "@/components/blocks/Block_3.vue";
import Block_4 from "@/components/blocks/Block_4.vue";
import Block_5 from "@/components/blocks/Block_5.vue";
import AppFooter from '@/components/AppFooter.vue'
</script>
<template>
  <div class="wrap">
    <Block_1 />
    <Block_2 />
    <block_3 />
    <block_4 />
    <block_5 />
    <AppFooter/>
  </div>
</template>
<style scoped>
.wrap {
  padding: 50px;
  display: flex;
  flex-direction: column;
  gap: 150px;
}
@media (max-width: 1024px) {
  .wrap {
    padding: 24px;
    gap: 80px;
  }
}
@media (max-width: 600px) {
  .wrap {
    padding: 16px;
    gap: 40px;
  }
}
</style>
