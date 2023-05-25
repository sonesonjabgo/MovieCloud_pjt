<template>
  <div class="article-list">
    <h3>Article List</h3>
    <ArticleListItem 
    v-for="article in displayedArticle" :key="article.id" :article="article"
    />
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'

export default {
  name: 'ArticleList',
  components: {
      ArticleListItem,
  },
  data() {
    return {
      posts: [], // 전체 게시글 목록
      currentPage: 1, // 현재 페이지
      postsPerPage: 10, // 페이지당 게시글 수
    };
  },
  computed: {
    articles(){
        return this.$store.state.articles
    },
    totalPages() {
      return Math.ceil(this.articles.length / this.postsPerPage);
    },
    displayedArticle() {
      const startIndex = (this.currentPage - 1) * this.postsPerPage;
      const endIndex = startIndex + this.postsPerPage;
      return this.articles.slice(startIndex, endIndex);
    },
  },
  methods: {
    setCurrentPage(page) {
      this.currentPage = page;
    },
  },

}
</script>

<style>
.article-list {
  text-align: start;
}
</style>