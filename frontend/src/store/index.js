import {createStore} from 'vuex'
import auth from "@/store/auth";
import dividend from "@/store/dividend";

export default createStore({
  state: {
    error: null,
    message: null
  },
  getters: {
    error: s => s.error,
    message: s => s.message
  },
  mutations: {
    setError(state, error) {
      state.error = error
    },
    setMessage(state, message) {
      state.message = message
    },
    clearError(state) {
      state.error = null
    },
    clearMessage(state) {
      state.message = null
    }
  },
  actions: {},
  modules: {
    auth, dividend
  }
})
