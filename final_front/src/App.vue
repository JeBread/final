<template>
  <div id="app">
    <nav class="d-flex justify-content-between">
      <img
        src="./assets/logo.png"
        alt=""
        id="logo"
        @click="toHome"
        width="50"
        height="50"
      />
      <div>
        <router-link v-if="token" :to="{ name: 'MovieView' }"
          >영화 목록</router-link
        ><span v-if="token"> | </span>
        <router-link v-if="token" :to="{ name: 'QuizView' }">퀴즈</router-link>
        <span v-if="token"> | </span>
        <router-link v-if="token" :to="{ name: 'OstView' }"
          >Ost</router-link
        ><span v-if="token"> | </span>
        <router-link v-if="token" :to="{ name: 'RecommendedView' }"
          >영화 추천</router-link
        ><span v-if="token"> | </span>
        <router-link v-if="token" :to="{ name: 'CommunityView' }"
          >커뮤니티</router-link
        ><span v-if="token"> | </span>
        <router-link v-if="!token" :to="{ name: 'SignUpView' }"
          >회원가입</router-link
        >
        <button v-if="token" class="logout" @click="logout">로그아웃</button>
      </div>
    </nav>
    <router-view />
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
        this.$router.push({ name: "LoginView" });
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
  font-family: "Riders-font";
  src: url("./assets/fonts/BMHANNAPro.ttf");
}
/* html,
body {
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
  font-family: "Riders-font";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background-color: rgb(42 193 188);
  height: 100%;
  /* overflow: hidden; */
}

nav {
  padding: 10px 150px 30px;
  line-height: 80px;
}

/* nav a {
  font-weight: bold;
  color: #2c3e50;
} */
nav a {
  font-weight: bold;
  color: rgb(166 229 227);
  text-decoration: none;
}
nav a:hover {
  color: #0d6efd;
}

/* nav a.router-link-exact-active {
  color: #42b983;
} */
nav a.router-link-exact-active {
  color: #2c3e50;
}
.logout {
  font-weight: bold;
  color: rgb(166 229 227);
  text-decoration: none;
  cursor: pointer;
}
.logout:hover {
  color: #0d6efd;
}

#logo {
  width: 150px;
  height: 100px;
}

#logo:hover {
  animation: rotate_image 3s linear infinite;
  transform-origin: 50% 50%;
}

@keyframes rotate_image {
  100% {
    transform: rotate(360deg);
  }
}
</style>
