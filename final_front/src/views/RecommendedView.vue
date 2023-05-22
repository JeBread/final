<template>
  <div class="">
    <h1>영화 추천 페이지</h1>
    <hr />
    <div v-for="movie in fivemovies" :key="movie" :fivemovies="fivemovies">
      <h3 class="fw-bold">{{ movie.title }}</h3>
      <p>정답 횟수 : {{ movie.answerCnt }}</p>
      <router-link
        :to="{
          name: 'DetailView',
          params: { id: movie.id },
        }"
      >
        <img :src="movie.poster_path" alt="" width="200" />
      </router-link>
      <hr />
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "RecommendedView",
  data() {
    return {
      fivemovies: [],
    };
  },
  components: {},
  computed: {},
  created() {
    this.getRecommendedMovies();
  },
  methods: {
    getRecommendedMovies() {
      axios({
        method: "get",
        url: `${API_URL}/movies/recommend/`,
      })
        .then((res) => {
          console.log(res);
          this.fivemovies = res.data;
          this.fivemovies.forEach((movie) => {
            movie.poster_path =
              "https://image.tmdb.org/t/p/original" + movie.poster_path;
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style></style>
