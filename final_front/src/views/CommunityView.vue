<template>
  <div class="container">
    <h1 class="title">Community</h1>
    <router-link :to="{ name: 'CreateView' }">게시글 작성 </router-link>
    <hr />
    <ArticleList />
  </div>
</template>

<script>
import ArticleList from "@/components/ArticleList.vue";

export default {
  name: "CommunityView",
  components: {
    ArticleList,
  },
  computed: {},
  created() {
    this.getArticles();
  },
  methods: {
    getArticles() {
      this.$store.dispatch("getArticles"); // 커뮤니티 페이지 불러오기 ( 함수 만들기 전 )
    },
  },
};
</script>

<style>
.title {
  letter-spacing: 0px;
  background: linear-gradient(
    45deg,
    deepskyblue,
    deeppink,
    deepskyblue,
    deeppink
  );
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
  font-size: 40px;
}
</style>
