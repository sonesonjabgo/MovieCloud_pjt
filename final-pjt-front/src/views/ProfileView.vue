<template>
  <div>
    <h1>profile</h1>
    <div v-if="login_same_profile">
        <MyProfile /> <!-- 로그인 한 사람이랑 프로필 페이지 주인이랑 같을 경우 -->
    </div>

    <div v-if="login_same_profile">
        <OthersProfile /> <!-- 로그인 한 사람이랑 프로필 페이지 주인이랑 다를 경우 -->
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
import OthersProfile from '@/components/OthersProfile'
import ProfileMovieList from '@/components/ProfileMovieList'
import ProfileArticleList from '@/components/ProfileArticleList'
import WordCloud from '@/components/WordCloud'


export default {
    name:'ProfileView',
    data(){
        return{
            login_username: this.$store.state.login_username,
            profile_username: this.$store.state.profile_username,
        }
    },
    components:{
        MyProfile,
        OthersProfile,
        ProfileMovieList,
        ProfileArticleList,
        WordCloud,
        
    },
    computed:{
        login_same_profile(){
            return this.$store.getters.login_same
        }
    },
    // created(){
    //     this.profile()
    // },
    // methods: {
    //     profile(){ // 현재 페이지의 user 정보를 state에 profile_user로 다 저장
    //         const username = this.username
    //         const following = this.following
    //         const follower = this.follower

    //         const payload = {
    //             username, following, follower
    //         }

    //         this.$store.dispatch('profile', payload)
    //     }
    // }

}
</script>

<style>

</style>