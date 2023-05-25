<template>
  <div>
    <h1>워드 클라우드로 영화 추천받기</h1>
    <p>워드 클라우드는 좋아하는 영화를 기반으로 생성됩니다.</p>
    <p>좋아하는 영화를 많이 추가하세요</p>
    <div>
      <div id="chart"></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import anychart from "anychart";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "WordCloud",
  data() {
    return {
      movies: this.$store.state.like_my_movies,
    };
  },
  methods: {
    get_wordcloud() {
      const overviews = this.like_movies_overview;
      axios({
        method: "post",
        url: `${API_URL}/movies/moviecloud/`,
        data: { overviews },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          // console.log(res.data['result'])
          this.drawChart(res.data['result'])
        })
        .catch();
    },
    drawChart(input) {
      anychart.onDocumentReady(() => {
        // console.log(input)
        const data = input;
        const chart = anychart.tagCloud(data); // Use tagCloud chart type
        chart.container('chart');

        chart.listen('pointClick', (e) => {
          const word = e.point.get('x'); // 클릭한 단어 가져오기
          // 클릭한 단어로 원하는 동작 수행
          this.searchKeyword(word)
        });
        chart.draw();
      });
    },
    searchKeyword(keyword) {
        axios({
          method: 'get',
          url: `${API_URL}/movies/search/${keyword}/`,
        })
        .then((res)=>{
          this.$store.dispatch('searchKeyword', res.data)
          if(this.$route.path !== this.$router.resolve({name: 'SearchListView'}).href){
            this.$router.push({name: 'SearchListView'})
          }
        })
        .catch((err)=>{
          console.log(err)
        })
      }
  },
  computed: {
    like_movies_overview() {
      let my_overview = this.movies.map(function (el) {
        return el.overview;
      });
      return my_overview;
    },
  },
  watch : {
    movies : {
      deep : true,
      handler(){
        this.get_wordcloud()
      }
    }
  },
  created() {
    this.get_wordcloud();
  },
};
</script>

<style>
#chart {
  height: 300px;
}
</style>