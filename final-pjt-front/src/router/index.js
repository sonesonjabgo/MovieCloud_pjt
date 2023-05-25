import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
// import AboutView from '../views/AboutView.vue'
import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ArticleView from '@/views/ArticleView.vue'
import ArticleCreateView from '@/views/CreateArticleView.vue'
import CommentCreateView from '@/views/CreateCommentView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import MyProfileView from '@/views/MyProfileView.vue'
import OtherProfileView from '@/views/OtherProfileView.vue'
import SearchListView from '@/views/SearchListView.vue'

import movieDetail from '../components/movieDetail.vue'
import articleDetail from '../components/articleDetail.vue'

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
  {
    path: '/articleDetail',
    name: 'articleDetail',
    component: articleDetail
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
    path: '/logout',
    name: 'LogOutView',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/myprofile',
    name: 'MyProfileView',
    component: MyProfileView
  },
  {
    path: '/otherprofile',
    name: 'OtherProfileView',
    component: OtherProfileView
  },
  {
    path: '/article',
    name: 'ArticleView',
    component: ArticleView
  },
  {
    path: '/createarticle',
    name: 'ArticleCreateView',
    component: ArticleCreateView
  },
  {
    path: '/createcomment/:id',
    name: 'CommentCreateView',
    component: CommentCreateView
  },
  {
    path: '/detailarticle/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView
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

// router.beforeEach((to,from,next)=>{
//   console.log(to.name)
//   console.log(from.name)
//   if(to.name !== from.name){
//     next()
//   }
// })

export default router
