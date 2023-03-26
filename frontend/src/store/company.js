import ky from "ky";
import errorMessageExtractor from "@/utils/errorMessageExtractor";
import router from "@/router";

const company = ky.create({prefixUrl: process.env.VUE_APP_PATH_SUFFIX + 'api/v1/'})

export default {
  state: {
    companies: []
  },
  getters: {
    companies: s => s.companies
  },
  mutations: {
    setCompanies(state, payload) {
      state.companies = payload
    }
  },
  actions: {
    async fetchCompaniesWithPagination({commit}, params) {
      try {
        return  await company('companies_with_pagination/',{
          searchParams:{
            ...params,
            ...router.currentRoute.value.query,
          }
        }).json()
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
    },
    async fetchCompanies({commit}) {
      try {
        const res = await company('companies/').json()
        commit('setCompanies', res)
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
    },
    async addCompany({commit}, ticker) {
      try {
        const res = await company.post('companies/',{
          json: ticker
        }).json()
        const message = res.info.message==='Ticker not found.'?'Тикер не найден':res.info.message
        commit('setMessage', message)
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