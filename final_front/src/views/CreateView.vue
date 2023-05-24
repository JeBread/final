<template>
  <div>
    <div
      class="container pt-14 md:pt-14 mx-auto flex flex-wrap flex-col md:flex-row items-center"
    >
      <!-- 게시글 작성 form -->
      <h1 class="mb-5 title">Post</h1>
      <form
        class="bg-gray-900 opacity-75 w-full shadow-lg rounded-lg px-8 pt-6 pb-8 mb-4"
        @submit.prevent="createArticle"
      >
        <div class="mb-4">
          <label class="block text-blue-300 py-2 font-bold mb-2" for="title">
          </label>
          <input
            class="shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out"
            type="text"
            id="title"
            placeholder="Title"
            v-model="title"
          /><br />

          <label class="block text-blue-300 py-2 font-bold mb-2" for="content">
          </label>
          <textarea
            class="shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out"
            id="content"
            cols="30"
            rows="10"
            placeholder="Content"
            v-model="content"
          ></textarea
          ><br />
          <div class="flex items-center justify-between pt-4">
            <input
              class="bg-gradient-to-r from-purple-800 to-green-500 hover:from-pink-500 hover:to-green-500 text-white font-bold py-2 px-4 rounded focus:ring transform transition hover:scale-105 duration-300 ease-in-out"
              type="submit"
              value="작성하기"
            />
          </div>
        </div>
      </form>
      <!-- 작성 form 종료 -->
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CreateView",
  data() {
    return {
      title: "",
      content: "",
    };
  },
  methods: {
    createArticle() {
      const title = this.title;
      const content = this.content;
      if (!title) {
        alert("제목을 입력해주세요.");
        return;
      } else if (!content) {
        alert("내용을 입력해주세요.");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/community/create/`,
        data: {
          title: title,
          content: content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          alert("게시글이 작성되었습니다.");
          this.$router.push({ name: "CommunityView" });
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style></style>
