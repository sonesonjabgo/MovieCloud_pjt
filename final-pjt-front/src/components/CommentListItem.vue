<template>
  <div>
    <h5>{{ comment.id }}</h5>
    <p>{{ comment.content }}</p>
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

</style>