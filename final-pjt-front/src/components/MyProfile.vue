<template>
  <div>
    <h3>{{username}}님 프로필</h3>
    <p>팔로잉 : {{following}}</p>
    <p>팔로워 : {{follower}}</p>
    <!-- <p>3    10</p> -->

</div>
</template>


<script>
import { mapState } from "vuex";

export default {
    name: 'MyProfileView',
    data(){
        return{
            username: this.$store.state.login_username,
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
    },
    computed:{
        ...mapState({
            following : state => state.profile_userfollowing,
            follower : state => state.profile_userfollower,
        }),
        
    },
    // watch: {
    //     following (newData) {
    //         //following -> msg 데이터가 변경될 때 실행
    //         this.profile(newData.following)
    //     },
    //     follower (newData) {
    //         //following -> msg 데이터가 변경될 때 실행
    //         this.profile(newData.follower)
    //     },
    // }
}
</script>

<style>

</style>