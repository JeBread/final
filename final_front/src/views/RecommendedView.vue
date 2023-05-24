<template>
  <div class="container">
    <h1 class="title mb-5">Recommended</h1>
    <hr />
    <div
      class="recomovie"
      v-for="movie in fivemovies"
      :key="movie"
      :fivemovies="fivemovies"
    >
      <h3 class="font-semibold text-xl">{{ movie.title }}</h3>
      <p class="text-md">정답 횟수 : {{ movie.answerCnt }}</p>
      <router-link
        :to="{
          name: 'DetailView',
          params: { id: movie.id },
        }"
      >
        <img
          :src="movie.poster_path"
          class="rounded-lg shadow-lg hover:scale-110 duration-300 ease-in-out"
        />
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

<style scoped>
.recomovie {
  display: inline-block;
  margin: 30px;
  text-align: center;
  justify-content: center;
  align-items: center;
}

img {
  width: 180px;
  height: 250px;
}
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
