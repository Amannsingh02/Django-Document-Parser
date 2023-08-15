import Vue from 'vue'
import VueRouter from 'vue-router';
import Vuex from 'vuex';
import HomePage from '../views/HomePage.vue';
import RegisterUser from '../views/RegisterUser.vue'
import UserLogin from '../views/UserLogin'

Vue.use(VueRouter);
Vue.use(Vuex);

const routes = [
  {
    path: '/',
    name: 'register',
    component: RegisterUser
  },
  {
    path: '/login',
    name: 'login',
    component: UserLogin
  },
  {
    path: '/home',
    name: 'home',
    component: HomePage
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
