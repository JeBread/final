<template>
  <div>
    <h1>Detail</h1>
    <img :src="movie.poster_path" alt="" width="200" />
    <p>영화 제목 : {{ movie?.title }}</p>
    <p>평점 : {{ movie.vote_average }}</p>
    <p>개봉일 : {{ movie.release_date }}</p>
    <p>줄거리 : {{ movie?.overview }}</p>
    <button @click="goBack">뒤로 가기</button>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "DetailView",
  data() {
    return {
      movie: null,
    };
  },
  created() {
    this.getMovieDetail();
  },
  methods: {
    getMovieDetail() {
      axios({
        method: "get",
        url: `${API_URL}/movies/${this.$route.params.id}/`,
      })
        .then((res) => {
          console.log(res);
          this.movie = res.data;
          this.movie.poster_path =
            "https://image.tmdb.org/t/p/original" + this.movie.poster_path;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goBack() {
      this.$router.go(-1);
    },
  },
};
</script>
