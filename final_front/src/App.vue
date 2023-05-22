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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
