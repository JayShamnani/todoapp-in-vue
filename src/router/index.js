import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import About from "@/views/About";
import SignUp from "@/views/signup";
import Login from "@/views/Login";
import Account from "@/views/Account";

const routes = [
  {
    path: "",
    name: "Home",
    component: Home,
  },
  {
    path: "/:account",
    name: "Account",
    component: Account,
    props: {
      account: {
        type: String,
        default: "jayshamnani",
      }
    },
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/signup",
    name: "signup",
    component: SignUp,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
