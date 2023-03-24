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
            <button @click="deleteDividend" type="button" class="btn btn-danger" data-bs-dismiss="modal">Удалить
            </button>
          </div>
        </div>
      </div>
    </div>


    <div class="col text-center mt-2 display-6">Полученные дивиденды</div>

    <!--    выбор по дате-->
    <div class="row">
      <form class="input-group justify-content-center my-4" @submit.prevent="currentPage = 1; fetchDividends()">
        <span class="input-group-text">С</span>
        <datepicker v-model="datepicker.start"
                    :inputFormat="datepicker.inputFormat"
                    :locale="datepicker.ru"
                    :upperLimit="datepicker.upperLimit"
                    class="form-control"
        />
        <button type="button" @click="datepicker.start = null" class="btn btn-light ms-1"><i
            class="bi-x-lg text-danger"></i></button>
        <span class="input-group-text ms-3">По</span>
        <datepicker v-model="datepicker.end"
                    :inputFormat="datepicker.inputFormat"
                    :locale="datepicker.ru"
                    :upperLimit="datepicker.upperLimit"
                    class="form-control"
        />
        <button type="button" @click="datepicker.end = null" class="btn btn-light ms-1"><i
            class="bi-x-lg text-danger"></i></button>
        <button class="btn btn-light ms-3 btn-outline-dark" type="submit">Выбрать</button>
      </form>
    </div>

    <!--      поиск -->
    <div class="row justify-content-center">
      <div class="col-6">
        <div class="input-group">
          <span class="input-group-text">Поиск</span>
          <input @input="currentPage = 1; fetchDividends()" v-model="search" type="text" class="form-control">
        </div>
      </div>
    </div>

    <h5 class="ms-3 my-3">Записей: <span class="badge bg-secondary">{{ dividends.count }}</span></h5>

    <!--    таблица-->
    <div class="row">
      <div class="col-12">
        <table class="table align-middle">
          <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Лого</th>
            <th scope="col">Тикер</th>
            <th scope="col">Название</th>
            <th scope="col">Валюта</th>
            <th scope="col">Выплата</th>
            <th scope="col">Дата</th>
            <th scope="col">Счет</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(div, index) in dividends.results" :key="div.id">
            <th>{{ index + 1 }}</th>
            <td><img class="icon_min img-thumbnail" :src="div.company.icon_image" alt=""></td>
            <td>{{ div.company.ticker }}</td>
            <td>{{ div.company.name }}</td>
            <td>{{ div.currency.name }}</td>
            <td>{{ parseFloat(div.payoff).toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, "$1 ").replace('.', ',') }}</td>
            <td>{{ localeDate(div.date_of_receipt) }}</td>
            <td>{{ div.account.name }}</td>
            <td>
              <router-link :to="{ name: 'edit_dividend', params: { id: div.id }, query:{r_page:this.currentPage}}"><i
                  class="text-black bi-pencil fs-4"></i></router-link>
            </td>
            <td>
              <router-link to="" @click="idForDelete = div.id" data-bs-toggle="modal" data-bs-target="#deleteModal">
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

            <input @change="currentPage = 1; fetchDividends()" v-model="pageSize" value="10" type="radio"
                   class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked>
            <label class="btn btn-outline-primary" for="btnradio1">10</label>

            <input @change="currentPage = 1; fetchDividends()" v-model="pageSize" value="20" type="radio"
                   class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
            <label class="btn btn-outline-primary" for="btnradio2">20</label>

            <input @change="currentPage = 1; fetchDividends()" v-model="pageSize" value="50" type="radio"
                   class="btn-check" name="btnradio" id="btnradio3" autocomplete="off">
            <label class="btn btn-outline-primary" for="btnradio3">50</label>

            <input @change="currentPage = 1; fetchDividends()" v-model="pageSize" value="100" type="radio"
                   class="btn-check" name="btnradio" id="btnradio4" autocomplete="off">
            <label class="btn btn-outline-primary" for="btnradio4">100</label>
          </div>
        </div>
      </div>
      <!--      пагинатор-->
      <div class="col-6">
        <Vue3BsPaginate
            class="fw-bold"
            :total="dividends.count"
            v-model="currentPage"
            :perPage="pageSize"
            :onChange="fetchDividends"
            alignment="center"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Datepicker from 'vue3-datepicker'
import {ru} from 'date-fns/locale'

export default {
  name: "Dividends",
  data: () => ({
    idForDelete: null,
    loading: true,
    search: '',
    currentPage: 1,
    pageSize: 10,
    datepicker: {
      start: null,
      end: null,
      ru: ru,
      upperLimit: new Date(),
      inputFormat: 'dd MMMM yyyy',
      typeable: true
    }
  }),
  async mounted() {
    if (this.$route.query.r_page) {
      this.currentPage = this.$route.query.r_page
    }
    await this.fetchDividends()

  },
  computed: {
    dividends() {
      return this.$store.getters.dividends
    },
  },
  methods: {
    async fetchDividends() {
      try {
        await this.$store.dispatch('fetchDividends', {
          page: this.currentPage,
          page_size: this.pageSize,
          search: this.search,
          // приведение даты к виду '2010-01-01'
          start: this.datepicker.start ? this.datepicker.start.toLocaleDateString("en-CA") : '2010-01-01',
          end: this.datepicker.end ? this.datepicker.end.toLocaleDateString("en-CA") : new Date().toLocaleDateString("en-CA")
        })
        this.loading = false
      } catch (e) {
        console.log(e)
      }
    },
    async deleteDividend() {
      try {
        await this.$store.dispatch('deleteDividend', this.idForDelete);
        this.fetchDividends()
      } catch (e) {
        console.log(e)
      } finally {
        this.idForDelete = null
      }
    },
    localeDate(date) {
      return new Date(date).toLocaleDateString("ru-RU", {
        year: 'numeric', month: 'long', day: 'numeric'
      })
    },
  },
  components: {
    Datepicker
  }
}
</script>
<style>

</style>