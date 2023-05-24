<template>
    <div>
        <h3 @click="articleClick">{{article.title}}</h3><hr>
    </div>
  </template>
  
  <script>
  export default {
      name : 'ProfileArticleItem',
      props:{
          article : Object,
      },
      methods: {
    articleClick() {
      // console.log(this.article.id)
      this.$store.dispatch("pickedAritlce", this.article.id);
      this.$router.push({ name: 'articleDetail' })
    },
  },
  
  }
  </script>
  
  <style>
  
  </style>