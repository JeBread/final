<template>
  <div>퀴즈 페이지</div>
</template>

<script>
export default {
  name: "QuizView",
  components: {},
  computed: {
    isLogin() {
      return this.$store.getters.isLogin; // 로그인 여부
    },
  },
  created() {
    this.getQuiz();
  },
  methods: {
    getQuiz() {
      if (this.isLogin) {
        this.$store.dispatch("getQuiz"); // 퀴즈 페이지 불러오기 ( 함수 만들기 전 )
      } else {
        alert("로그인이 필요한 페이지입니다...");
        this.$router.push({ name: "LogInView" });
      }

      // 로그인이 되어 있으면 getQuiz action 실행
      // 로그인 X라면 login 페이지로 이동
    },
  },
};
</script>

<style></style>
