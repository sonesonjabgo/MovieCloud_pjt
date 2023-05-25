<template>
  <div>
    <div id="myProfile">
      <h1 id="detail_title">{{ username }}님 프로필</h1>
      <div id="follow_div">
        <div id="following_div">
          <p>팔로잉</p>
          <p id="following">{{ following }}</p>
        </div>
        <div id="follower_div">
          <p>팔로워</p>
          <p id="follower">{{ follower }}</p>
        </div>
      </div>
      <button @click="follow" v-if="this.isFollowing">언팔로우</button>
      <button @click="follow" v-else>팔로우</button>
    </div>
  </div>
</template>
  
<script>
import { mapGetters, mapState } from "vuex";

export default {
  name: "OthersProfileView",
  data() {
    return {
      // username: this.$router.params.username, // url에 적히는 username 가져올거임
      username: this.$store.state.profile_username,
      userid: this.$store.state.profile_userid,
    };
  },
  created() {
    this.profile();
  },
  computed: {
    // isfollowing(){
    //     return this.$store.getters.isFollowing
    // },
    ...mapState({
      following: (state) => state.profile_userfollowing,
      follower: (state) => state.profile_userfollower,
    }),
    ...mapGetters(["isFollowing"]),
  },
  methods: {
    profile() {
      // 현재 페이지의 user 정보를 state에 profile_user로 다 저장
      const username = this.username;

      const payload = {
        username,
      };

      this.$store.dispatch("get_profile", payload);
      this.$store.dispatch("getMyLikeMovies");
    },
    follow() {
      const userid = this.userid;
      const username = this.$store.state.login_username;
      const payload = {
        userid,
        username,
      };

      this.$store.dispatch("follow", payload);
    },
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
};
</script>
  
<style>
#myProfile {
  width: 100%;
  display: flex;
  /* justify-content: center; */
}
#detail_title {
  width: fit-content;
  text-align: left;
  font-size: 70px;
  font-weight: bold;
}
div p {
  font-size: 20px;
}
#follow_div {
  display: flex;
  margin-top: 12px;
  /* justify-content: flex-end; */
}
#following_div {
  margin-right: 8px;
}
</style>