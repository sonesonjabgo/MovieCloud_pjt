<template>
  <div>
    <h1>댓글 작성</h1>
    <form @submit.prevent="createComment">
        <label for="content">내용 : </label>
        <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>

        <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name:'CommentCreateView',
    data(){
        return {
            content: null,
        }
    },
    
    computed:{
        articleid(){
            return this.$route.params.id
        }
    },
    methods: {
        createComment(){
            const content = this.content
            
            if (!content){
                alert('내용 적으소')
                return
            }
            axios({
                method: 'post',
                url: `${API_URL}/articles/${this.articleid}/comment/post/`,
                data: { content, },
                headers: {
                    Authorization: `Token ${this.$store.state.token}`,
                },
            })
            .then(() => {
                // console.log('dsafkafafgilf')
                this.$router.push({name: 'ArticleDetailView', params: { id: this.articleid }} )
            })
            .catch((err) => {
                console.log(err)
            })
        }
    }
}
</script>

<style>

</style>