<template>
  <div>
    <h1 class="detail_title">{{ movie_detail_data.title }}</h1>
    <div id="movie_detail_div">
      <img id="movie_poster" :src="getPosterImage" />
      <div class="text-content">
        <p>개봉일 : {{ movie_detail_data.release_date }}</p>
        <p>{{ movie_detail_data.overview }}</p>
        <p>평점 : {{ movie_detail_data.vote_average }}</p>
        <p>인기도 : {{ movie_detail_data.popularity }}</p>
        <p>
          {{ movie_detail_data.like_users.length }}명이 이 영화를 좋아합니다.
        </p>
        <button @click="likesbtn">좋아요</button>
      </div>
    </div>
      <iframe id="iframe" :src="frameSrc" frameborder="0"> </iframe>
  </div>
</template>

<script>
import { mapState } from "vuex";
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "movieDetail",
  data() {
    return {
      oneVideo: null,
    };
  },
  methods: {
    likesbtn() {
      const movieId = this.movie_detail_data.id;
      // console.log(this.token)
      axios({
        method: "post",
        url: `${API_URL}/movies/likes/${movieId}/`,
        headers: {
          Authorization: `Token ${this.token}`,
        },
      })
        .then(() => {
          // 여기에 store pickedMovie 실행하게 하고
          // watch로 state 의 movie_detail_data 좋아요 확인하게 함
          this.$store.dispatch("pickedMovie", this.movie_detail_data.id);
          // this.$store.dispatch("profile", this.$store.state.login_username);
          this.$store.dispatch("getMyLikeMovies");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    search(keyword) {
      const API_URL = "https://www.googleapis.com/youtube/v3/search";

      //api 요청해서 데이터 받아와서 this.videoList에 추가
      axios({
        url: API_URL,
        params: {
          method: "get",
          key: "AIzaSyCz9GxLsV2bVeTbsl00Z53l27f-cGO89jA",
          part: "snippet",
          type: "video",
          q: keyword + "예고편",
        },
      }).then((response) => {
        // console.log(response.data.items)
        // this.videoList = response.data.items
        this.oneVideo = response.data.items[0];
      });
    },
  },
  computed: {
    ...mapState(["movie_detail_data", "token"]),
    ...mapState({
      movieDetailData: (state) => state.movie_detail_data,
    }),
    // ...mapGetters(['pickedTitle']),
    getPosterImage() {
      return `https://image.tmdb.org/t/p/w200${this.movie_detail_data.poster_path}`;
    },

    frameSrc() {
      return `https://www.youtube.com/embed/${this.oneVideo?.id.videoId}`;
    },
  },
  watch: {
    movieDetailData(newData) {
      // console.log(newData.title)
      this.search(newData.title);
    },
  },
  created() {
    window.scrollTo(0, 0);
  },
};
</script>

<style>
.detail_title {
  font-size: 70px;
  font-weight: bold;
}
#movie_detail_div {
  display: flex;
  align-items: center;
  /* 기타 스타일을 적용해주세요 */
  width: auto;
}

#movie_detail_div-content {
  display: flex;
  align-items: center;
}

#movie_poster {
  width: 290px;
  height: 430px;
}
.text-content {
  display: flex;
  flex-direction: column;
  padding: 30px;
}
#iframe{
  width: 100%;
  height: 600px;
}
</style>