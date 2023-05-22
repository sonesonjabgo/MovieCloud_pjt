<template>
  <div>
    <h3>{{ username }}님이 작성한 게시글</h3>
    <div>
      <ProfileArticleListItem 
      v-for="article in articles" :key="article.id" :article="article"
      />
    </div>
    
  </div>
</template>

<script>
import ProfileArticleListItem from './ProfileArticleListItem.vue';

export default {
    name: "ProfileArticleList",
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
    methods: {
    },
    
}
</script>

<style>

</style>