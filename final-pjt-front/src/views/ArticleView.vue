<template>
  <div>
    <h1>Community</h1>
    <div class="board-container">
      <router-link :to="{ name: 'ArticleCreateView' }" v-if="isLogin" class="button">게시글 작성하기</router-link>
      <div class="post-list">
        <ArticleList />
      </div>
    </div>
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
      this.$store.dispatch('setlike_other_movies')
    }
  }
}
</script>

<style>
/* 게시판 컨테이너 */
.board-container {
  /* max-width: 800px; */
  /* margin: 0 auto; */
  padding: 20px;
  width: 100%;
  /* height: 3000px */
  
}
/* 게시물 목록 */
.post-list {
  list-style: none;
  padding: 0;
  /* width: 800px; */
}

/* 버튼 스타일 */
.button {
  display: inline-block;
  padding: 8px 16px;
  background-color: #61A2DA;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  text-decoration: none;
  font-size: 14px;
  margin-right: 0
}

.button:hover {
  background-color: #4c7eaa;
}

.button:active {
  background-color: #437097;
}
</style>