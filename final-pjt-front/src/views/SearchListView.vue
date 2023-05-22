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
  }
}
</script>

<style>

</style>