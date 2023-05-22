<template>
  <div>
    <p>{{ this.movieId }}</p>
  </div>
</template>

<script>
import axios from "axios"
const API_URL = "http://127.0.0.1:8000"

export default {
  name: "AboutView",
  data() {
    return {
      movieId: null,
    };
  },
  created() {
    this.movieId = this.$route.params.id;
    // this.getDetailInfo()
  },
  methods() {
    axios({
      method: 'get',
      url: `${API_URL}/movies/${this.movieId}/`,
    })
  },
};
</script>

<style>
</style>