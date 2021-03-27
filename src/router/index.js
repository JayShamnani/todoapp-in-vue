import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import About from "@/views/About"
import Login from "@/views/Login"
const routes = [
  {
    path: "",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About
  },
  {
    path: "/login",
    name:"login",
    component:Login
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
