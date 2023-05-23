<template>
  <img
    id="poster"
    :src="getPosterImage"
    @click="imageClick"
    class="image-zoom"
  />
</template>

<script>
// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "TopListItem",
  props: {
    topmovie: Object,
  },
  computed: {
    getPosterImage() {
      return `https://image.tmdb.org/t/p/w200${this.topmovie.poster_path}`;
    },
  },
  methods: {
    imageClick() {
      this.$store.dispatch("pickedMovie", this.topmovie.id);
      this.$router.push({ name: 'movieDetail' })
      
    },
  },
};
</script>

<style>
.image-zoom {
  transition: transform 0.3s;
}

.image-zoom:hover {
  transform: scale(1.2); /* 원하는 이미지 확대 비율로 조정해주세요 */
}
</style>