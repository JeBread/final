<template>
  <!-- <div class="article-list justify-content-center mt-5"> -->
  <div class="justify-content-center align-content-center mt-5">
    <div class="relative overflow-x-auto">
      <table class="w-full text-sm text-left dark:text-gray-400">
        <thead
          class="text-xs uppercase bg-gray-900 bg-opacity-60 dark:bg-gray-700"
        >
          <tr>
            <th scope="col" class="px-6 py-3 text-lg rounded-l-lg">
              게시글 제목
            </th>
            <th scope="col" class="px-6 py-3 text-lg">작성자</th>
            <th scope="col" class="px-6 py-3 text-lg rounded-r-lg">좋아요</th>
          </tr>
        </thead>
        <ArticleListItem
          v-for="article in articles"
          :key="article.id"
          :article="article"
        />
      </table>
    </div>
  </div>
</template>

<script>
import ArticleListItem from "@/components/ArticleListItem.vue";

export default {
  name: "ArticleList",
  components: {
    ArticleListItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles;
    },
  },
};
</script>

<style>
.article-list {
  text-align: start;
}
</style>
