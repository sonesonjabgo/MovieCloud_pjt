<template>
  <div id="profileImg">
    <img id="poster" @click="imageClick" :src="getPosterImage" alt="" />
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
  methods: {
    imageClick() {
      this.$store.dispatch("pickedMovie", this.movie.id);
      this.$router.push({ name: 'movieDetail' })
    },
  },
};
</script>
  
<style>
#profileImg {
  width: fit-content;
}
</style>