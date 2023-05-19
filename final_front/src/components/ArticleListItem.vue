<template>
  <div>
    <router-link
      :to="{
        name: 'ArticleDetailView',
        params: { articleId: article.id },
      }"
    >
      게시글 상세 정보
    </router-link>
  </div>
</template>

<script>
export default {
  name: "ArticleListItem",
  props: {
    article: Object,
  },
};
</script>

<style></style>
