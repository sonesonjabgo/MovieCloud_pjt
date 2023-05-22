import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router' // store/index.js 에서는 $router 접근 불가 -> import 해야 됨

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    token: null,
    movies: [],
    users: [],
    login_username: null,
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
    }
  },
  mutations: {
    // signup, login 완료하면 토큰 발급, login한 username 저장
    SAVE_TOKEN(state, dataArray) {
      state.token = dataArray[0]
      state.login_username = dataArray[1]
      state.profile_username = dataArray[1]
      router.push({ name: 'home' })
    },
    GET_USERS(state, users) {
      state.users = users
    },
    SET_PROFILE(state, userdata) { // 현재 프로필 페이지의 user 정보 저장 (내가 내 프로필 볼 경우 대비)
      console.log(userdata)
      state.profile_userid = userdata.id
      state.profile_username = userdata.name
      state.profile_userfollower = userdata.follower_count
      state.profile_userfollowing = userdata.following_count

    },
    // GET_PROFILE(state, filteredUsers){
    //   state.profile_userid = filteredUsers.id
    //   state.profile_username = filteredUsers.username
    //   state.profile_userfollower = filteredUsers.follower_count
    //   state.profile_userfollowing = filteredUsers.following_count
    // },
    SEARCH_KEYWORD(state, data) {
      state.searchlist = data
      // console.log(data)
    },
    PICK_MOVIE(state, data) {
      state.movie_detail_data = data
      router.push({ name: 'movieDetail' })
    }
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
          context.commit('SAVE_TOKEN', res.data.key)
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
          context.commit('SAVE_TOKEN', [res.data.key, username])
          // context.commit('GET_LOGIN_USER', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getUsers(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/users/`,
      })
        .then((res) => {
          // console.log(res, context)
          context.commit('GET_USERS', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // getProfileMovie(context){
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/movies/list/`
    //   })
    //     .then((res) => {
    //       context.commit('GET_PROFILE_MOVIE', res.data)
    //     })
    //     .cathch((err) => {
    //       console.log(err)          
    //     })
    // }
    profile(context, payload) { // 내가 내 프로필 볼때 받아올 프로필 정보
      const username = payload.username

      axios({
        method: 'get',
        url: `${API_URL}/accounts/${username}/`,
      })
        .then((res) => {
          // console.log(res.data)
          context.commit('SET_PROFILE', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    get_profile(context, payload) { // 다른 사람 프로필 볼때 받아올 프로필 정보
      const username = payload.username

      const filteredUsers = this.$store.state.users.filter(user => user.username === username)
      this.commit('SET_PROFILE', filteredUsers)
    },
    searchKeyword(context, data) {
      context.commit('SEARCH_KEYWORD', data)
    },
    pickedMovie(context, movie_id) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${movie_id}`,
      })
      .then((res)=>{
        context.commit('PICK_MOVIE', res.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
  },
  modules: {
  }
})
