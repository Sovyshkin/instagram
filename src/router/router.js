import { createRouter, createWebHistory } from "vue-router";
import AppMain from "../components/AppMain.vue";
import AppTerms from "../components/AppTerms.vue";

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
  ],
});

export default router;
