<template>
  <div class="home">
    <div class="image-container">
      <img id="mainposter" :src="getPosterImage" />
      <div class="search-container">
        <h1 class="welcome_text">Welcome</h1>
        <h3 class="welcome_content">내가 몰랐던, 나의 취향</h3>
        <hr />
        <SearchBar />
      </div>
    </div>
    <!-- <div id="high-list" class="container"> -->
    <!-- <div id="classification_name"> -->
    <br />
    <h1 id="classification_name" class="big-text">
      요즘엔 이 영화들이 인기 있어요.
    </h1>
    <!-- </div> -->
    <div id="card_div" class="row flex-nowrap overflow-auto">
      <HighListItem
        v-for="highmovie in highList"
        :key="highmovie.id"
        :highmovie="highmovie"
      />
    </div>
    <!-- </div> -->
    <br />
    <!-- <div id="top-list" class="container"> -->
    <!-- <div id="classification_name"> -->
    <br />
    <h1 class="big-text">오늘은 고전 명작 영화 어때요?</h1>
    <!-- </div> -->
    <div id="card_div" class="row flex-nowrap overflow-auto">
      <TopListItem
        v-for="topmovie in topList"
        :key="topmovie.id"
        :topmovie="topmovie"
      />
    </div>
    <!-- </div> -->
  </div>
</template>

<script>
import axios from "axios"
import { mapGetters, mapState } from "vuex";

import SearchBar from "@/components/SearchBar.vue";
import TopListItem from "@/components/TopListItem.vue";
import HighListItem from "@/components/HighListItem.vue";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "HomeView",
  data() {
    return {
      mainPoster: "",
      topList: [],
      highList: [],
    };
  },
  computed: {
    getPosterImage() {
      return `https://image.tmdb.org/t/p/w1280${this.mainPoster.backdrop_path}`;
      // return `https://image.tmdb.org/t/p/w1280/dqK9Hag1054tghRQSqLSfrkvQnA.jpg`
    },
    ...mapGetters(['isLogin']),
    ...mapState(['login_username']),
  },
  components: {
    SearchBar,
    TopListItem,
    HighListItem,
  },
  created() {
    this.getTopList()
    this.getHighList()

    if (this.isLogin) {
      // console.log(this.isLogin)
      this.$store.dispatch('profile', this.login_username)
      this.$store.dispatch('getMyLikeMovies')
    }

    // this.getLikeMovies()
    // this.getArticles()
    // this.getUsers()
  },
  methods: {
    getTopList() {
      axios({
        method: "get",
        url: `${API_URL}/movies/top_rated/`,
      })
        .then((res) => {
          this.topList = res.data;
          // console.log(this.mainPoster)
          // console.log(this.topList)
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getHighList() {
      axios({
        method: "get",
        url: `${API_URL}/movies/popularity/`,
      })
        .then((res) => {
          this.mainPoster =
            res.data[Math.floor(Math.random() * res.data.length)];
          this.highList = res.data;
          // console.log(this.highList)
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // getLikeMovies(){
    //   this.$store.dispatch('getLikeMovies')
    // },
    // getArticles(){
    //   this.$store.dispatch('getArticles')
    // },
    // getUsers(){
    //   this.$store.dispatch('getUsers')
    // },
  },
};
</script>
<style>
.home {
  min-width: 1430px; /* 최소한의 너비로 설정 */
  min-height: min-content; /* 최소한의 높이로 설정 */
  margin: 0 auto; /* 가운데 정렬을 위해 margin을 auto로 설정 */
}
.welcome_text {
  color: white;
  font-size: 100px;
  font-weight: bold;
}
.welcome_content {
  color: white;
  font-size: 60px;
}
.container {
  width: auto;
}
#mainposter {
  width: auto;
  height: 800px;
  border-radius: 20px;
  /* filter: sepia(120%); */
  filter: brightness(50%);
}
#poster {
  /* background-size: 280px 400px; */
  width: 280px;
  height: 400px;
  /* border: 1px solid black; */
  object-fit: cover;
}
#card_div {
  width: auto;
  padding: 40px;
}
.image-container {
  position: relative;
}
.search-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1;
}
.big-text {
  font-size: 60px; /* 원하는 글자 크기로 조정 */
  font-weight: bold;
  color: #6CB7DA;
}
#classification_name h1 {
  /* text-align: left; */
  padding: 20px;
}
</style>