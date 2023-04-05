<template>
  <!--  спиннер-->
  <div v-if="loading" class="text-center mt-5">
    <div class="spinner-border mt-5" role="status">
      <span class="visually-hidden">Загрузка...</span>
    </div>
  </div>

  <div v-else class="container p-3 my-3 bg-body">
    <div class="col text-center my-5 display-6">Информация о компании: {{ company.name }}</div>
    <div class="row">
<!--      график дивиденды-->
      <div class="col">
        <div class="card row ms-2 me-1">
          <div v-if="loadingChart" class="card-body text-center my-5">
            <div class="spinner-border text-success" role="status">
              <span class="visually-hidden">Загрузка...</span>
            </div>
          </div>
          <bar
              v-else
              id="my-chart-id"
              :key="chartData.labels"
              :options="chartOptions"
              :data="chartData"
          />
          <div class="card-footer text-muted">
            <div class="input-group justify-content-center">
              <span class="input-group-text" id="basic-addon1"> Последние </span>
              <div class="btn-group" role="group" aria-label="limit dividends">
                <input @change="dividendHistory()" v-model="limit" value="10" type="radio" class="btn-check"
                       name="btnradio" id="btnradio1" autocomplete="off" checked>
                <label class="btn btn-outline-primary" for="btnradio1">10</label>

                <input @change="dividendHistory()" v-model="limit" value="20" type="radio" class="btn-check"
                       name="btnradio" id="btnradio2" autocomplete="off">
                <label class="btn btn-outline-primary" for="btnradio2">20</label>

                <input @change="dividendHistory()" v-model="limit" value="40" type="radio" class="btn-check"
                       name="btnradio" id="btnradio3" autocomplete="off">
                <label class="btn btn-outline-primary" for="btnradio3">40</label>
              </div>
            </div>
          </div>
        </div>
      </div>
<!--      информация по комппании-->
      <div class="col">
        <div class="card row ms-1 me-2">
          <div class="col-4 offset-4 mt-4">
            <img v-if="company.icon_image" :src="company.icon_image" class=" card-img-top" alt="...">
            <img v-else src="https://i.postimg.cc/bwSyqTTF/empty.jpg" class="card-img-top" alt="...">
          </div>
          <div class="card-body">
            <h3 class="card-title text-center">{{ company.name }}</h3>
            <h4 class="card-subtitle mb-2 text-muted text-center">Тикер: {{ company.ticker }}</h4>
            <p class="card-text">{{ company.description }}</p>
          </div>
        </div>
      </div>
    </div>

    <div v-if="!dividends.count" class="col text-center my-5 display-6">Полученных дивидендов нет</div>
<!--    таблица полученных дивидендов-->
    <div v-else class="row">
      <div class="col-10 offset-1 mt-5">
        <div class="col text-center my-5 display-6">Полученные дивиденды:</div>

        <!--    счетчик записей-->
        <span class="h5 ms-3 my-3">Записей: <span class="badge bg-secondary">{{ dividends.count }}</span></span>
        <!--    общая сумма дивидендов-->
        <span class="h5 ms-5 my-3">Сумма: <span class="badge bg-secondary">{{ totalPayoff }}</span></span>

        <!--    таблица-->
        <div class="row mt-3">
          <div class="col-12">
            <table class="table align-middle">
              <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Дата выплаты</th>
                <th scope="col">Сумма</th>
                <th scope="col">Валюта</th>
                <th scope="col">Счет</th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="(div, index) in dividends.results" :key="div.id">
                <th>{{ (index + 1) + (qParams.page - 1) * qParams.page_size }}</th>
                <td>{{ div.date_of_receipt }}</td>
                <td>{{ div.payoff }}</td>
                <td>{{ div.currency.name }}</td>
                <td>{{ div.account.name }}</td>
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

                <input @change="qParams.page = 1; fetchDividends()" v-model="qParams.page_size" value="10" type="radio"
                       class="btn-check" name="btnradio" id="btnradio11" autocomplete="off" checked>
                <label class="btn btn-outline-primary" for="btnradio11">10</label>

                <input @change="qParams.page = 1; fetchDividends()" v-model="qParams.page_size" value="20" type="radio"
                       class="btn-check" name="btnradio" id="btnradio22" autocomplete="off">
                <label class="btn btn-outline-primary" for="btnradio22">20</label>

                <input @change="qParams.page = 1; fetchDividends()" v-model="qParams.page_size" value="50" type="radio"
                       class="btn-check" name="btnradio" id="btnradio33" autocomplete="off">
                <label class="btn btn-outline-primary" for="btnradio33">50</label>

                <input @change="qParams.page = 1; fetchDividends()" v-model="qParams.page_size" value="100" type="radio"
                       class="btn-check" name="btnradio" id="btnradio44" autocomplete="off">
                <label class="btn btn-outline-primary" for="btnradio44">100</label>
              </div>
            </div>
          </div>
          <!--      пагинатор-->
          <div class="col-6">
            <Vue3BsPaginate
                class="fw-bold"
                :key="qParams.page"
                :total="dividends.count"
                v-model="qParams.page"
                :perPage="qParams.page_size"
                :onChange="fetchDividends"
                alignment="center"
            />
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import {Bar} from 'vue-chartjs'
import {Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)
ChartJS.defaults.backgroundColor = 'rgba(0,121,107,0.64)';

export default {
  name: "Company",
  props: ['id'],
  data: () => ({
    limit: 10,
    loading: true,
    loadingChart: true,
    company: {},
    dividends: [],
    totalPayoff: 0,
    qParams: {
      page: 1,
      page_size: 10,
    },
    chartData: {
      labels: [],
      datasets: []
    },
    chartOptions: {
      maintainAspectRatio: true,
      aspectRatio: 1,
      layout: {
        padding: 5
      },
      plugins: {
        legend: {
          display: false,
        },
        tooltip: {
          titleFont: {
            size: 20
          }
        },
        title: {
          font: {
            size: 30
          },
          display: true,
          text: ''
        }
      }
    },

  }),
  async mounted() {
    if (this.$route.query) {
      this.qParams = {...this.qParams, ...this.$route.query}
      this.qParams.page = parseInt(this.qParams.page)
    }

    try {
      this.company = await this.$store.dispatch('getCompany', this.id)
      this.totalPayoff = (await this.$store.dispatch('totalPayoff', {ticker: this.company.ticker})).totalPayoff
      await this.fetchDividends()
      await this.dividendHistory()
      this.loading = false
    } catch (e) {
      console.log(e)
    }
  },
  methods: {
    async fetchDividends() {
      try {
        await this.$store.dispatch('fetchDividends', {
          ticker: this.company.ticker,
          page: this.qParams.page,
          page_size: this.qParams.page_size
        })
        this.dividends = this.$store.getters.dividends
      } catch (e) {

      }
    },
    async dividendHistory() {
      this.loadingChart = true
      this.chartOptions.plugins.title.text = `Дивиденды, последние ${this.limit} выплат`;
      const res = (await this.$store.dispatch('dividendHistory', {limit: this.limit, ticker: this.company.ticker})).res;
      this.chartData = {
        labels: res[1],
        datasets: [{data: res[0], label: 'выплата'}]
      }
      this.loadingChart = false
    },
  },
  components: {
    Bar
  },
}
</script>

<style scoped>
.badge{
  background-color: teal !important;
}
</style>