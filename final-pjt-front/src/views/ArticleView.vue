<template>
  <div>
    <h1>Community</h1>
    <router-link :to="{ name: 'CreateView' }" v-if="isLogin">[새 글 쓰기]</router-link>
    <ArticleList />
    
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'


export default {
    name:'ArticleView',
    components: {
        ArticleList,
    },
    computed:{
        isLogin() {
        return this.$store.getters.isLogin // 로그인 여부
        }
    },
    created() {
        this.getArticles()
    },
    methods: {
        getArticles() {
            this.$store.dispatch('getArticles')

    }
  }
}
</script>

<style>

</style>