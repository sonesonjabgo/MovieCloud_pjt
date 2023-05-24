<template>
  <div>
    <h3>{{ username }}님이 좋아요 누른 영화</h3>
    <div>
      <ProfileMovieListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import ProfileMovieListItem from './ProfileMovieListItem.vue';
import { mapState } from "vuex";

export default {
    name: "ProfileMovieList",
    data(){
      return {
        username: this.$store.state.login_username,
        // movies: this.$store.state.like_movies,
      }
    },
    components: {
      ProfileMovieListItem
    },
    // created(){
    //   this.$store.dispatch('getMyLikeMovies')
    // },
    computed: {
      ...mapState({
            movies : state => state.like_movies,
            // follower : state => state.profile_userfollower,

      }),
    },
    methods: {
    },
  //   watch : {
  //     movies(){
  //         // console.log(newData.title)
  //         this.$store.dispatch('getMyLikeMovies')
  //       }
  // },
}
</script>

<style>
</style>