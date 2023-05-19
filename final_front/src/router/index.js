import Vue from "vue";
import VueRouter from "vue-router";
import SignUpView from "@/views/SignUpView.vue";
import LogInView from "@/views/LogInView.vue";
// import MovieView from "@/views/MovieView.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "LogInView",
    component: LogInView,
  },
  {
    path: "/movie",
    name: "MovieView",
    // component: MovieView,
    component: () => import("@/views/MovieView.vue"),
  },
  {
    path: "/signup",
    name: "SignUpView",
    component: SignUpView,
  },
  {
    path: "/Profile",
    name: "ProfileView",
    component: () => import("@/views/ProfileView.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
