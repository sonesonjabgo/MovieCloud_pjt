<template>
  <div>
    <h3>{{ username }}님이 좋아요 누른 영화</h3>
    <div class="row">
      <ProfileMovieListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        class="col-lg-2 col-md-3 col-sm-4 col-6"
      />
    </div>
  </div>
</template>

<script>
import ProfileMovieListItem from "./ProfileMovieListItem.vue";
import { mapState } from "vuex";

export default {
  name: "ProfileMovieList",
  data() {
    return {
      username: this.$store.state.login_username,
    };
  },
  components: {
    ProfileMovieListItem,
  },
  computed: {
    ...mapState({
      movies: (state) => state.like_movies,
    }),
  },
  created(){
    this.$store.dispatch('getMyLikeMovies')
  },
  methods: {},
};
</script>
<style>
</style>