<template>
    <div>
        <h3>{{article.title}}</h3><hr>
    </div>
  </template>
  
  <script>
  export default {
      name : 'ProfileArticleItem',
      props:{
          article : Object,
      },
  
  }
  </script>
  
  <style>
  
  </style>