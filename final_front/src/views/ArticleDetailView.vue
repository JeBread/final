<template>
  <div class="container">
    <h1 class="title mb-5">Post Detail</h1>
    <hr />
    <div
      class="bg-gray-900 text-blue-300 opacity-75 w-full shadow-lg rounded-lg px-8 pt-5 pb-4 mb-5 mt-5"
    >
      <h2 class="text-indigo-400 font-semibold">{{ article?.title }}</h2>
      <p class="mt-4">작성자 : {{ article?.username }}</p>
      <p class="text-lg mt-4 text-indigo-400 font-semibold">
        {{ article?.content }}
      </p>
      <p class="mt-4">작성 일시 <br />{{ create_time }}</p>
      <span class="mt-4 flex justify-center"
        ><svg
          @click="likeMovie"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="w-6 h-6 relative object-center"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M6.633 10.5c.806 0 1.533-.446 2.031-1.08a9.041 9.041 0 012.861-2.4c.723-.384 1.35-.956 1.653-1.715a4.498 4.498 0 00.322-1.672V3a.75.75 0 01.75-.75A2.25 2.25 0 0116.5 4.5c0 1.152-.26 2.243-.723 3.218-.266.558.107 1.282.725 1.282h3.126c1.026 0 1.945.694 2.054 1.715.045.422.068.85.068 1.285a11.95 11.95 0 01-2.649 7.521c-.388.482-.987.729-1.605.729H13.48c-.483 0-.964-.078-1.423-.23l-3.114-1.04a4.501 4.501 0 00-1.423-.23H5.904M14.25 9h2.25M5.904 18.75c.083.205.173.405.27.602.197.4-.078.898-.523.898h-.908c-.889 0-1.713-.518-1.972-1.368a12 12 0 01-.521-3.507c0-1.553.295-3.036.831-4.398C3.387 10.203 4.167 9.75 5 9.75h1.053c.472 0 .745.556.5.96a8.958 8.958 0 00-1.302 4.665c0 1.194.232 2.333.654 3.375z"
          /></svg>
        </span>
      <br />
      <p>{{ like_users_count }}</p>
    </div>
    <hr />
    <div
      class="text-xl"
      v-for="(comment, idx) in article.comment_set"
      :key="idx"
    >
      <div>
        {{ comment.content }} <span style="opacity: 0"> | </span> |
        <span style="opacity: 0"> | </span> {{ comment.username }}
      </div>
      <hr />
    </div>

    <div>
      <h4 class="mt-4 text-blue-400 font-semibold">Comment</h4>
      <div
        class="container pt-1 md:pt-1 mx-auto flex flex-wrap flex-col md:flex-row items-center"
      >
        <div
          class="bg-gray-900 opacity-75 w-full shadow-lg rounded-lg px-8 pt-6 pb-3 mb-4"
        >
          <div class="block text-blue-300 py-2 font-bold mb-2">
            <input
              type="text"
              maxlength="100"
              style="width: 100%; height: 180px"
              class="shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out"
              v-model="new_comment_content"
            />
            <br />
            <br />
            <button
              class="bg-gradient-to-r from-purple-800 to-green-500 hover:from-pink-500 hover:to-green-500 text-white font-bold py-2 px-4 rounded focus:ring transform transition hover:scale-105 duration-300 ease-in-out"
              @click="createComment"
            >
              작성하기
            </button>
          </div>
        </div>
      </div>
    </div>
    <button
      class="mb-5 font-semibold text-blue-400 no-underline hover:text-pink-500 hover:text-underline text-center h-10 p-2 md:h-auto md:p-4 transform hover:scale-125 duration-300 ease-in-out fill-current h-6 mx-auto"
      @click="goBack"
    >
      뒤로 가기
    </button>
    <br />
    <br />
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
      new_comment_content: "",
      create_time: "",
      like_users_count: "",
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
          this.getCreateTime();
        })
        .catch((err) => console.log(err));
    },
    goBack() {
      this.$router.go(-1);
    },

    createComment() {
      axios({
        method: "post",
        url: `${API_URL}/community/${this.article.id}/comments/create/`,
        data: { content: this.new_comment_content },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          this.new_comment_content = "";
          this.getArticleDetail();
        })
        .catch((err) => console.log(err));
    },
    getCreateTime() {
      this.create_time =
        this.article.created_at.split("T")[0] +
        " " +
        this.article.created_at.split("T")[1].split(".")[0];
    },
    likeMovie() {
      this.like_users_count = this.article.like_users_count++;
    },
  },
};
</script>

<style></style>
