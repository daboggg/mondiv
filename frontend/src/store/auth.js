import ky from "ky";
import errorMessageExtractor from "@/utils/errorMessageExtractor";
import router from "@/router";

const auth = ky.create({prefixUrl: process.env.VUE_APP_PATH_SUFFIX + 'auth/'})

export default {
  state: {
    username: null,
    token: null
  },
  getters: {
    token: s => s.token
  },
  mutations: {
    login(state, {token, username}) {
      state.username = username
      state.token = token
      sessionStorage.setItem('username', username)
      sessionStorage.setItem('token', token)
    },
    logout(state) {
      state.token = null
      state.username = null
      sessionStorage.removeItem('token')
      sessionStorage.removeItem('username')
    }
  },
  actions: {
    async login({commit}, formData) {
      try {
        const res = await auth.post('token/login', {json: formData}).json();
        commit('login',{token:res.auth_token, username:formData.username})
        commit('setMessage', `Добро пожаловать, ${formData.username}`)
        router.push('/')
      } catch (error) {
        if (error.name === 'HTTPError') {
          const errorJson = await error.response.json();
          commit('setError', errorMessageExtractor(errorJson))
          throw error
        }
      }
    },
    async logout({commit, getters}) {
      try {
        await auth.post('token/logout', {
          headers: {
            Authorization: `Token ${getters.token}`
          }
        })
        commit('logout')
      } catch (error){
        if (error.name === 'HTTPError') {
          const errorJson = await error.response.json();
          commit('setError', errorMessageExtractor(errorJson))
          throw error
        }
      }
    }
  }
}