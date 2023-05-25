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
    </div>
  </div>
</template>


<script>
import { mapState } from "vuex";

export default {
  name: "MyProfileView",
  data() {
    return {
      username: this.$store.state.login_username,
    };
  },
  computed: {
    ...mapState({
      following: (state) => state.login_userfollowing,
      follower: (state) => state.login_userfollower,
    }),
    ...mapState(["login_username"]),
  },
  created() {
    this.profile();
  },
  methods: {
    profile() {
      // 현재 페이지의 user 정보를 state에 profile_user로 다 저장
      const username = this.username;
      // const following = this.following
      // const follower = this.follower

      // const payload = {
      //     username, following, follower
      // }

      this.$store.dispatch("profile", username);
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
  // }
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