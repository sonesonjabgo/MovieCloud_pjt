<template>
  <div class="signup-container">
    <div class="signup-form">
      <h1>Sign Up</h1>
      <form @submit.prevent="signUp">
        <label for="username"></label>
        <input type="text" id="username" v-model="username" placeholder="Username"><br>

        <label for="password1"></label>
        <input type="password" id="password1" v-model="password1" placeholder="Password"><br>

        <label for="password2"></label>
        <input type="password" id="password2" v-model="password2" placeholder="Password 확인">
        
        <input type="submit" value="SignUp" id="button">
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data(){
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload)
      // this.$store.dispatch('profile', username)
      // this.profile()

    },
    // profile(){ // 현재 페이지의 user 정보를 state에 profile_user로 다 저장
    //         const username = this.username
    //         // const following = this.following
    //         // const follower = this.follower

    //         // const payload = {
    //         //     username, following, follower
    //         // }

    //         this.$store.dispatch('profile', username)
    //     }
  }
}
</script>

<style>
.signup-container {
  /* width: 500px; */
  display: flex;
  justify-content: center;
  /* align-items: center; */
  height: 400px;
}

.signup-form {
  width: 700px;
  height: 400px;
  padding: 20px;
  margin-top: 20px;
  margin-bottom: 20px;
  background: #f2f2f2;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* form{
  height: 400px;
} */

.signup-form h1 {
  text-align: center;
  margin-bottom: 20px;
}

.signup-form input {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

.signup-form #button {
  margin-top: 30px;
  width: 100%;
  padding: 10px;
  background: #61A2DA;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.signup-form #button:hover {
  background: #4c7eaa;
}
</style>