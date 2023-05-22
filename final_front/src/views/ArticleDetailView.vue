<template>
  <div>
    <h1>게시글 상세 정보</h1>
    <p>제목 : {{ article?.title }}</p>
    <p>작성자 : {{ article?.user }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성 시간 : {{ article?.created_at }}</p>
    <p>수정 시간 : {{ article?.updated_at }}</p>
    <button @click="goBack">뒤로 가기</button>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "ArticleDetailView",
  data() {
    return {
      article: null,
    };
  },
  created() {
    this.getArticleDetail();
  },
  methods: {
    getArticleDetail() {
      axios({
        method: "get",
        url: `${API_URL}/community/${this.$route.params.articleId}/`,
      })
        .then((res) => {
          console.log(res);
          this.article = res.data;
        })
        .catch((err) => console.log(err));
    },
    goBack() {
      this.$router.go(-1);
    },
  },
};
</script>

<style></style>
