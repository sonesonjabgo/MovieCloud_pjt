<template>
    <div>
        <h1>Login</h1>
        <form @submit.prevent="login">
            <label for="username">USERNAME : </label>
            <input type="text" id="username" v-model="username"><br>

            <label for="password">PASSWORD : </label>
            <input type="text" id="password" v-model="password"><br><br>

            <!-- <label for="first_name">FIRST NAME : </label>
            <input type="text" id="first_name" v-model="first_name"><br><br> -->

            <input type="submit" value="LOGIN">
        </form>
    </div>
  
</template>

<script>
export default {
    name: 'LogInview',
    data(){
        return{
            username: null,
            password: null,
            // first_name: null,
        }
    },
    methods:{
        login(){
            const username = this.username
            const password = this.password

            const payload = {
                username, password
            }

            this.$store.dispatch('login', payload)
        }
    }
}
</script>

<style>

</style>