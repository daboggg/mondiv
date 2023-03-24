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
    },
    removeDividends(state) {
      state.dividends = []
    }
  },
  actions: {
    async fetchDividends({commit, getters}, params) {
      try {
        const res = await dividend('dividends/', {
          headers: {
            Authorization: `Token ${getters.token}`
          },
          searchParams: {
            ...params,
            ...router.currentRoute.value.query,
          }
        }).json()
        commit('setDividends', res)
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
    async addDividend({commit, getters}, formData){
      try {
        await dividend.post('dividends/', {
          headers: {
            Authorization: `Token ${getters.token}`
          },
          json: formData
        }).json()
        commit('setMessage', "Дивиденд добавлен")
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
    async deleteDividend({commit, getters}, id) {
      try {
        await dividend.delete(`dividends/${id}/`, {
          headers: {
            Authorization: `Token ${getters.token}`
          }
        })
        commit('setMessage', 'Успешно удалено')
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
    async getDividend({commit, getters}, id) {
      try {
        const res = await dividend(`dividends/${id}/`, {
          headers: {
            Authorization: `Token ${getters.token}`
          }
        }).json()
        return res
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
    async editDividend({commit, getters}, {formData,id}) {
      try {
        await dividend.put(`dividends/${id}/`, {
          headers: {
            Authorization: `Token ${getters.token}`
          },
          json:formData
        })
        commit('setMessage', 'Данные изменены')
        if (router.currentRoute.value.query && router.currentRoute.value.query.r_page) {
          await router.push(`/dividends?r_page=${router.currentRoute.value.query.r_page}`);
        } else {
          await router.push(`/dividends`);
        }
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