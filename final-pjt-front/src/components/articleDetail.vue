<template>
    <div>
      <h1>Detail</h1>
      <div class="article-item">

        <p class="post-title">제목 : {{ articleDetailData?.title }}</p>
        <div class="post-content">
          {{ articleDetailData?.content }}
        </div>

        <p class="post-meta">작성시간 : {{ articleDetailData?.created_at }}</p>
        <p class="post-meta">수정시간 : {{ articleDetailData?.updated_at }}</p><br>
        
        <hr>

      </div>

      
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
      created () {
        window.scrollTo(0, 0);
      },
      computed:{
        ...mapState({
            articleDetailData : state => state.article_detail_data
        }),
      },
      
  }
  </script>
  
  <style>
  .article-item {
  border: 1px solid #ccc;
  /* margin-bottom: 10px; */
  /* margin-left: 10px;
  margin-right: 10px; */

  padding: 10px;
  width: 70;
}

/* 게시물 제목 */
.post-title {
  font-size: 18px;
  font-weight: bold;
}

/* 내용 글씨
.post-content1 {
  font-size: 10px;
  margin-top: 10px;
  /* margin-bottom: 50px;
} */
/* 게시물 내용 */
.post-content {
  margin-top: 10px;
  margin-bottom: 50px;
}
/* 게시물 작성자 및 날짜 */
.post-meta {
  font-size: 12px;
  color: #888;
}
  </style>