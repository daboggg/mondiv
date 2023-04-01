<template>

  <div class="container p-3 my-3 bg-body">

    <div class="col text-center mt-2 display-6">Добавить компанию</div>

    <!--фарма добавления тикера-->
    <div class="row">
      <div class="col-xs-12 col-md-8 offset-md-2 col-xl-4 offset-xl-4 mt-5">
        <form class="input-group justify-content-center mb-2" @submit.prevent="submitHandler">
          <span class="input-group-text">Тикер</span>
          <input v-model="ticker" class="form-control"/>
          <button type="button" @click="ticker = ''" class="btn btn-light ms-1"><i
              class="bi-x-lg text-danger"></i></button>
          <button class="btn btn-light ms-3 btn-outline-dark" :disabled="adding" type="submit">
            <span v-if="adding" class="adding spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
            {{ adding ? 'Добавление...' : 'Добавить' }}
          </button>
          <div
              class="invalid form-text me-5"
              v-for="e in v$.ticker.$errors"
              :key="e.$uid"
          >{{ e.$message }}
          </div>
        </form>
      </div>
    </div>

    <!--фарма поиска-->
    <div class="row mb-2">
      <div class="col-xs-12 col-md-8 offset-md-2 col-xl-4 offset-xl-4">
        <form class="input-group justify-content-end my-4" @submit.prevent="fetchCompaniesWithPagination">
          <span class="input-group-text">Поиск</span>
          <input @input="currentPage = 1; fetchCompaniesWithPagination()" v-model="search" class="form-control"/>
          <button type="button" @click="search = ''" class="btn btn-light ms-1"><i
              class="bi-x-lg text-danger"></i></button>
          <div
              class="invalid form-text me-5"
              v-for="e in v$.ticker.$errors"
              :key="e.$uid"
          >{{ e.$message }}
          </div>
        </form>
      </div>
    </div>

    <!--  спиннер-->
    <div v-if="loading" class="text-center mt-5">
      <div class="spinner-border mt-5" role="status">
        <span class="visually-hidden">Загрузка...</span>
      </div>
    </div>

    <div v-else>
      <!--    счетчик записей-->
      <h5 class="ms-3 my-3">Записей: <span class="badge bg-secondary">{{ companies.count }}</span></h5>

      <!--  таблица-->
      <div class="row mx-3">
        <div class="col-12">
          <table class="table align-middle">
            <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Лого</th>
              <th scope="col">Тикер</th>
              <th scope="col">Название</th>
              <th scope="col">Подробнее</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(com, index) in companies.results" :key="com.id">
              <th>{{ (index + 1)+(currentPage-1)*pageSize }}</th>
              <td><img class="icon_min img-thumbnail" :src="com.icon_image" alt=""></td>
              <td>{{ com.ticker }}</td>
              <td>{{ com.name }}</td>
              <td>
                <router-link :to="{name:'company', params: { id: com.id }}">
                  <i class="ms-4  bi-box-arrow-in-right fs-3 text-black"></i>
                </router-link>
              </td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="row my-5">
      <!--      выбор количества записей на страницу-->
      <div class="col-6">
        <div class="row justify-content-end">
          <div class="btn-group col-10 align-items-center" role="group"
               aria-label="Выбор количества записей не страницу">
            <div class="input-group-text" id="btnGroupAddon">Показывать по</div>

            <input @change="currentPage = 1; fetchCompaniesWithPagination()" v-model="pageSize" value="10" type="radio"
                   class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked>
            <label class="btn btn-outline-primary" for="btnradio1">10</label>

            <input @change="currentPage = 1; fetchCompaniesWithPagination()" v-model="pageSize" value="20" type="radio"
                   class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
            <label class="btn btn-outline-primary" for="btnradio2">20</label>

            <input @change="currentPage = 1; fetchCompaniesWithPagination()" v-model="pageSize" value="50" type="radio"
                   class="btn-check" name="btnradio" id="btnradio3" autocomplete="off">
            <label class="btn btn-outline-primary" for="btnradio3">50</label>

            <input @change="currentPage = 1; fetchCompaniesWithPagination()" v-model="pageSize" value="100" type="radio"
                   class="btn-check" name="btnradio" id="btnradio4" autocomplete="off">
            <label class="btn btn-outline-primary" for="btnradio4">100</label>
          </div>
        </div>
      </div>
      <!--      пагинатор-->
      <div class="col-6">
        <Vue3BsPaginate
            class="fw-bold"
            :total="companies.count"
            v-model="currentPage"
            :perPage="pageSize"
            :onChange="fetchCompaniesWithPagination"
            alignment="center"
        />
      </div>
    </div>

  </div>
</template>

<script>
import {useVuelidate} from "@vuelidate/core"
import {helpers, required} from "@vuelidate/validators";

export default {
  name: "AddCompany",
  setup() {
    return {
      v$: useVuelidate()
    }
  },
  data: () => ({
    currentPage: 1,
    pageSize: 10,
    search: '',
    ticker: '',
    companies: [],
    loading: true,
    adding: false
  }),
  async mounted() {
    await this.fetchCompaniesWithPagination()
  },
  methods: {
    async fetchCompaniesWithPagination() {
      try {
        this.companies = await this.$store.dispatch('fetchCompaniesWithPagination', {
          page: this.currentPage,
          page_size: this.pageSize,
          search: this.search,
        })
        this.loading = false
      } catch (e) {
        console.log(e)
      }
    },
    async submitHandler() {
      const isFormCorrect = await this.v$.$validate()
      if (!isFormCorrect) return
      this.adding = true
      try {
        await this.$store.dispatch('addCompany', {ticker: this.ticker});
        this.adding = false
        await this.fetchCompaniesWithPagination()

      } catch (e) {
        console.log(e)
      } finally {
        this.ticker = ''
        this.v$.$reset()
      }
    }
  },
  validations() {
    return {
      ticker: {
        required: helpers.withMessage('Поле не может быть пустым', required),
      },
    }
  },
}
</script>

<style scoped>
.adding.spinner-border {
  width: 1rem !important;
  height: 1rem !important;
  border-width: 2px !important;
}

.invalid {
  color: red;
}
</style>