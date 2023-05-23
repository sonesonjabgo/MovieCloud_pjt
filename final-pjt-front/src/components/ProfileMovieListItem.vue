<template>
  <div>
    <img id="poster" :src="getPosterImage" alt="" />
  </div>
</template>
  
  <script>
export default {
  name: "ProfileMovieItem",
  props: {
    movie: Object,
  },
  computed: {
    getPosterImage() {
      return `https://image.tmdb.org/t/p/w200${this.movie.poster_path}`;
    },
  },
};
</script>
  
  <style>
</style>