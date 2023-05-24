<template>
    <div>
      <h1>Detail</h1>
      <p>글 번호 : {{ articleDetailData?.id }}</p>
      <p>제목 : {{ articleDetailData?.title }}</p>
      <p>내용 : {{ articleDetailData?.content }}</p>
      <p>작성시간 : {{ articleDetailData?.created_at }}</p>
      <p>수정시간 : {{ articleDetailData?.updated_at }}</p><br>
      <!-- <p @click="go_myprofile" v-if="this.$store.getters.login_same">작성자 본인임: {{ article?.user }}</p>
      <p @click="go_otherprofile" v-if="!this.$store.getters.login_same">작성자 타인임: {{ article?.user }}</p> -->
      <hr>
      <!-- 댓글 작성할 수 있는 버튼 만들어주기 -->
      
  
      <!-- 댓글들 보여주기 -->
      
    </div>
</template>
  
<script>
//   import axios from 'axios'
  import { mapState } from "vuex";
//   const API_URL = 'http://127.0.0.1:8000'
  
  export default {
      name: 'articleDetail',
      data(){
          return {
            //   article: null,
            //   writer: null,
          }
      },
    //   created(){
    //       this.getArticleDetail()
    //   },
      computed:{
        ...mapState({
            articleDetailData : state => state.article_detail_data
        }),
      },
      
  }
  </script>
  
  <style>
  
  </style>