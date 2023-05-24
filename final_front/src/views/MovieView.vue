<template>
  <div class="">
    <div>
      <p>테스트</p>
      <Flicking class="slide" :options="{ circular: true }" :plugins="plugins">
        <MovieListItem
          v-for="movie in this.$store.state.movies"
          :key="movie.id"
          :movie="movie"
        ></MovieListItem>
      </Flicking>
    </div>
    <hr />
    <MovieList />
  </div>
</template>

<script>
import MovieList from "@/components/MovieList.vue";
import { Flicking } from "@egjs/vue-flicking";
import { Fade, Perspective, AutoPlay } from '@egjs/flicking-plugins'
import MovieListItem from "@/components/MovieListItem.vue";

export default {
  name: "MovieView",
  data(){
    return {
      plugins: [new Fade(), new Perspective({ rotate: -1 }), new AutoPlay({ duration: 2000, direction: "NEXT", stopOnHover: false })],
    }
  },
  components: {
    MovieList,
    Flicking: Flicking,
    MovieListItem,
  },
  computed: {},
  created() {
    this.getMovies();
  },
  methods: {
    getMovies() {
      this.$store.dispatch("getMovies");
    },
  },
};
</script>

<style scoped>
@import "@egjs/vue-flicking/dist/flicking.css";
</style>
