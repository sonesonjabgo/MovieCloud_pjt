<template>
    <div class="logout-container">
        <div class="logout-form">
            <h1>Logout</h1>
            <h3>{{username}}님 로그아웃 하시겠습니까?</h3>
            <form @submit.prevent="logout">
                <input type="submit" value="LOGOUT" id="button">
            </form>
        </div>
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
.logout-container {
  /* width: 500px; */
  display: flex;
  justify-content: center;
  /* align-items: center; */
  height: 370px;
}

.logout-form {
  width: 700px;
  padding: 20px;
  margin-top: 20px;
  margin-bottom: 20px;
  background: #f2f2f2;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.logout-form h1 {
  text-align: center;
  margin-bottom: 20px;
}
.logout-form h3 {
  text-align: center;
  margin-bottom: 20px;
}

/* .login-form input {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 4px;
  border: 1px solid #ccc;
} */

.logout-form #button {
  width: 70%;
  padding: 10px;
  background: #61A2DA;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 10px;
}

.logout-form #button:hover {
  background: #4c7eaa;
}
</style>