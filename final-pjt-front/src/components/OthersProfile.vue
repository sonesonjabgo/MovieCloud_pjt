<template>
    <div>
      <h3>{{username}}님 프로필</h3>
      <p>팔로잉           {{following}}</p>
      <p>팔로워        {{follower}}</p>
      <!-- <p>3    10</p> -->
  
      <button @click="follow" v-if="this.isFollowing">언팔로우</button>
      <button @click="follow" v-else>팔로우</button>
    </div>
</template>
  
<script>
import { mapGetters, mapState } from "vuex";

export default {
    name: 'OthersProfileView',
    data(){
        return{
            // username: this.$router.params.username, // url에 적히는 username 가져올거임
            username: this.$store.state.profile_username,
            userid: this.$store.state.profile_userid,
        }
    },
    created(){
        this.profile()
    },
    computed:{
        // isfollowing(){
        //     return this.$store.getters.isFollowing
        // },
        ...mapState({
            following : state => state.profile_userfollowing,
            follower : state => state.profile_userfollower,

        }),
        ...mapGetters(['isFollowing'])
    },
    methods: {
        profile(){ // 현재 페이지의 user 정보를 state에 profile_user로 다 저장
            const username = this.username
  
            const payload = {
                username, 
            }
  
            this.$store.dispatch('get_profile', payload)
            this.$store.dispatch('getMyLikeMovies')
        },
        follow(){
            const userid = this.userid
            const username = this.$store.state.login_username
            const payload = {
                userid, username
            }

            this.$store.dispatch('follow', payload)
        }
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
    // },
}

  </script>
  
  <style>
  
  </style>