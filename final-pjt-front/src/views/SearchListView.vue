<template>
  <div>
  <h1>SearchList</h1>
  <!-- search bar -->
  <SearchBar />
  <!-- search list item x 100 -->
  <SearchListItem 
  v-for="search in searchlist" :key="search.id" :search="search"
  />
  </div>
</template>

<script>
import SearchBar from "@/components/SearchBar.vue"
import SearchListItem from "@/components/SearchListItem.vue"

export default {
  name : 'SearchListView',
  components: {
    SearchBar, SearchListItem,
  },
  computed: {
    searchlist() {
      return this.$store.state.searchlist
    }
  },
  created () {
    window.scrollTo(0, 0);
  }
  // created() {
  //   // state에서 search data 받아와서 search list item 으로 넘겨주기
  // }
}
</script>

<style>
  .results {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
  }
  .item {
      /* width: 200px; */
      margin: 10px;
      padding: 10px;
      border: 1px solid #ccc;
      text-align: center;
  }
</style>