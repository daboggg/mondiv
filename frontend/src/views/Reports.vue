<template>

  <!--  спиннер-->
  <div v-if="loading" class="text-center mt-5">
    <div class="spinner-border mt-5" role="status">
      <span class="visually-hidden">Загрузка...</span>
    </div>
  </div>

  <div v-else class="container p-3 my-3 bg-body">

    <!-- Модальное окно -->
    <div class="modal fade" id="deleteModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
         aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Подтвердите удаление</h5>
            <button @click="idForDelete = null" type="button" class="btn-close" data-bs-dismiss="modal"
                    aria-label="Закрыть"></button>
          </div>
          <div class="modal-body">
            <h3 class="text-danger">Внимание, будьте осторожны, восстановленю не подлежит!</h3>
          </div>
          <div class="modal-footer">
            <button @click="idForDelete = null" type="button" class="btn btn-teal" data-bs-dismiss="modal">Отменить
            </button>
            <button @click="deleteReport" type="button" class="btn btn-danger" data-bs-dismiss="modal">Удалить
            </button>
          </div>
        </div>
      </div>
    </div>


    <div class="col text-center mt-2 display-6">Отчеты</div>

    <!--    выбор по дате-->
    <div class="row">
      <div class="col-md-12 col-xl-8 offset-xl-2">
        <form class=" input-group justify-content-center my-4" @submit.prevent="qParams.page = 1; fetchReports()">

          <span class="input-group-text">С</span>
          <input v-model="qParams.date_start" type="date"
                 class="form-control" min="2019-01-01"
                 :max="moment().format('YYYY-MM-DD')"
                 style="font-weight: bold"
          />
          <button type="button" @click="qParams.date_start = ''; fetchReports()"
                  class="input-group-btn btn btn-light ms-1"><i
              class="bi-x-lg text-danger"></i></button>

          <span class="input-group-text ms-3">По</span>
          <input v-model="qParams.date_end" type="date"
                 class="form-control" min="2019-01-01"
                 :max="moment().format('YYYY-MM-DD')"
                 style="font-weight: bold"

          />
          <button type="button" @click="qParams.date_end = ''; fetchReports()"
                  class="input-group-btn btn btn-light ms-1"><i
              class="bi-x-lg text-danger"></i></button>

          <button class="btn btn-light ms-3 btn-outline-dark" type="submit">Выбрать</button>
        </form>
      </div>
    </div>

    <!--    счетчик записей-->
    <h5 class="ms-3 my-3">Записей: <span class="badge bg-secondary">{{ reports.count }}</span></h5>

    <!--    таблица-->
    <div class="row">
      <div class="col-12">
        <table class="table align-middle">
          <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Счет</th>
            <th scope="col">Валюта</th>
            <th scope="col">Период отчета</th>
            <th scope="col">Сумма</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(report, index) in reports.results" :key="report.id">
            <th>{{ (index + 1) + (qParams.page - 1) * qParams.page_size }}</th>
            <td>{{ report.account.name }}</td>
            <td>{{ report.currency.name }}</td>
            <td>{{ localeDate(report.report_date) }}</td>
            <td>{{ report.amount }}</td>
                        <td>
                          <router-link :to="{ name: 'edit_report', params: { id: report.id }, query: qParams}"><i
                              class="text-black bi-pencil fs-4"></i></router-link>
                        </td>
            <td>
              <router-link to="" @click="idForDelete = report.id" data-bs-toggle="modal" data-bs-target="#deleteModal">
                <i class="bi-x-lg fs-4 text-danger"></i>
              </router-link>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="row my-5">
      <!--      выбор количества записей на страницу-->
      <div class="col-6">
        <div class="row justify-content-end">
          <div class="btn-group col-10 align-items-center" role="group"
               aria-label="Выбор количества записей не страницу">
            <div class="input-group-text" id="btnGroupAddon">Показывать по</div>

            <input @change="qParams.page = 1; fetchReports()" v-model="qParams.page_size" value="10" type="radio"
                   class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked>
            <label class="btn btn-outline-primary" for="btnradio1">10</label>

            <input @change="qParams.page = 1; fetchReports()" v-model="qParams.page_size" value="20" type="radio"
                   class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
            <label class="btn btn-outline-primary" for="btnradio2">20</label>

            <input @change="qParams.page = 1; fetchReports()" v-model="qParams.page_size" value="50" type="radio"
                   class="btn-check" name="btnradio" id="btnradio3" autocomplete="off">
            <label class="btn btn-outline-primary" for="btnradio3">50</label>

            <input @change="qParams.page = 1; fetchReports()" v-model="qParams.page_size" value="100" type="radio"
                   class="btn-check" name="btnradio" id="btnradio4" autocomplete="off">
            <label class="btn btn-outline-primary" for="btnradio4">100</label>
          </div>
        </div>
      </div>
      <!--      пагинатор-->
      <div class="col-6">
        <Vue3BsPaginate
            class="fw-bold"
            :total="reports.count"
            v-model="qParams.page"
            :perPage="qParams.page_size"
            :onChange="fetchReports"
            alignment="center"
        />
      </div>
    </div>
  </div>
</template>

<script>

import moment from "moment";

export default {
  name: "Dividends",
  data: () => ({
    moment:moment,
    idForDelete: null,
    loading: true,
    reports: [],
    qParams: {
      page: 1,
      page_size: 10,
      date_start: '',
      date_end: '',
    },
  }),
  async mounted() {

    if (this.$route.query) {
      this.qParams = {...this.qParams, ...this.$route.query}
      this.qParams.page = parseInt(this.qParams.page)
    }

    await this.fetchReports()

  },
  methods: {
    async fetchReports() {
      // console.log(new Date().toISOString().split('T')[0])
      try {
        this.reports = await this.$store.dispatch('fetchReports', {
          page: this.qParams.page,
          page_size: this.qParams.page_size,
          // приведение даты к виду '2010-01-01' (.toISOString().split('T')[0])
          date_start: this.qParams.date_start ? this.qParams.date_start : '2010-01-01',
          date_end: this.qParams.date_end ? this.qParams.date_end : moment(new Date).format('YYYY-MM-DD')
        })
        this.loading = false
      } catch (e) {
        console.log(e)
      }
    },
    async deleteReport() {
      try {
        await this.$store.dispatch('deleteReport', this.idForDelete);
        this.fetchReports()
      } catch (e) {
        console.log(e)
      } finally {
        this.idForDelete = null
      }
    },
    localeDate(date) {
      return new Date(date).toLocaleDateString("ru-RU", {
        year: 'numeric', month: 'long'
      })
    },
  }
}
</script>
<style>

</style>