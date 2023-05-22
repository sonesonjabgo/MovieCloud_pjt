<template>
    <div>
        <h1>Logout</h1>
        <h3>{{username}}님 로그아웃 하시겠습니까?</h3>
        <!-- <form @submit.prevent="logout">
            <input type="submit" value="LOGOUT">
        </form> -->
    </div>
  
</template>

<script>
export default {
    name: 'LogOutview',
    data(){
        return{
            username: this.$store.state.login_username,
            // token: this.$store.state.token,
            // first_name: null,
        }
    },
    // methods:{
    //     logout(){
    //       console.log(localStorage.getItem('token'))
    //       localStorage.removeItem('vuex')
    //       this.$router.push('/')
    //     }
    // }
}
</script>

<style>

</style>