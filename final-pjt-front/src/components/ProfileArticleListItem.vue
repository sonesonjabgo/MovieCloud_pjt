<template>
  <div>
    <h3 @click="imageClick">{{ article.title }}</h3>
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
    imageClick() {
      this.$store.dispatch("pickedAritlce", this.article.id);
      this.$router.push({ name: "ArticleDetailView" });
    },
  },
};
</script>
  
  <style>
</style>