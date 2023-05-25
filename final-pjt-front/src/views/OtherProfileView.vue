<template>
  <div>
    <!-- 글 작성자 프로필 보는거 -->
    <div>
        <OthersProfile /> <!-- 로그인 한 사람이랑 프로필 페이지 주인이랑 다를 경우 -->
    </div>
    
    <div>
        <!-- 좋아요 누른 영화  내 프로필이든 다른 사람 프로필이든 공통 -->
        <OtherProfileMovieList />
    </div>

    <div>
        <!-- 누구누구님이 작성한 글 내 프로필이든 다른 사람 프로필이든 공통-->
        <OtherProfileArticleList />
    </div>

    <!-- <div v-if="login_same_profile">
        워드클라우드는 내 프로필에서만 보이게
        <WordCloud />
    </div> -->
  </div>
</template>

<script>
// import MyProfile from '@/components/MyProfile'
import OthersProfile from '@/components/OthersProfile'
import OtherProfileMovieList from '@/components/OtherProfileMovieList'
import OtherProfileArticleList from '@/components/OtherProfileArticleList'
// import WordCloud from '@/components/WordCloud'


export default {
    name:'OtherProfileView',
    data(){
        return{
            // login_username: this.$store.state.login_username,
            // profile_username: this.$store.state.profile_username,
        }
    },
    components:{
        // MyProfile,
        OthersProfile,
        OtherProfileMovieList,
        OtherProfileArticleList,
        // WordCloud,
        
    },
    // computed:{
    //     login_same_profile(){
    //         return this.$store.getters.login_same
    //     }
    // },
    

}
</script>

<style>

</style>