<template>
  <div id="profile">
    <!-- 내 프로필 보는거 -->
    <!-- <h1 class="detail_title">Profile</h1> -->
    <div>
        <MyProfile /> <!-- 로그인 한 사람이랑 프로필 페이지 주인이랑 같을 경우 -->
    </div>
    
    <div>
        <!-- 좋아요 누른 영화  내 프로필이든 다른 사람 프로필이든 공통 -->
        <MyProfileMovieList />
    </div>

    <div>
        <!-- 누구누구님이 작성한 글 내 프로필이든 다른 사람 프로필이든 공통-->
        <MyProfileArticleList />
    </div>

    <div>
        <!-- 워드클라우드 나만 보이게?-->
        <WordCloud />
    </div>
  </div>
</template>

<script>
import MyProfile from '@/components/MyProfile'
import MyProfileMovieList from '@/components/MyProfileMovieList'
import MyProfileArticleList from '@/components/MyProfileArticleList'
import WordCloud from '@/components/WordCloud'


export default {
    name:'MyProfileView',
    data(){
        return{
            // login_username: this.$store.state.login_username,
            // profile_username: this.$store.state.profile_username,
        }
    },
    components:{
        MyProfile,
        MyProfileMovieList,
        MyProfileArticleList,
        WordCloud,
        
    },
    // computed:{
    //     login_same_profile(){
    //         return this.$store.getters.login_same
    //     }
    // },
    

}
</script>

<style>
.detail_title {
    text-align: left;
  font-size: 70px;
  font-weight: bold;
}
</style>