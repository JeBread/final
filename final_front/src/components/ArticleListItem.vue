<template>
  <div>
    <h5>{{ article.id }}</h5>
    <router-link
      :to="{
        name: 'ArticleDetailView',
        params: { articleId: article.id },
      }"
    >
      <p>게시글 제목 : {{ article.title }}</p>
    </router-link>
    <p>작성자 : {{ article.user }}</p>
    <p>게시글 내용 : {{ article.content }}</p>
    <p>좋아요 : {{ article.like_users_count }}</p>
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
