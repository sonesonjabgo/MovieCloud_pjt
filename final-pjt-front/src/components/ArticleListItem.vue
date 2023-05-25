<template>
  <div class="post-item">
    <!-- <p>{{ article.id }}</p> -->
    
    <router-link :to="{
      name: 'ArticleDetailView',
      params: { id: article.id }}" class="post-title router-link">
      <p>{{ article.title }}</p>
    </router-link>

    <p class="post-meta">작성 시간 : {{ article.created_at }}</p>
  </div>
</template>

<script>
export default {
    name: 'ArticleListItem',
    props: {
      article: Object,
    }
}
</script>

<style>
/* 게시물 항목 */
.post-item {
  border: 1px solid #ccc;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 10px;
}

/* 게시물 제목 */
.post-title {
  font-size: 18px;
  font-weight: bold;
  color: #61A2DA;
}

/* 게시물 작성자 및 날짜 */
.post-meta {
  font-size: 12px;
  color: #888;
}

.router-link {
  text-decoration: none;
}
</style>