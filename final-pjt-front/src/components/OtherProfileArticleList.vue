<template>
  <div>
    <br />
    <br />
    <h1>{{ username }}님이 작성한 게시글</h1>
    <br />
    <div class="article-item">
      <ProfileArticleListItem
        v-for="article in articles"
        :key="article.id"
        :article="article"
        class="article-list"
      />
    </div>
  </div>
</template>

<script>
import ProfileArticleListItem from "./ProfileArticleListItem.vue";
import { mapState } from "vuex";

export default {
  name: "ProfileArticleList",
  data() {
    return {
      username: this.$store.state.profile_username,
      // articles: this.$store.state.wrote_articles,
    };
  },
  components: {
    ProfileArticleListItem,
  },
  computed: {
    ...mapState({
      articles: (state) => state.wrote_articles,
      // follower : state => state.profile_userfollower,
    }),
  },
  methods: {},
  created() {
    this.$store.dispatch("getOtherWroteArticles");
  },
};
</script>

<style>
</style>