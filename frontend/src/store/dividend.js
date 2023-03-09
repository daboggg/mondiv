import ky from "ky";
import errorMessageExtractor from "@/utils/errorMessageExtractor";
import router from "@/router";

const dividend = ky.create({prefixUrl: process.env.VUE_APP_PATH_SUFFIX + 'api/v1/'})

export default {
  state: {
    dividends: []
  },
  getters: {
    dividends: s => s.dividends
  },
  mutations: {
    setDividends(state, payload) {
      state.dividends = payload
    }
  },
  actions: {
    async getDividends({commit, getters}) {
      try {
        const res = await dividend('dividends/', {
          headers: {
            Authorization: `Token ${getters.token}`
          }
        }).json()
        commit('setDividends', res)
      }catch (error){
        if (error.message === 'Request failed with status code 401 Unauthorized'){
          commit('logout')
          await router.push('/login')
        }
        if (error.name === 'HTTPError') {
          const errorJson = await error.response.json();
          commit('setError', errorMessageExtractor(errorJson))
          throw error
        }
      }
    }
  }
}