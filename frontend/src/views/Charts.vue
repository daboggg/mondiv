<template>
  <div class="container  p-3 my-3 bg-body">
    <div class="row mx-3">
      <div class="col text-center my-5 display-6">Графическая часть</div>
      <nav>
        <div class="nav nav-tabs" id="nav-tab" role="tablist">
          <button class="nav-link active" id="nav-home-tab" data-bs-toggle="tab" data-bs-target="#nav-home"
                  type="button" role="tab" aria-controls="nav-home" aria-selected="true"><span
              class="h5">Дивиденды</span>
          </button>
          <button class="nav-link" id="nav-profile-tab" data-bs-toggle="tab" data-bs-target="#nav-profile" type="button"
                  role="tab" aria-controls="nav-profile" aria-selected="false"><span class="h5">Отчеты</span>
          </button>
        </div>
      </nav>

      <div class="tab-content" id="nav-tabContent">
        <!--        дивиденды-->
        <div class="tab-pane fade show active" id="nav-home" role="tabpanel" aria-labelledby="nav-home-tab">
          <div class="row mt-4">
            <div v-if="totalForEachYearInUSD" class="col-6">
              <div class="card">
                <div class="h3 card-header text-center">
                  Дивиденды в USD
                </div>
                <div class="card-body">
                  <bar
                      :options="totalForEachYearInUSD.chartOptions"
                      :data="totalForEachYearInUSD.chartData"
                  />
                </div>
              </div>
            </div>
            <div v-if="totalForEachYearInRUB" class="col-6">
              <div class="card">
                <div class="h3 card-header text-center">
                  Дивиденды в RUB
                </div>
                <div class="card-body">
                  <bar
                      :options="totalForEachYearInRUB.chartOptions"
                      :data="totalForEachYearInRUB.chartData"
                  />
                </div>
              </div>
            </div>
          </div>
          <div class="row mt-4">
            <div v-if="lastYearInUSD" class="col-6">
              <div class="card">
                <div class="h3 card-header text-center">
                  Дивиденды за последний год в USD
                </div>
                <div class="card-body">
                  <bar
                      :options="lastYearInUSD.chartOptions"
                      :data="lastYearInUSD.chartData"
                  />
                </div>
              </div>
            </div>
            <div v-if="lastYearInRUB" class="col-6">
              <div class="card">
                <div class="h3 card-header text-center">
                  Дивиденды за последний год в RUB
                </div>
                <div class="card-body">
                  <bar
                      :options="lastYearInRUB.chartOptions"
                      :data="lastYearInRUB.chartData"
                  />
                </div>
              </div>
            </div>
          </div>
          <div class="row mt-4">
            <div v-if="lastNYearsInUSD" class="col-6">
              <div class="card">
                <div class="h3 card-header text-center">
                  Дивиденды за три последних года в USD
                </div>
                <div class="card-body">
                  <bar
                      :options="lastNYearsInUSD.chartOptions"
                      :data="lastNYearsInUSD.chartData"
                  />
                </div>
              </div>
            </div>
            <div v-if="lastNYearsInRUB" class="col-6">
              <div class="card">
                <div class="h3 card-header text-center">
                  Дивиденды за три последних года в RUB
                </div>
                <div class="card-body">
                  <bar
                      :options="lastNYearsInRUB.chartOptions"
                      :data="lastNYearsInRUB.chartData"
                  />
                </div>
              </div>
            </div>
          </div>
          <div class="row mt-4">
            <div v-if="totalForEachTickerInUSD" class="col-6">
              <div class="card">
                <div class="h3 card-header text-center">
                  Дивиденды по компаниям в USD
                </div>
                <div class="card-body">
                  <doughnut
                      :options="totalForEachTickerInUSD.chartOptions"
                      :data="totalForEachTickerInUSD.chartData"
                  />
                </div>
              </div>
            </div>
            <div v-if="totalForEachTickerInRUB" class="col-6">
              <div class="card">
                <div class="h3 card-header text-center">
                  Дивиденды по компаниям в RUB
                </div>
                <div class="card-body">
                  <doughnut
                      :options="totalForEachTickerInRUB.chartOptions"
                      :data="totalForEachTickerInRUB.chartData"
                  />
                </div>
              </div>
            </div>
          </div>
          <div class="row mt-4">
            <div v-if="totalForEachAccountInUSD" class="col-6">
              <div class="card">
                <div class="h3 card-header text-center">
                  Дивиденды на счетах в USD
                </div>
                <div class="card-body">
                  <polar-area
                      :options="totalForEachAccountInUSD.chartOptions"
                      :data="totalForEachAccountInUSD.chartData"
                  />
                </div>
              </div>
            </div>
            <div v-if="totalForEachAccountInRUB" class="col-6">
              <div class="card">
                <div class="h3 card-header text-center">
                  Дивиденды на счетах в RUB
                </div>
                <div class="card-body">
                  <polar-area
                      :options="totalForEachAccountInRUB.chartOptions"
                      :data="totalForEachAccountInRUB.chartData"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
        <!--        отчеты-->
        <div class="tab-pane fade" id="nav-profile" role="tabpanel" aria-labelledby="nav-profile-tab">
          <div class="row mt-4">
            <div v-if="reportsForEachCompanyInUSD" class="col">
              <div class="card">
                <div class="h3 card-header text-center">
                  Отчеты в USD
                </div>
                <div class="card-body">
                  <Line
                      :options="reportsForEachCompanyInUSD.chartOptions"
                      :data="reportsForEachCompanyInUSD.chartData"
                  />
                </div>
              </div>
            </div>
          </div>
          <div class="row mt-4">
            <div v-if="reportsForEachCompanyInRUB" class="col">
              <div class="card">
                <div class="h3 card-header text-center">
                  Отчеты в RUB
                </div>
                <div class="card-body">
                  <Line
                      :options="reportsForEachCompanyInRUB.chartOptions"
                      :data="reportsForEachCompanyInRUB.chartData"
                  />
                </div>
              </div>
            </div>
          </div>
          <div class="row mt-4">
            <div v-if="generalReportInUSD" class="col">
              <div class="card">
                <div class="h3 card-header text-center">
                  Отчет в USD
                </div>
                <div class="card-body">
                  <Line
                      :options="generalReportInUSD.chartOptions"
                      :data="generalReportInUSD.chartData"
                  />
                </div>
              </div>
            </div>
          </div>
          <div class="row mt-4">
            <div v-if="generalReportInRUB" class="col">
              <div class="card">
                <div class="h3 card-header text-center">
                  Отчет в RUB
                </div>
                <div class="card-body">
                  <Line
                      :options="generalReportInRUB.chartOptions"
                      :data="generalReportInRUB.chartData"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import {Bar, Doughnut, PolarArea, Line} from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  Colors,
  ArcElement,
  RadialLinearScale,
  PointElement,
  LineElement,
} from 'chart.js';
import groupedChartData from "@/utils/groupedChartData";
import '@/utils/chartSettings'
import {backgroundColor, borderColor, threeColors} from "@/utils/chartSettings";
import moment from "moment";

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, BarElement, Title, Tooltip, Legend, Colors, ArcElement, RadialLinearScale)
// ChartJS.defaults.backgroundColor = 'rgba(0,121,107,0.64)';
export default {
  name: "Charts",
  data: () => ({
    totalForEachYearInUSD: null,
    totalForEachYearInRUB: null,
    lastYearInUSD: null,
    lastYearInRUB: null,
    lastNYearsInUSD: null,
    lastNYearsInRUB: null,
    totalForEachTickerInUSD: null,
    totalForEachTickerInRUB: null,
    totalForEachAccountInUSD: null,
    totalForEachAccountInRUB: null,
    reportsForEachCompanyInUSD: null,
    reportsForEachCompanyInRUB: null,
    generalReportInUSD: null,
    generalReportInRUB: null,
  }),
  mounted() {
    try {
      this.getDataForDividendCharts()
      this.getDataForReportCharts()
    } catch (e) {
      console.log(e)
    }
  },
  methods: {
    async getDataForDividendCharts() {

      let res, tmp;

      //totalForEachYearInUSD
      res = (await this.$store.dispatch('dividendsForChart', {
        currency: 'USD',
        type: 'total_for_each_year'
      })).res
      tmp = JSON.parse(JSON.stringify(groupedChartData));
      tmp.chartData.labels = res.years
      tmp.chartData.datasets = [{
        data: res.total,
        label: 'Дивиденды в USD',
        backgroundColor: backgroundColor,
        borderColor: borderColor,
        borderWidth: 2
      }]
      this.totalForEachYearInUSD = tmp

      //totalForEachYearInRUB
      res = (await this.$store.dispatch('dividendsForChart', {
        currency: 'RUB',
        type: 'total_for_each_year'
      })).res
      tmp = JSON.parse(JSON.stringify(groupedChartData));
      tmp.chartData.labels = res.years
      tmp.chartData.datasets = [{
        data: res.total,
        label: 'Дивиденды в RUB',
        backgroundColor: backgroundColor,
        borderColor: borderColor,
        borderWidth: 2
      }]
      this.totalForEachYearInRUB = tmp

      //lastYearInUSD
      res = (await this.$store.dispatch('dividendsForChart', {
        date_start: moment().subtract("years", 1).format('YYYY-MM-DD'),
        currency: 'USD',
        type: 'last_year'
      })).res
      tmp = JSON.parse(JSON.stringify(groupedChartData));
      tmp.chartData.labels = res.month
      tmp.chartData.datasets = [{
        data: res.total,
        label: 'Дивиденды в USD',
        backgroundColor: 'rgba(0,121,107,0.3)',
        borderColor: 'rgba(0,121,107,0.6)',
        borderWidth: 2
      }]
      this.lastYearInUSD = tmp

      //lastYearInRUB
      res = (await this.$store.dispatch('dividendsForChart', {
        date_start: moment().subtract("years", 1).format('YYYY-MM-DD'),
        currency: 'RUB',
        type: 'last_year'
      })).res
      tmp = JSON.parse(JSON.stringify(groupedChartData));
      tmp.chartData.labels = res.month
      tmp.chartData.datasets = [{
        data: res.total,
        label: 'Дивиденды в RUB',
        backgroundColor: 'rgba(0,121,107,0.3)',
        borderColor: 'rgba(0,121,107,0.6)',
        borderWidth: 2
      }]
      this.lastYearInRUB = tmp

      //lastNYearsInUSD
      res = (await this.$store.dispatch('dividendsForChart', {
        date_start: moment().subtract("years", 2).year() + '-01-01',
        currency: 'USD',
        type: 'last_n_years'
      }))
      tmp = JSON.parse(JSON.stringify(groupedChartData));
      tmp.chartData.labels = res.month
      tmp.chartOptions.plugins.legend.display = true
      const tmpChartDataUSD = []
      Object.keys(res.years).forEach(a => {
        tmpChartDataUSD.push({
          data: res.years[a],
          label: `Дивиденды за ${a} год в USD`,
        })
      })
      tmp.chartData.datasets = tmpChartDataUSD
      this.lastNYearsInUSD = tmp

      //lastNYearsInUSD
      res = (await this.$store.dispatch('dividendsForChart', {
        date_start: moment().subtract("years", 2).year() + '-01-01',
        currency: 'RUB',
        type: 'last_n_years'
      }))
      tmp = JSON.parse(JSON.stringify(groupedChartData));
      tmp.chartData.labels = res.month
      tmp.chartOptions.plugins.legend.display = true
      const tmpChartDataRUB = []
      Object.keys(res.years).forEach(a => {
        tmpChartDataRUB.push({
          data: res.years[a],
          label: `Дивиденды за ${a} год в RUB`,
        })
      })
      tmp.chartData.datasets = tmpChartDataRUB
      this.lastNYearsInRUB = tmp

      //totalForEachTickerInUSD
      res = (await this.$store.dispatch('dividendsForChart', {
        currency: 'USD',
        type: 'total_for_each_ticker'
      }))
      tmp = JSON.parse(JSON.stringify(groupedChartData));
      tmp.chartData.labels = res.companyName
      tmp.chartData.datasets = [{
        data: res.total,
        label: 'Всего в USD',
      }]
      this.totalForEachTickerInUSD = tmp

      //totalForEachTickerInRUB
      res = (await this.$store.dispatch('dividendsForChart', {
        currency: 'RUB',
        type: 'total_for_each_ticker'
      }))
      tmp = JSON.parse(JSON.stringify(groupedChartData));
      tmp.chartData.labels = res.companyName
      tmp.chartData.datasets = [{
        data: res.total,
        label: 'Всего в RUB',
      }]
      this.totalForEachTickerInRUB = tmp

      //totalForEachAccountInUSD
      res = (await this.$store.dispatch('dividendsForChart', {
        currency: 'USD',
        type: 'total_for_each_account'
      }))
      tmp = JSON.parse(JSON.stringify(groupedChartData));
      tmp.chartOptions.plugins.legend.display = true
      tmp.chartData.labels = res.accountName
      tmp.chartData.datasets = [{
        data: res.total,
        label: 'Всего в USD',
      }]
      this.totalForEachAccountInUSD = tmp

      //totalForEachAccountInRUB
      res = (await this.$store.dispatch('dividendsForChart', {
        currency: 'RUB',
        type: 'total_for_each_account'
      }))
      tmp = JSON.parse(JSON.stringify(groupedChartData));
      tmp.chartOptions.plugins.legend.display = true
      tmp.chartData.labels = res.accountName
      tmp.chartData.datasets = [{
        data: res.total,
        label: 'Всего в RUB',
      }]
      this.totalForEachAccountInRUB = tmp
    },
    async getDataForReportCharts() {
      let data, tmp, tmpDatasets;

      //reportsForEachCompanyInUSD
      data = (await this.$store.dispatch('reportsForChart', {
        currency: 'USD',
        type: 'reports_for_each_company'
      }))

      tmp = JSON.parse(JSON.stringify(groupedChartData))
      tmp.chartOptions.responsive = true
      tmp.chartOptions.maintainAspectRatio = false
      tmp.chartOptions.plugins.legend.display = true
      tmp.chartData.labels = data.labels
      tmpDatasets = []
      Object.keys(data.data).forEach(acc => {
        tmpDatasets.push({
          data: data.data[acc],
          label: acc,
          pointStyle: 'rectRounded',
          pointRadius: 10,
          pointHoverRadius: 12,
          pointBorderWidth: 0,
          borderWidth: 7,
          tension: 0.3
        })
      })
      tmp.chartData.datasets = tmpDatasets

      this.reportsForEachCompanyInUSD = tmp

      //reportsForEachCompanyInRUB
      data = (await this.$store.dispatch('reportsForChart', {
        currency: 'RUB',
        type: 'reports_for_each_company'
      }))

      tmp = JSON.parse(JSON.stringify(groupedChartData))
      tmp.chartOptions.responsive = true
      tmp.chartOptions.maintainAspectRatio = false
      tmp.chartOptions.plugins.legend.display = true
      tmp.chartData.labels = data.labels
      tmpDatasets = []
      Object.keys(data.data).forEach(acc => {
        tmpDatasets.push({
          data: data.data[acc],
          label: acc,
          pointStyle: 'rectRounded',
          pointRadius: 10,
          pointHoverRadius: 12,
          pointBorderWidth: 0,
          borderWidth: 7,
          tension: 0.3
        })
      })
      tmp.chartData.datasets = tmpDatasets
      // console.log(tmp)
      this.reportsForEachCompanyInRUB = tmp

      //generalReportInUSD
      data = (await this.$store.dispatch('reportsForChart', {
        currency: 'USD',
        type: 'general_report'
      }))

      tmp = JSON.parse(JSON.stringify(groupedChartData))
      tmp.chartOptions.responsive = true
      tmp.chartOptions.maintainAspectRatio = false
      tmp.chartData.labels = data.labels
      tmp.chartData.datasets = [{
        data: data.data,
        label: 'USD',
        pointStyle: 'rectRounded',
        pointRadius: 10,
        pointHoverRadius: 12,
        pointBorderWidth: 0,
        borderWidth: 7,
        tension: 0.3
      }]

      this.generalReportInUSD = tmp

      //generalReportInRUB
      data = (await this.$store.dispatch('reportsForChart', {
        currency: 'RUB',
        type: 'general_report'
      }))

      tmp = JSON.parse(JSON.stringify(groupedChartData))
      tmp.chartOptions.responsive = true
      tmp.chartOptions.maintainAspectRatio = false
      tmp.chartData.labels = data.labels
      tmp.chartData.datasets = [{
        data: data.data,
        label: 'RUB',
        pointStyle: 'rectRounded',
        pointRadius: 10,
        pointHoverRadius: 12,
        pointBorderWidth: 0,
        borderWidth: 7,
        tension: 0.3
      }]

      this.generalReportInRUB = tmp
    }

  },
  computed: {},
  components: {Bar, Doughnut, PolarArea, Line}
}
</script>

<style scoped>
.nav-tabs {
  border-bottom: teal 2px solid;
}

.nav-link, .card-header {
  color: teal;
}

.nav-link.active {
  background-color: teal;
  color: white;
}
</style>