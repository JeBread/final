<template>
  <div class="movies container">
    <h1>영화 페이지</h1>
    <div class="carousel-wrapper">
      <div class="carousel">
        <div class="wrapper">
          <div class="carousel-content">
            <h5>{{ movie.id }}</h5>
            <img :src="poster_url" alt="" width="200" />
            <p>{{ movie.title }}</p>
            <p>{{ movie.vote_average }}</p>
            <router-link
              :to="{
                name: 'DetailView',
                params: { id: movie.id },
              }"
            >
              [DETAIL]
            </router-link>
            <hr />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieListItem",
  props: {
    movie: Object,
  },
  data() {
    return {
      poster_url:
        "https://image.tmdb.org/t/p/original" + this.movie.poster_path,
    };
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
  },
};
</script>

<style></style>
