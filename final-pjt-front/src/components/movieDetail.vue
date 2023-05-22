<template>
  <div>
  <h1>{{ movie_detail_data.title }}</h1>
  <p>세부사항 페이지다 꾸며라잉</p>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "movieDetail",
  computed: {
    ...mapState(["movie_detail_data"]),
  },
}
</script>

<style>
</style>