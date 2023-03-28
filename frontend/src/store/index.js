import {createStore} from 'vuex'
import auth from "@/store/auth";
import dividend from "@/store/dividend";
import account from "@/store/account";
import company from "@/store/company";
import report from "@/store/report";
import router from "@/router";
import errorMessageExtractor from "@/utils/errorMessageExtractor";

import ky from "ky";

const currency = ky.create({prefixUrl: process.env.VUE_APP_PATH_SUFFIX + 'api/v1/'})

export default createStore({
  state: {
    error: null,
    message: null,
    currencies: []
  },
  getters: {
    error: s => s.error,
    message: s => s.message,
    currencies: s=>s.currencies
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
    },
    setCurrencies(state, payload) {
      state.currencies = payload
    }
  },
  actions: {
    async fetchCurrencies({commit}) {
      try {
        const res = await currency('currencies/').json()
        commit('setCurrencies', res)
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
  },
  modules: {
    auth, dividend, account, company, report
  }
})
