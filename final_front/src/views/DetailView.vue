<template>
  <div>
    <h1>Detail</h1>
    <p>{{ movie?.id }}</p>
    <img :src="poster_url" alt="" width="200" />
    <p>영화 제목 : {{ movie?.title }}</p>
    <p>줄거리 : {{ movie?.overview }}</p>
    <p>작성시간 : {{ movie?.created_at }}</p>
    <p>수정시간 : {{ movie?.updated_at }}</p>
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
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
