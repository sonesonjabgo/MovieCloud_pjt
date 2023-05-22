<template>
  <div>
    <h3>{{ username }}님이 좋아요 누른 영화</h3>
    <div>
      <ProfileMovieListItem 
      v-for="movie in movies" :key="movie.id" :movie="movie"
      />
    </div>
    
  </div>
</template>

<script>
import ProfileMovieListItem from './ProfileMovieListItem.vue';

export default {
    name: "ProfileMovieList",
    data(){
      return {
        username: this.$store.state.profile_username
      }
    },
    components: {
      ProfileMovieListItem
    },
    computed: {
      movies(){
          return this.$store.state.movies.filter((element)=>{ element.like_users == this.$store.state.profile_userid})
      }
    },
    methods: {
    },
    
}
</script>

<style>

</style>