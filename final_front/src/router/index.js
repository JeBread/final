import Vue from "vue";
import VueRouter from "vue-router";
// import store from "@/store/"; 네이게이션 가드 킬 때 주석 해제하기

import LogInView from "@/views/LogInView.vue";
import SignUpView from "@/views/SignUpView.vue";
import MovieView from "@/views/MovieView.vue";

import QuizView from "@/views/QuizView.vue";
import OstView from "@/views/OstView.vue";
import CommunityView from "@/views/CommunityView.vue";
// import DetailView from "@/views/DetailView.vue";
// import RecommendedView from "@/views/RecommendedView.vue";
import NotFound404 from "@/views/NotFound404.vue";

Vue.use(VueRouter);

const routes = [
  // 홈 화면은 LoginView
  {
    path: "/",
    name: "LogInView",
    component: LogInView,
  },
  {
    path: "/signup",
    name: "SignUpView",
    component: SignUpView,
  },

  // 로그인 이후 페이지는 MovieView
  // Movie 관련 router
  {
    path: "/movie",
    name: "MovieView",
    component: MovieView,
  },
  {
    path: "/detail/:id",
    name: "DetailView",
    // component: DetailView,
    component: () => import("@/views/DetailView.vue"),
  },

  // 커뮤니티 관련 router
  {
    path: "/community",
    name: "CommunityView",
    component: CommunityView,
    // component: () => import("@/views/CommunityView.vue"),
  },
  {
    path: "/create",
    name: "CreateView",
    component: () => import("@/views/CreateView.vue"),
  },
  {
    path: "/:articleId",
    name: "ArticleDetailView",
    component: () => import("@/views/ArticleDetailView.vue"),
  },
  // 퀴즈 관련 router
  {
    path: "/quiz",
    name: "QuizView",
    component: QuizView,
  },
  // 추천 영화 관련 router
  {
    path: "/recommended",
    name: "RecommendedView",
    // component: RecommendedView,
    component: () => import("@/views/RecommendedView.vue"),
  },
  {
    path: "/ost",
    name: "OstView",
    component: OstView,
  },

  // 프로필 관련 router
  // {
  //   path: "/Profile/:userName",
  //   name: "ProfileView",
  //   component: () => import("@/views/ProfileView.vue"),
  // },
  // 404 페이지
  {
    path: "/404",
    name: "NotFoundView",
    component: NotFound404,
  },
  // 이상한 경로로 들어왔을 때 404 페이지로 이동
  {
    path: "*",
    redirect: "/404",
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

// // Navigation Guard 설정
// router.beforeEach((to, from, next) => {
//   // 로그인 여부 확인
//   const { isLoggedIn } = store.getters;

//   // Auth가 필요한 route의 name
//   const authPages = [
//     "MovieView",
//     "CommunityView",
//     "DetailView",
//     "ProfileView",
//     "QuizView",
//     "RecommendedView",
//   ];

//   // 로그인이 되어있지 않을 때만 가능한 route의 name
//   const notAuthPages = ["LoginView", "SignUpView"];

//   // 현재 이동하고자 하는 페이지가 로그인이 필요한지 확인
//   const isAuthRequired = authPages.includes(to.name);

//   const isNotAuthRequired = notAuthPages.includes(to.name);

//   // 로그인이 필요한 페이지인데 로그인이 되어있지 않다면 로그인 페이지로 이동
//   if (isAuthRequired && !isLoggedIn) {
//     next({ name: "LogInView" });
//   } else {
//     // 로그인이 되어 있다면 MovieView 이동
//     next({ name: "MovieView" });
//   }

//   // 로그인이 되어있는데 로그인, 회원가입 페이지로 이동하려고 한다면 MovieView로 이동
//   if (isNotAuthRequired && isLoggedIn) {
//     next({ name: "MovieView" });
//   } else {
//     next();
//   }
// });

// const originalPush = VueRouter.prototype.push;
// VueRouter.prototype.push = function push(location) {
//   return originalPush.call(this, location).catch((err) => {
//     if (err.name !== "NavigationDuplicated") throw err;
//   });
// };

export default router;
