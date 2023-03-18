<template>

  {{ dividends }}

  <form class="row mt-5" @submit.prevent="currentPage = 1; fetchDividends()">
    <div class="input-group col-6 offset-3">
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
    </div>
  </form>


  <div class="container mt-4">
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
        <td><img class="icon_min" :src="div.company.icon_image" alt=""></td>
        <td>{{ div.company.ticker }}</td>
        <td>{{ div.company.name }}</td>
        <td>{{ div.currency.name }}</td>
        <td>{{ div.payoff }}</td>
        <td>{{ localeDate(div.date_of_receipt) }}</td>
        <td>{{ div.account.name }}</td>
        <td><i class="bi-pencil fs-4"></i></td>
        <td><i class="bi-x-lg fs-4 text-danger"></i></td>
      </tr>
      </tbody>
    </table>
  </div>

  <Vue3BsPaginate
      class="mt-5 fw-bold"
      :total="dividends.count"
      v-model="currentPage"
      :perPage="3"
      :onChange="fetchDividends"
      alignment="center"
  />
</template>

<script>
import Datepicker from 'vue3-datepicker'
import {ru} from 'date-fns/locale'

export default {
  name: "Dividends",
  data: () => ({
    currentPage: 1,
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
          // приведение даты в виду '2010-01-01'
          start: this.datepicker.start ? this.datepicker.start.toLocaleDateString("en-CA") : '2010-01-01',
          end: this.datepicker.end ? this.datepicker.end.toLocaleDateString("en-CA") : new Date().toLocaleDateString("en-CA")
        })
        // this.$router.push({query: {page: 26, page_size: 1}})
      } catch (e) {
        console.log(e)
      }
    },
    localeDate(date) {
      const options = {year: 'numeric', month: 'long', day: 'numeric'};
      const dt = new Date(date);
      return dt.toLocaleDateString("ru-RU", options)
    },
  },
  components: {
    Datepicker
  }
}
</script>
<style>

</style>