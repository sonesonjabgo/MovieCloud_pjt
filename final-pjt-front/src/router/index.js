import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
// import AboutView from '../views/AboutView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'

import ProfileView from '@/views/ProfileView.vue'
import SearchListView from '@/views/SearchListView.vue'

import movieDetail from '../components/movieDetail.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movieDetail',
    name: 'movieDetail',
    component: movieDetail
  },
  // {
  //   path: '/',
  //   name: 'about',
  //   component: AboutView
  // },
  {
    path: '/login',
    name: 'LogInView',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/searchlist',
    name: 'SearchListView',
    component: SearchListView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
