<template>
  <div>
    <h1>Movie Page</h1>
    <!-- <MovieList /> -->
    sfdasd
    <hr />
  </div>
</template>

<script>
// import MovieList from "@/components/MovieList.vue";

export default {
  name: "MovieView",
  components: {
    // MovieList,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin; // 로그인 여부
    },
  },
  created() {
    this.getMovies();
  },
  methods: {
    getMovies() {
      if (this.isLogin) {
        this.$store.dispatch("getMovies");
      } else {
        alert("로그인이 필요한 페이지입니다...");
        this.$router.push({ name: "LogInView" });
      }

      // 로그인이 되어 있으면 getMovies action 실행
      // 로그인 X라면 login 페이지로 이동
    },
  },
};
</script>

<style></style>
