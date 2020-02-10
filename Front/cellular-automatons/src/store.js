import Vuex from 'vuex'
import Vue from 'vue'
Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
      page : 0
    },
    mutations: {
      changePage(state, nbPage){
        state.page = nbPage
      }
    },
    getters:{
      page: (state) => state.page
    },
    actions:{
      changePage({commit}, nbPage){
        commit('changePage', nbPage)
      }
    }
  })