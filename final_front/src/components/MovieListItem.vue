<template>
  <div class="movies container">
    <div class="carousel-wrapper">
      <div class="carousel">
        <div class="wrapper">
          <div class="carousel-content">
            <router-link
              :to="{
                name: 'DetailView',
                params: { id: movie.id },
              }"
              ><img :src="poster_url" alt="" width="200" />
            </router-link>
            <br />
            <h5>{{ movie.title }}</h5>
            <p>{{ movie.vote_average }}</p>
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
