import { createRouter, createWebHistory } from "vue-router";
import AppMain from "@/views/AppMain.vue";
import AppTerms from "@/views/AppTerms.vue";
import AppTransfer from "@/views/AppTransfer.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      component: AppMain,
      name: "main",
    },
    {
      path: "/terms",
      component: AppTerms,
      name: "terms",
    },
    {
      path: "/transfer",
      component: AppTransfer,
      name: "transfer",
    },
  ],
});

export default router;
