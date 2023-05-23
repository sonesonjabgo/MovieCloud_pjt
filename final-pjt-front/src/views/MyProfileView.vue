<template>
  <div>
    <!-- 내 프로필 보는거 -->
    <h1>profile</h1>
    <div>
        <MyProfile /> <!-- 로그인 한 사람이랑 프로필 페이지 주인이랑 같을 경우 -->
    </div>
    
    <div>
        <!-- 좋아요 누른 영화  내 프로필이든 다른 사람 프로필이든 공통 -->
        <ProfileMovieList />
    </div>

    <div>
        <!-- 누구누구님이 작성한 글 내 프로필이든 다른 사람 프로필이든 공통-->
        <ProfileArticleList />
    </div>

    <div v-if="login_same_profile">
        <!-- 워드클라우드 나만 보이게?-->
        <WordCloud />
    </div>
  </div>
</template>

<script>
import MyProfile from '@/components/MyProfile'
import ProfileMovieList from '@/components/ProfileMovieList'
import ProfileArticleList from '@/components/ProfileArticleList'
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
        ProfileMovieList,
        ProfileArticleList,
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

</style>