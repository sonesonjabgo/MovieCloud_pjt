<template>
    <div class="login-container">
        <div class="login-form">    
            <h1>Login</h1>
            <form @submit.prevent="login" >
                <label for="username"></label>
                <input type="text" id="username" v-model="username" placeholder="Username"><br>

                <label for="password"></label>
                <input type="password" id="password" v-model="password" placeholder="Password"><br><br>

                <!-- <label for="first_name">FIRST NAME : </label>
                <input type="text" id="first_name" v-model="first_name"><br><br> -->

                <input type="submit" value="LOGIN" id="button">
            </form>
        </div>
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
            // this.$store.dispatch('profile', payload)
            // this.getUserDetail(username)

        },
        // getUserDetail(username) {
        //     axios({
        //         method: 'get',
        //         url: `${API_URL}/accounts/${username}/`,
        //     })
        //     .then((res) => {
        //         console.log(res)
        //         console.log('----------------')
        //         const username = res.data.username
        //         const userid = res.data.id
        //         const following = res.data.following_count
        //         const follower = res.data.follower_count
        //         const following_list = res.data.followeings
        //         const payload = {
        //             username, userid, following, follower, following_list
        //         }

        //         this.$store.dispatch('profile', payload)
        //     })
        //     .catch((err) => {
        //         console.log(err)
        //     })
        // },
    }
}
</script>

<style>
.login-container {
  /* width: 500px; */
  display: flex;
  justify-content: center;
  /* align-items: center; */
  height: 370px;
}

.login-form {
  width: 700px;
  padding: 20px;
  margin-top: 20px;
  margin-bottom: 20px;
  background: #f2f2f2;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.login-form h1 {
  text-align: center;
  margin-bottom: 20px;
}

.login-form input {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

.login-form #button {
  width: 100%;
  padding: 10px;
  background: #61A2DA;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.login-form #button:hover {
  background: #4c7eaa;
}
</style>