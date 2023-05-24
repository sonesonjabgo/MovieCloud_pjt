<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p><br>
    <p @click="go_myprofile" v-if="this.$store.getters.login_same">작성자 본인임: {{ article?.user }}</p>
    <p @click="go_otherprofile" v-if="!this.$store.getters.login_same">작성자 타인임: {{ article?.user }}</p>
    <hr>
    <!-- 댓글 작성할 수 있는 버튼 만들어주기 -->
    

    <!-- 댓글들 보여주기 -->
    
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ArticleDetailView',
    data(){
        return {
            article: null,
            writer: null,
        }
    },
    created(){
        this.getArticleDetail()
    },
    // computed:{
    //     profi() {
    //         return this.article.user
    //     }
    // },
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
                console.log(res)
                this.article = res.data
                this.getUserDetail(this.article.user)
                this.$store.dispatch('get_profile', this.article.user)
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
        // get_writer_profile(){
        //     const userid = this.article.id
        //     const payload = {
        //         userid
        //     }

        //     this.$store.dispatch('get_profile', payload)
        //     // this.getUserDetail(username)

        // },
    }
}
</script>

<style>

</style>