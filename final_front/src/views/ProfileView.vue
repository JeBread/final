<template>
  <div>
    <h1>프로필 페이지</h1>
    <h2>안녕하세요 {{ userName }}</h2>
  </div>
</template>

<script>
export default {
  name: "ProfileView",
  data() {
    return {
      userName: this.$route.params.userName,
    };
  },
  components: {},
  computed: {
    isLogin() {
      return this.$store.getters.isLogin; // 로그인 여부
    },
  },
  created() {
    this.getProfile();
  },
  methods: {
    getProfile() {
      if (this.isLogin) {
        this.$store.dispatch("getProfile"); // 프로필 페이지 불러오기 ( 함수 만들기 전 )
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
