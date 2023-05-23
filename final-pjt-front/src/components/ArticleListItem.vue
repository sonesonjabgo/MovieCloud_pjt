<template>
  <div>
    <h5>{{ article.id }}</h5>
    
    <router-link :to="{
      name: 'ArticleDetailView',
      params: {id: article.id }}">
      <p>{{ article.title }}</p>
    </router-link>
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

</style>