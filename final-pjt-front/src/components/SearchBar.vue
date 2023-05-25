<template>
  <div>
    <div class="search">
      <form id="search_form" method="get" @submit.prevent="searchKeyword">
        <input type="hidden">
        <label>
          <input type="text" class="search-input" placeholder="키워드를 입력하세요" v-model="keyword">
        </label>
        <input type="submit" class="search-submit" value="Search">
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'


export default {
    name: 'SearchBar',
    data() {
      return {
        keyword: null,
      }
    },
    methods : {
      searchKeyword() {
        const keyword = this.keyword
        // 검색 결과 페이지에 keyword와 함께 넘어가도록
        // 검색 결과 페이지 생성(created)되면 keyword로 search 함수 실생되도록
        if (!keyword) {
          alert('키워드를 입력해주세요.')
          return
        }
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
    
}
</script>

<style>
.search-input {
  /* border-radius: 20px; */
  width: 600px;
  padding: 10px;
  font-size: 16px;
}
.search-input::placeholder {
  text-align: center; /* 가운데 정렬 */
}
.search-submit {
  padding: 10px;
  font-size: 16px;
}
</style>