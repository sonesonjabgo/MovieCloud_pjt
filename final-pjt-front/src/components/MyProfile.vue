<template>
  <div>
    <h3>{{username}}님 프로필</h3>
    <p>팔로잉           {{following}}</p>
    <p>팔로워        {{follower}}</p>
    <!-- <p>3    10</p> -->

    <p>비밀번호 수정</p> <!-- 로그인한 사람이랑 프로필 주인 같을때 표시 -->
</div>
</template>


<script>
export default {
    name: 'MyProfileView',
    data(){
        return{
            username: this.$store.state.login_username,
            following: this.$store.state.profile_userfollowing,
            follower: this.$store.state.profile_userfollower,
        }
    },
    created(){
        this.profile()
    },
    methods: {
        profile(){ // 현재 페이지의 user 정보를 state에 profile_user로 다 저장
            const username = this.username
            const following = this.following
            const follower = this.follower

            const payload = {
                username, following, follower
            }

            this.$store.dispatch('profile', payload)
        }
    }

    }
</script>

<style>

</style>