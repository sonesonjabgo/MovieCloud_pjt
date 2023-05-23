<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p><br>
    <p @click="go_profile">작성자 : {{ article?.user }}</p>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ArticleDetailView',
    data(){
        return {
            article: null
        }
    },
    created(){
        this.getArticleDetail()
    },
    computed:{
        profi() {
            return this.article.user
        }
    },
    methods: {
        getArticleDetail(){
            axios({
                method: 'get',
                url: `${API_URL}/articles/${ this.$route.params.id }/`,
            })
            .then((res) => {
                console.log(res)
                this.article = res.data
                this.getUserDetail(this.article.user)
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
                console.log(res)
                this.article.user = res.data.username
            })
            .catch((err) => {
                console.log(err)
            })
        },
        go_profile() {
            axios({
                method: 'get',
                url: `${API_URL}/accounts/${this.profi}/`,
            })
            .then((res) => {
                console.log(res)
                this.$router.push({path: '/ProfileView}'})
            })
            .catch((err) => {
                console.log(err)
            })
        },
    }
}
</script>

<style>

</style>