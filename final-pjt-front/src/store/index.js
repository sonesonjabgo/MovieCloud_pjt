import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router' // store/index.js 에서는 $router 접근 불가 -> import 해야 됨
// import { RouterLink } from 'vue-router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    token: null,
    like_movies: null,
    wrote_articles: [],
    users: [],
    articles: [],
    login_username: null,
    login_userid: null,
    login_userfollower: null,
    login_userfollowing: null,
    login_following_list: null,
    profile_username: null,
    profile_userid: null,
    profile_userfollower: null,
    profile_userfollowing: null,
    searchlist: null,
    movie_detail_data: null,
  },
  getters: {
    login_same(state) {
      return state.login_username == state.profile_username ? true : false
    },
    isLogin(state) {
      return state.token ? true : false
    },
    isFollowing(state) {
      return  state.login_following_list.includes(state.profile_userid) ? true : false
    },
  },
  mutations: {
    // signup, login 완료하면 토큰 발급, login한 username 저장
    // SAVE_TOKEN_1(state, dataArray) { // sign up 했을 때 토큰 저장
    //   console.log(dataArray)
    //   state.token = dataArray

    //   router.push({ name: 'home' })
    // },
    SAVE_TOKEN(state, dataArray) { // login 했을 때 토큰 저장
      console.log(dataArray)
      state.token = dataArray[0]
      state.login_username = dataArray[1]
      // state.profile_username = dataArray[1]
      router.push({ name: 'home' })
    },
    GET_LIKE_MOVIES(state, movies) {
      // console.log(movies)
      // // console.log(state.profile_userid)
      // console.log(movies[0].like_users)
      // const like_movies = movies.filter((element)=>{ element.like_users.includes(state.profile_userid)})
      const like_movies = movies.filter((element) => element.like_users.includes(state.profile_userid));
      // console.log(like_movies)
      state.like_movies = like_movies
    },
    GET_WROTE_ARTICLES(state, articles) {
      const wrote_articles = articles.filter((element)=>{ element.user == state.profile_userid})
      state.wrote_articles = wrote_articles
    },
    DELETE_TOKEN(state) {
      state.token = null
      state.like_movies = null
      state.login_username = null
      state.login_userid = null
      state.login_userfollower = null
      state.login_userfollowing = null
      state.login_following_list = null
      state.profile_username = null
      state.profile_userid = null
      state.profile_userfollower = null
      state.profile_userfollowing = null

      router.push({name: "home"})
    },

    GET_USERS(state, users) {
      state.users = users
    },
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    SET_LOGIN_PROFILE(state, userdata) { // 로그인한 이용자 정보 저장
      console.log(userdata)
      state.login_username = userdata.username
      state.login_userid = userdata.id
      state.login_userfollower = userdata.follower_count
      state.login_userfollowing = userdata.following_count
      state.login_following_list = userdata.followings

    },
    SET_WRITER_PROFILE(state, userdata) { // 현재 프로필 페이지의 user 정보 저장 (내가 내 프로필 볼 경우 대비)
      console.log(userdata)
      state.profile_username = userdata.username
      state.profile_userid = userdata.id
      state.profile_userfollower = userdata.follower_count
      state.profile_userfollowing = userdata.following_count
      // state.login_following_list = userdata.followings

    },
    
    // SET_PROFILE(state, userdata) { // 현재 프로필 페이지의 user 정보 저장 (내가 내 프로필 볼 경우 대비)
    //   console.log(userdata)
    //   state.profile_userid = userdata.id
    //   state.profile_username = userdata.username
    //   state.profile_userfollower = userdata.follower_count
    //   state.profile_userfollowing = userdata.following_count

    // },
    SEARCH_KEYWORD(state, data) {
      state.searchlist = data
      // console.log(data)
    },
    PICK_MOVIE(state, data) {
      state.movie_detail_data = data
      
    },
    FOLLOW(state, data) {
      state.profile_userfollower = data.follower_count
      state.profile_userfollowing = data.following_count
      state.profile_following_list = data.followings
    },
  },
  actions: {
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {

          context.commit('SAVE_TOKEN', [res.data.key, username])
        })
        .catch((err) => {
          console.log(err)
        })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
          console.log(res)
          console.log('--------------------------------')
          console.log(res.data)
          context.commit('SAVE_TOKEN', [res.data.key, username])
          // context.commit('GET_LOGIN_USER', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    logout(context) {
      axios({
        method: "post",
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
      })
      .then(()=>{
        context.commit('DELETE_TOKEN')
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getLikeMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/list/`,
      })
        .then((res) => {
          // console.log(res.data[400])
          context.commit('GET_LIKE_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getWroteArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/articles/list/`,
      })
        .then((res) => {
          console.log(res)
          context.commit('GET_WROTE_ARTICLES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // getUsers(context) {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/accounts/users/`,
    //   })
    //     .then((res) => {
    //       // console.log(res, context)
    //       context.commit('GET_USERS', res.data)
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
    // },
    getArticles(context) { // community에 articles를 보여주기 위한
      axios({
        method: 'get',
        url: `${API_URL}/articles/list/`,
      })
        .then((res) => {
          // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    profile(context, payload) { // 로그인한 사용자 정보 받아오기
      const username = payload.username

      axios({
        method: 'get',
        url: `${API_URL}/accounts/${username}/`,
      })
        .then((res) => {
          // console.log(res)
          context.commit('SET_LOGIN_PROFILE', res.data)
        })
        .catch((err) => {
          console.log(err)
        })

    },
    get_profile(context, payload) { // 작성자로 들어간 프로필 정보 받아오기
      const userid = payload

      axios({
        method: 'get',
        url: `${API_URL}/accounts/${userid}/info/`,
      })
        .then((res) => {
          console.log(res)
          context.commit('SET_WRITER_PROFILE', res.data)
        })
        .catch((err) => {
          console.log(err)
        })

    },
    // get_profile(context, payload) { // 작성자로 들어간 프로필 정보 받아오기
    //   const username = payload.username

    //   const filteredUsers = this.$store.state.users.filter(user => user.username === username)
    //   this.commit('SET_PROFILE', filteredUsers)
    // },
    searchKeyword(context, data) {
      context.commit('SEARCH_KEYWORD', data)
    },
    pickedMovie(context, movie_id) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${movie_id}`,
      })
        .then((res) => {
          context.commit('PICK_MOVIE', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    follow(context, payload) {
      const userid = payload.userid

      axios({
        method: 'post',
        url: `${API_URL}/${userid}/follow/`,
        data: {
          userid
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res.data)
          context.commit('FOLLOW', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  modules: {
  }
})
