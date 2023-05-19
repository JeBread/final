<template>
  <div>
    <h1>퀴즈 페이지</h1>
  </div>
</template>

<script>
export default {
  name: "QuizView",
  components: {},
  computed: {},
  created() {
    this.getQuiz();
  },
  methods: {
    getQuiz() {
      this.$store.dispatch("getQuiz"); // 퀴즈 페이지 불러오기 ( 함수 만들기 전 )
    },
  },
};
</script>

<style></style>
