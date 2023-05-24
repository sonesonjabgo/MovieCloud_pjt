<template>
  <div class="article-list">
    <h3>댓글 List</h3>
    <CommentListItem 
    v-for="comment in comments" :key="comment.id" :comment="comments"
    />
    <hr>
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem'

export default {
    name: 'CommentList',
    components: {
        CommentListItem,
    },
    computed: {
        comments(){ // 해당 아티클에 해당하는 댓글만 뽑아와야됨.
            return this.$store.state.articles
        }
    }

}
</script>

<style>
.article-list {
  text-align: start;
}
</style>