<template>
  <div class="post-item">
    
    <!-- <h5>{{ comment.id }}</h5> -->
    <p class="post-title router-link">{{ comment.content }}</p>
    <!-- <hr> -->
  </div>
</template>

<script>
export default {
    name: 'CommentListItem',
    props: {
      comment: Object,
    }
}
</script>

<style>
/* 게시물 항목 */
.post-item {
  border: 1px solid #ccc;
  margin-bottom: 10px;
  margin-top: 10px;
  padding: 10px;
  border-radius: 10px;
}
/* 게시물 제목 */
.post-title {
  font-size: 18px;
  font-weight: bold;
  color: #61A2DA;
}
.router-link {
  text-decoration: none;
}
</style>