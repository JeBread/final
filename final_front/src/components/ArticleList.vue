<template>
  <div class="article-list justify-content-center mt-5">
    <ArticleListItem
      v-for="article in articles"
      :key="article.id"
      :article="article"
    />
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
