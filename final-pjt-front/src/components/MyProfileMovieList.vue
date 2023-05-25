<template>
  <div>
    <br>
    <h1>{{ username }}님이 좋아요 누른 영화</h1>
    <div id="card_div" class="row flex-nowrap overflow-auto">
      <ProfileMovieListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
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
      movies: (state) => state.like_my_movies,
    }),
  },
  created(){
    this.$store.dispatch('getMyLikeMovies')
  },
  methods: {},
};
</script>
<style>
#card_div {
  width: auto;
  padding: 40px;
}
</style>