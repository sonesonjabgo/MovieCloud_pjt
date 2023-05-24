<template>
  <div>
    <h3>{{ username }}님이 좋아요 누른 영화</h3>
    <div>
      <ProfileMovieListItem 
      v-for="movie in movies" :key="movie.id" :movie="movie"
      />
    <p>overview 모은 거 : {{ like_movies_overview }}</p>
    </div>
    
  </div>
</template>

<script>
import ProfileMovieListItem from './ProfileMovieListItem.vue';

export default {
    name: "ProfileMovieList",
    data(){
      return {
        username: this.$store.state.profile_username,
        movies: this.$store.state.like_movies,
      }
    },
    components: {
      ProfileMovieListItem
    },
    created(){
      this.$store.dispatch('getLikeMovies')
      
    },
    computed: {
      like_movies_overview() {
        let my_overview = this.movies.map(function(el){
          return el.overview
        })
        return my_overview
      }
    },
    methods: {
    },
    
}
</script>

<style>

</style>