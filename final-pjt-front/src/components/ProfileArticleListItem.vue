<template>
  <div class="post-item">
    <h3 @click="articleClick" class="post-title router-link">{{ article.title }}</h3>
    <hr />
  </div>
</template>
  
  <script>
export default {
  name: "ProfileArticleItem",
  props: {
    article: Object,
  },
  methods: {
    articleClick() {
      // console.log(this.article.id)
      this.$store.dispatch("pickedAritlce", this.article.id);
      this.$router.push({ name: "articleDetail" });
    },
  },
};
</script>
  
<style>
.post-item {
  border: 1px solid #ccc;
  margin-bottom: 10px;
  margin-top: 10px;
  padding: 10px;
  border-radius: 10px;
}
.post-title {
  font-size: 18px;
  font-weight: bold;
  color: #61A2DA;
}
.router-link {
  text-decoration: none;
}
</style>