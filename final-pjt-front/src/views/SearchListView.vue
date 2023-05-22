<template>
  <div>
  <h1>SearchList</h1>
  <!-- search bar -->
  <SearchBar />
  <!-- search list item x 100 -->
  </div>
</template>

<script>
import SearchBar from "@/components/SearchBar.vue"

export default {
  name : 'SearchListView',
  components: {
    SearchBar,
  },
  created() {
    // state에서 search data 받아와서 search list item 으로 넘겨주기
  }
}
</script>

<style>

</style>