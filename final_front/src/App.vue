<template>
  <div
    class="first leading-normal tracking-normal text-indigo-400 m-6 background"
    id="app"
  >
    <div class="h-full">
      <!-- Nav Bar -->
      <nav class="w-full container mx-auto">
        <div class="w-full flex items-center justify-between">
          <!-- <a
            class="flex items-center text-indigo-400 no-underline hover:no-underline font-bold text-2xl lg:text-4xl mt-5"
            href=""
            @click="toHome"
          >
            Rain<span
              class="bg-clip-text text-transparent bg-gradient-to-r from-green-400 via-pink-500 to-purple-500"
              >blur</span
            >
          </a> -->
          <router-link
            v-if="token"
            :to="{ name: 'MovieView' }"
            class="flex items-center text-indigo-400 no-underline hover:no-underline font-bold text-2xl lg:text-4xl mt-5"
            >Rain<span
              class="bg-clip-text text-transparent bg-gradient-to-r from-green-400 via-pink-500 to-purple-500"
              >blur</span
            ></router-link
          >
          <router-link
            v-if="!token"
            :to="{ name: 'LogInView' }"
            class="flex items-center text-indigo-400 no-underline hover:no-underline font-bold text-2xl lg:text-4xl mt-5"
            >Rain<span
              class="bg-clip-text text-transparent bg-gradient-to-r from-green-400 via-pink-500 to-purple-500"
              >blur</span
            ></router-link
          >
          <!-- <img src="./assets/logo.png" alt="" id="logo" @click="toHome" /> -->
          <!-- nav bar right section-->
          <div class="flex w-1/2 justify-end content-center mt-5 font-semibold">
            <router-link
              v-if="token"
              :to="{ name: 'MovieView' }"
              class="inline-block text-blue-300 no-underline hover:text-pink-500 hover:text-underline text-center h-10 p-2 md:h-auto md:p-4 transform hover:scale-125 duration-300 ease-in-out fill-current h-6"
              >Movie</router-link
            >
            <router-link
              v-if="token"
              :to="{ name: 'QuizView' }"
              class="inline-block text-blue-300 no-underline hover:text-pink-500 hover:text-underline text-center h-10 p-2 md:h-auto md:p-4 transform hover:scale-125 duration-300 ease-in-out fill-current h-6"
              >Quiz</router-link
            >

            <router-link
              v-if="token"
              :to="{ name: 'OstView' }"
              class="inline-block text-blue-300 no-underline hover:text-pink-500 hover:text-underline text-center h-10 p-2 md:h-auto md:p-4 transform hover:scale-125 duration-300 ease-in-out fill-current h-6"
              >Ost</router-link
            >
            <router-link
              v-if="token"
              :to="{ name: 'RecommendedView' }"
              class="inline-block text-blue-300 no-underline hover:text-pink-500 hover:text-underline text-center h-10 p-2 md:h-auto md:p-4 transform hover:scale-125 duration-300 ease-in-out fill-current h-6"
              >Recommend</router-link
            >
            <router-link
              v-if="token"
              :to="{ name: 'CommunityView' }"
              class="inline-block text-blue-300 no-underline hover:text-pink-500 hover:text-underline text-center h-10 p-2 md:h-auto md:p-4 transform hover:scale-125 duration-300 ease-in-out fill-current h-6"
              >Community</router-link
            >
            <router-link
              v-if="!token"
              :to="{ name: 'SignUpView' }"
              class="inline-block text-blue-300 no-underline hover:text-pink-500 hover:text-underline text-center h-10 p-2 md:h-auto md:p-4 transform hover:scale-125 duration-300 ease-in-out fill-current h-6"
              >SignUp</router-link
            >
            <button
              v-if="token"
              class="inline-block text-blue-300 no-underline hover:text-pink-500 hover:text-underline text-center h-10 p-2 md:h-auto md:p-4 transform hover:scale-125 duration-300 ease-in-out fill-current h-6"
              @click="logout"
            >
              LogOut
            </button>
          </div>
        </div>
      </nav>
      <router-view class="mt-32" />
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  computed: {
    token() {
      return this.$store.state.token;
    },
  },
  methods: {
    toHome() {
      if (this.token) {
        this.$router.push({ name: "MovieView" });
      } else {
        this.$router.push({ name: "LogInView" });
      }
    },
    logout() {
      this.$store.dispatch("logout");
    },
  },
};
</script>

<style>
@font-face {
  font-family: "Poppins", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji",
    "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  src: url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap");
}

@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap");

.first {
  font-family: "Poppins", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji",
    "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
}
/* html, body {
  margin: 0;
  padding: 0;
  height: 100vh;
  width: 100vw;
} */
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
} */
#app {
  /* font-family: 'Gowun Dodum', sans-serif; */
  /* font-family: "Riders-font";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; */
  text-align: center;
  /* color: white; */
  /* overflow: hidden; */
}

.background {
  background-image: url("./assets/header.png");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  height: 100vh;
  margin: 0;
  overflow: auto;
}

/* nav {
  padding: 10px 150px 30px;
  line-height: 80px;
} */

/* nav a {
  font-weight: bold;
  color: #2c3e50;
} */
/* nav a {
  font-weight: bold;
  color: rgb(166 229 227);
  text-decoration: none;
} */
/* nav a:hover {
  color: #0d6efd;
} */

/* nav a.router-link-exact-active {
  color: #42b983;
} */
/* nav a.router-link-exact-active {
  color: #2c3e50;
} */
/* .logout {
  font-weight: bold;
  color: rgb(166 229 227);
  text-decoration: none;
  cursor: pointer;
} */
/* .logout:hover {
  color: #0d6efd;
} */

/* #logo {
  width: 50px;
  height: 50px;
} */

/* #logo:hover {
  animation: rotate_image 3s linear infinite;
  transform-origin: 50% 50%;
} */

@keyframes rotate_image {
  100% {
    transform: rotate(360deg);
  }
}
</style>
