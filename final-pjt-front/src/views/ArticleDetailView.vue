<template>
  <div>
    <h1>Detail</h1>
    <div class="article-item">
        <!-- <p>글 번호 : {{ article?.id }}</p> -->
        <p class="post-title">제목 : {{ article?.title }}</p>
        <!-- <p class="post-content1">내용 : </p> -->
        <div class="post-content">
            {{ article?.content }}
        </div>
        <p class="post-meta">작성시간 : {{ article?.created_at }}</p>
        <p class="post-meta">수정시간 : {{ article?.updated_at }}</p><br>
        <p @click="go_myprofile" v-if="this.$store.getters.login_same">{{ article?.user }} 씀</p>
        <p @click="go_otherprofile" v-if="!this.$store.getters.login_same">{{ article?.user }} 씀</p>
        <hr>
    </div>
    <!-- 댓글 작성할 수 있는 버튼 만들어주기 -->
    

    <!-- 댓글들 보여주기 -->
    <div class="article-item1">
        <p>댓글</p>
        <router-link :to="{ name: 'CommentCreateView', params: { id: article.id } }">[댓글 작성]</router-link>
        <CommentListItem 
        v-for="comment in comments" :key="comment.id" :comment="comment" class="article-list"
        />
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import CommentListItem from '@/components/CommentListItem'

export default {
    name: 'ArticleDetailView',
    data(){
        return {
            article: null,
            writer: null,
            comments: null,
        }
    },
    created(){
        this.getArticleDetail()
    },
    components: {
        CommentListItem,
    },
    computed:{
        articleid() {
            return this.$route.params.id
        }
    },
    methods: {
        getArticleDetail(){
            axios({
                method: 'get',
                url: `${API_URL}/articles/${ this.$route.params.id }/`,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                },
            })
            .then((res) => {
                // console.log(res)
                this.article = res.data
                this.getUserDetail(this.article.user)
                this.$store.dispatch('get_profile', this.article.user)
                this.getCommentList(this.article.id)
                this.$store.dispatch('getOtherLikeMovies')
                // console.log('-------------------------')
                // console.log(this.article.id)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        getUserDetail(userid) {
            axios({
                method: 'get',
                url: `${API_URL}/accounts/${userid}/info/`,
            })
            .then((res) => {
                // console.log(res)
                this.article.user = res.data.username
                this.writer = res.data.username
            })
            .catch((err) => {
                console.log(err)
            })
        },
        go_myprofile() { // 작성자 누르면 프로필로 넘어갈거
            this.$router.push({name: 'MyProfileView'})
        },
        go_otherprofile() { // 작성자 누르면 프로필로 넘어갈거
            this.$router.push({name: 'OtherProfileView'})
        },
        getCommentList(article_pk){
            axios({
                method: 'get',
                url: `${API_URL}/articles/${article_pk}/comment/`,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                },
            })
            .then((res) => {
                // console.log('-------------------------')
                // console.log(res.data)
                this.comments = res.data
                // this.$store.dispatch('get_comment', this.article.id)
            })
            .catch((err) => {
                console.log(err)
            })
        },
    }
}
</script>

<style>
/* 게시물 항목 */
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
.article-item {
  border: 1px solid #ccc;
  /* margin-bottom: 10px; */
  /* margin-left: 10px;
  margin-right: 10px; */

  padding: 10px;
  width: 70;
}
.article-item1 {
  border: 1px solid #ccc;
  margin-top: 20px;
  /* margin-left: 10px;
  margin-right: 10px; */

  padding: 10px;
  width: 70;
}

</style>