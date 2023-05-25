<template>
  <div id="app">
    <nav :class="{ 'nav-fixed': isNavFixed, 'nav-hidden': isNavHidden }">
      <div class="nav_content">
        <div class="sub_media">
        <router-link to="/" class="left-link"
          ><img src="./assets/movieCloud_logo.png" alt=""
        /></router-link>
        <div v-if="isLogin" class="right-links">
          <!-- login 했으면 profile, logout만 -->
          <router-link to="/article">Community</router-link> <br />
          <router-link to="/logout">Logout</router-link> <br />
          <router-link to="/myprofile">Profile</router-link> <br />
        </div>
        <div v-if="!isLogin" class="right-links">
          <!-- login 안 했으면 login, signup만 -->
          <router-link to="/login">Login</router-link> <br />
          <router-link to="/signup">Signup</router-link> <br />
        </div>
        </div>
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
    window.addEventListener("scroll", this.handleScroll);
    window.addEventListener("scroll", this.handleScroll);
    // 초기에 페이지 로드될 때 높이를 조정
    // this.adjustRouterViewHeight();
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin; // 로그인 여부
    },
  },
  methods: {
    // adjustRouterViewHeight() {
    //   const routerViewBg = document.getElementById("router-view-bg");
    //   routerViewBg.style.height = `${document.documentElement.scrollHeight}px`;
    // },
    handleScroll() {
      const scrollTop =
        window.pageYOffset || document.documentElement.scrollTop;
      const threshold = 1; // 스크롤 위치가 200px 이상일 때 네비게이션 사라짐

      this.isNavFixed = scrollTop >= threshold;
      this.isNavHidden = scrollTop >= threshold;
      // this.adjustRouterViewHeight();
    },
  },
};
</script>

<style>
img {
  width: 200px; /* 이미지 크기를 원하는 대로 조정해주세요 */
  height: auto;
  margin-right: 10px; /* 이미지와 텍스트 사이 간격을 조정해주세요 */
}
#to_margin {
  margin-left: 60px;
  margin-right: 60px;
}
#router-view-bg {
  background-color: #fffffd;
  width: 1423px;
  margin-left: auto;
  margin-right: auto;
  /* height: 1850px; */
}
#app {
  font-family: 'Montserrat', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;

  color: #2c3e50;
}
.nav_content{
  width: 100%;
    display: flex;
    justify-content: center;
}
.sub_media{
  display: flex;
    justify-content: space-between;
    position: relative;
    top: 0;
    left: 0;
    width: 100%;
    max-width: 1422px;
    padding: 0 40px;
}
.nav-fixed {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: #61a2da;
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
  background-color: #61a2da;
}
.left-link {
  /* display: flex; */
    justify-content: flex-start;
    /* flex-wrap: nowrap;
    align-items: center;
    overflow: visible; */
}
.right-links {
  display: flex;
  justify-content: flex-end;
  flex-wrap: nowrap;
    /* align-items: center; */
    overflow: visible;
}
nav a {
  margin-right: 10px;
  font-size: 30px;
  font-weight: bold;
  color: #fffffd;
  text-decoration: none;
}
nav a.router-link-exact-active {
  color: #F3A20D;
}
</style>
