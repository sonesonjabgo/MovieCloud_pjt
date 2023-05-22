<template>
  <div>
    <h3>{{ username }}님 작성한 게시글</h3>
    <ProfileArticleListItem 
    v-for="article in articles" :key="article.id" :article="article"
    />
  </div>
</template>

<script>
import ProfileArticleListItem from './ProfileArticleListItem.vue';

export default {
    name: "ProfileMovieList",
    data(){
      return {
        username: this.$store.state.profile_username
      }
    },
    components: {
      ProfileArticleListItem
    },
    computed: {
      articles(){
          return this.$store.state.articles.filter((element)=>{ element.user == this.$store.state.profile_userid})
      }
    },
    created(){
      
    }
    
}
</script>

<style>

</style>