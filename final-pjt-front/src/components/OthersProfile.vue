<template>
    <div>
      <h3>{{username}}님 프로필</h3>
      <p>팔로잉           {{following}}</p>
      <p>팔로워        {{follower}}</p>
      <!-- <p>3    10</p> -->
  
      <button @click="follow" v-if="isfollowing">팔로우</button> <!-- 로그인한 사람이랑 프로필 주인 다를때 표시 -->
      <button @click="follow" v-if="!isfollowing">언팔로우</button> <!-- 로그인한 사람이랑 프로필 주인 다를때 표시 -->
  </div>
  </template>
  
  <script>
  import { mapState } from "vuex";

  export default {
    name: 'OthersProfileView',
    data(){
        return{
            username: this.$router.params.username, // url에 적히는 username 가져올거임
            userid: this.$store.state.profile_userid,
        }
    },
    created(){
        this.profile()
    },
    computed:{
        isfollowing(){
            return this.$store.getters.isFollowing
        },
        ...mapState({
            following : state => state.profile_userfollowing,
            follower : state => state.profile_userfollower,
        }),
    },
    methods: {
        profile(){ // 현재 페이지의 user 정보를 state에 profile_user로 다 저장
            const username = this.username
  
            const payload = {
                username, 
            }
  
            this.$store.dispatch('get_profile', payload)
        },
        follow(){
            const userid = this.userid
            const payload = {
                userid,
            }

            this.$store.dispatch('follow', payload)
        }
    },
    watch: {
        following (newData) {
            //following -> msg 데이터가 변경될 때 실행
            this.profile(newData.following)
        },
        follower (newData) {
            //following -> msg 데이터가 변경될 때 실행
            this.profile(newData.follower)
        },
    },
}

  </script>
  
  <style>
  
  </style>