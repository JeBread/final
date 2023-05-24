<template>
  <div class="justify-content-center align-content-center">
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
        <tbody>
          <tr class="bg-gray-300">
            <router-link
              class="text-gray-900 no-underline"
              :to="{
                name: 'ArticleDetailView',
                params: { articleId: article.id },
              }"
            >
              <th
                scope="row"
                class="px-6 py-4 font-lg text-lg text-gray-900 whitespace-nowrap dark:text-white"
              >
                {{ article.title }}
              </th>
            </router-link>
            <td class="px-6 py-4 text-lg text-black">{{ article.user }}</td>
            <td class="px-6 py-4 text-lg text-black">
              {{ article.like_users_count }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
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
