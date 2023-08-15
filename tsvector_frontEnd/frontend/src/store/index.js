import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null,
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user;
      console.log('User state:', state.user);
    },
  },
  actions: {
    updateToken({ commit }, token) {
      commit('SET_USER', { token });
      
    },
  },
});
