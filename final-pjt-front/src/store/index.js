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
    searchlist: null,
  },
  getters: {
  },
  mutations: {
    // signup, login 완료하면 토큰 발급
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name:'home'})
    },
    SEARCH_KEYWORD(state, data) {
      state.searchlist = data
      console.log(data)
    }
  },
  actions: {
    signUp(context, payload){
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
    login(context, payload){
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
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    searchKeyword(context, data){
      context.commit('SEARCH_KEYWORD', data)
    }
  },
  modules: {
  }
})
