<template>
  <div>
    <div class="container">
      <h1 class="title">Community</h1>
      <div class="flex justify-end">
        <router-link :to="{ name: 'CreateView' }">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="#facc15"
            class="w-6 h-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10"
            />
          </svg>
        </router-link>
      </div>
      <hr />
      <ArticleList />
    </div>
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
