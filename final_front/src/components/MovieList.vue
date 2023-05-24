<template>
  <div class="movie-list" style="margin-left: 10%; margin-right: 10%">
    <div class="MovieView">
      <div class="title" style="text-align: center; margin-top: 65px">
        Movie List
      </div>
      <hr />
      <div class="container flex flex-wrap">
        <MovieListItem v-for="movie in movies" :key="movie.id" :movie="movie" />
      </div>
    </div>
  </div>
</template>

<script>
import MovieListItem from "@/components/MovieListItem";
// import { Carousel } from "vue-carousel";

export default {
  name: "MovieList",
  components: {
    MovieListItem,
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
  },
};
</script>

<style>
.article-list {
  text-align: start;
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
