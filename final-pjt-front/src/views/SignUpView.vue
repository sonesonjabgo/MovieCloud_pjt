<template>
  <div>
    <h1>Sign Up</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp">
    </form>
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

</style>