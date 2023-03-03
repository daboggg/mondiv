import ky from "ky";
import errorMessageExtractor from "@/utils/errorMessageExtractor";

const auth = ky.create({prefixUrl: process.env.VUE_APP_PATH_SUFFIX + 'auth/'})

export default {
  state: {
    username: null,
    token: null
  },
  getters: {

  },
  mutations: {
    login(state, {token, username}) {
      state.username = username
      state.token = token
      localStorage.setItem('username', username)
      localStorage.setItem('token', token)
    }
  },
  actions: {
    async login({commit}, formData) {
      try {
        const res = await auth.post('token/login/', {
          json: formData
        }).json();
        commit('login', {username: formData.username, token: res.auth_token})
      } catch (error) {
        if (error.name === 'HTTPError') {
          const errors = await error.response.json();
          commit('setError', errorMessageExtractor(errors))
        }
      }
    }
  }
}