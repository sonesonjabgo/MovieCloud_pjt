<template>
    <div>
        <h1>Logout</h1>
        <h3>{{username}}님 로그아웃 하시겠습니까?</h3>
        <form @submit.prevent="logout">
            <input type="submit" value="LOGOUT">
        </form>
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
    methods:{
        logout(){
            this.$store.dispatch('logout')
        }
    }
}
</script>

<style>

</style>