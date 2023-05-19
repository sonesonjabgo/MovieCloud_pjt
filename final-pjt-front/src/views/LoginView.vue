<template>
    <div>
        <h1>Login</h1>
        <form action="">
            <label for="username">USERNAME : </label>
            <input type="text" id="username" v-model="username"><br><br>

            <label for="password">PASSWORD : </label>
            <input type="text" id="password" v-model="password"><br><br>

            <label for="first_name">FIRST NAME : </label>
            <input type="text" id="first_name" v-model="first_name"><br><br>

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
            first_name: null,
        }
    }
}
</script>

<style>

</style>