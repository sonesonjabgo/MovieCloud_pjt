<template>
  <div id="app">
    <nav :class="{ 'nav-fixed': isNavFixed, 'nav-hidden': isNavHidden }">
      <router-link to="/" class="left-link">Home</router-link>
      <!-- <router-link to="/about">About</router-link> | -->
      <div v-if="isLogin" class="right-links"> <!-- login 했으면 profile, logout만 -->
        <router-link to="/article">Community</router-link> <br />
        <router-link to="/logout">Logout</router-link> <br />
        <router-link to="/myprofile">Profile</router-link> <br />
      </div>
      <div v-if="!isLogin" class="right-links"> <!-- login 안 했으면 login, signup만 -->
        <!-- <router-link to="/article">Community</router-link> <br /> -->
        <router-link to="/login">Login</router-link> <br />
        <router-link to="/signup">Signup</router-link> <br />
      </div>
    </nav>
    <div id="router-view-bg">
    <router-view />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isNavFixed: false,
      isNavHidden: false,
    };
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  methods: {
    handleScroll() {
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      const threshold = 1; // 스크롤 위치가 200px 이상일 때 네비게이션 사라짐

      this.isNavFixed = scrollTop >= threshold;
      this.isNavHidden = scrollTop >= threshold;
    },

  },
};
</script>

<style>
#router-view-bg {
  background-color: #D9D9D9;
  height: 1850px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  
  color: #2c3e50;
}
.nav-fixed {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: #316f9c;
  z-index: 999;
  transition: transform 1.5s ease-out;
}
.nav-hidden {
  transform: translateY(-100%);
}
nav {
  display: flex;
  height: 80px;
  justify-content: space-between;
  align-items: center;
  background-color: #316f9c;
}
.left-link {
  margin-right: auto;
}
.right-links {
  display: flex;
  gap: 10px;
}
nav a {
  font-size: 40px;
  font-weight: bold;
  color: #5d8fd1;
  text-decoration: none;
}
nav a.router-link-exact-active {
  color: rgb(190, 110, 243);
}

</style>
