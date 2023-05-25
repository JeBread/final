<template>
  <div class="justify-center container">
    <h1 class="title">Detail</h1>
    <hr />
    <!-- 여기서 부터는 새로운 디테일 페이지 -->
    <div class="d-flex bg-gray-900 bg-opacity-60 mt-5 rounded-lg">
      <div class="poster-container">
        <img class="poster-image" :src="movie.poster_path" alt="" />
      </div>

      <div class="movie-details mx-5 mt-4">
        <h2 class="movie-title mx-auto mt-3">{{ movie.title }}</h2>
        <div class="rating-date mx-auto mt-4">
          <div class="rating">평점: {{ movie.vote_average }}</div>
          <div class="release-date">개봉일: {{ movie.release_date }}</div>
        </div>
        <div class="overview">{{ movie.overview }}</div>
        <br />
        <br />
        <div class="button-container d-flex justify-between">
          <p style="opacity: 0">///////////////</p>
          <button
            @click="goBack"
            class="mb-3 font-semibold text-blue-400 no-underline hover:text-pink-500 hover:text-underline text-center h-10 p-2 md:h-auto md:p-4 transform hover:scale-125 duration-300 ease-in-out fill-current h-6 mx-auto"
          >
            뒤로 가기
          </button>
          <YoutubePlayer
            :video-id="movie.ost"
            class="justify-center content-center"
          />
        </div>
      </div>
    </div>

    <div class="video-player-container">
    <MovieVideoPlayer :video-id="movie.video" class="video-player" />
  </div>
    <!-- <div v-if="yego == true" class="bg-dark">
      <div class="justify-center justify-items-center items-center content-center">
    <youtube :video-id="videoId" ref="youtube" style=""></youtube>
  </div>
  <button @click="yego = false"></button>
    </div> -->
  </div>
</template>

<script>
import MovieVideoPlayer from "@/components/MovieVideoPlayer.vue";
import axios from "axios";
import YoutubePlayer from "@/components/YoutubePlayer.vue";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "DetailView",
  components: {
    MovieVideoPlayer,
    YoutubePlayer,
  },
  data() {
    return {
      movie: null,
      yego: false,
    };
  },
  created() {
    this.getMovieDetail();
  },
  computed: {
    player() {
      return this.$refs.youtube.player;
    },
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

<style>
.poster-container {
  flex-shrink: 0;
}

/* .bg-darkk {
  background-color: #343a4071;
} */

.poster-image {
  height: 400px;
  width: auto;
  max-width: 100%;
  border-radius: 10px;
  object-fit: cover;
}

.movie-details {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.movie-title {
  font-size: 24px;
  margin: 0;
}

.rating-date {
  display: flex;
  font-size: 16px;
  margin-top: 10px;
}

.rating {
  margin-right: 10px;
}

.overview {
  font-size: 16px;
  margin-top: 20px;
}

.video-player-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 4rem;
}
</style>
