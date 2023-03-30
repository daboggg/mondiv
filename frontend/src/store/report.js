import ky from "ky";
import errorMessageExtractor from "@/utils/errorMessageExtractor";
import router from "@/router";

const report = ky.create({prefixUrl: process.env.VUE_APP_PATH_SUFFIX + 'api/v1/'})

export default {
  state: {

  },
  getters: {
  },
  mutations: {
  },
  actions: {
    async fetchReports({commit,getters}, params) {
      // console.log(params)
      try {
        return  await report('reports/',{
          headers: {
            Authorization: `Token ${getters.token}`
          },
          searchParams:{
            ...params,
            // ...router.currentRoute.value.query,
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
  }
}