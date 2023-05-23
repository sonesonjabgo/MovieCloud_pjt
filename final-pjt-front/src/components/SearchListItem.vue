<template>
  <div class="item" @click="divClick">
    <img :src="getPosterImage" />
    <div class="text-content">
      <h3>{{ search.title }}</h3>
      <p class="limited-text">{{ search.overview }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchListItem",
  props: {
    search: Object,
  },
  computed: {
    getPosterImage() {
      return `https://image.tmdb.org/t/p/w200${this.search.poster_path}`;
    },
  },
  methods: {
    divClick() {
      this.$store.dispatch("pickedMovie", this.search.id);
      this.$router.push({ name: 'movieDetail' })
    },
  },
};
</script>

<style>
.item {
  display: flex;
  align-items: center;
  /* 기타 스타일을 적용해주세요 */
  width: auto;
}

.item-content {
  display: flex;
  align-items: center;
}

img {
  width: 200px; /* 이미지 크기를 원하는 대로 조정해주세요 */
  height: auto;
  margin-right: 10px; /* 이미지와 텍스트 사이 간격을 조정해주세요 */
}

.text-content {
  display: flex;
  flex-direction: column;
  padding: 30px;
}

h3,
p {
  margin: 0;
}
/* .limited-text {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: wrap;
  max-width: 5000px; 
  /* 원하는 글자 수에 맞춰 조정해주세요 */
</style>