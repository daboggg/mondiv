import ky from "ky";
import errorMessageExtractor from "@/utils/errorMessageExtractor";
import router from "@/router";

const account = ky.create({prefixUrl: process.env.VUE_APP_PATH_SUFFIX + 'api/v1/'})

export default {
  state: {
    accounts: []
  },
  getters: {
    accounts: s => s.accounts
  },
  mutations: {
    setAccounts(state, payload) {
      state.accounts = payload
    },
    removeAccounts(state) {
      state.accounts = []
    }
  },
  actions: {
    async fetchAccounts({commit, getters}) {
      try {
        const res = await account('accounts/', {
          headers: {
            Authorization: `Token ${getters.token}`
          }
        }).json()
        commit('setAccounts', res)
      } catch (error) {
        if (error.message === 'Request failed with status code 401 Unauthorized') {
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