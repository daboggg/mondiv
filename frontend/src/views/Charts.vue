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
            <div class="col-6">
              <div class="card">
                <div class="h3 card-header text-center">
                  Дивиденды в USD
                </div>
                <div class="card-body">
                  <bar
                      :options="chartOptions"
                      :data="chartData"
                  />
                </div>
              </div>
            </div>
            <div class="col-6">
              <div class="card">
                <div class="h3 card-header text-center">
                  Дивиденды в RUB
                </div>
                <div class="card-body">
                  <bar
                      :options="chartOptions"
                      :data="chartData"
                  />
                </div>
              </div>
            </div>
          </div>
          <div class="row mt-4">
            <div class="col-6">
              <div class="card">
                <div class="h3 card-header text-center">
                  Дивиденды в USD
                </div>
                <div class="card-body">
                  <bar
                      :options="chartOptions"
                      :data="chartData"
                  />
                </div>
              </div>
            </div>
            <div class="col-6">
              <div class="card">
                <div class="h3 card-header text-center">
                  Дивиденды в RUB
                </div>
                <div class="card-body">
                  <bar
                      :options="chartOptions"
                      :data="chartData"
                  />
                </div>
              </div>
            </div>
          </div>
          <div class="row mt-4">
            <div class="col-6">
              <div class="card">
                <div class="h3 card-header text-center">
                  Дивиденды в USD
                </div>
                <div class="card-body">
                  <bar
                      :options="chartOptions"
                      :data="chartData"
                  />
                </div>
              </div>
            </div>
            <div class="col-6">
              <div class="card">
                <div class="h3 card-header text-center">
                  Дивиденды в RUB
                </div>
                <div class="card-body">
                  <bar
                      :options="chartOptions"
                      :data="chartData"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
        <!--        отчеты-->
        <div class="tab-pane fade" id="nav-profile" role="tabpanel" aria-labelledby="nav-profile-tab">
          gGGGGGGGGGGGGGGGG
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
  name: "Charts",
  data: ()=>({
    chartData: {
      labels: ['январь','февраль','март','апрель','май'],
      datasets: [{data:[9,12,21,13,19]}]
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
    const res = (await this.$store.dispatch('dividendsForChart', {
      currency: 'RUB',
      type: 'total_for_each_year'
    })).res
    this.chartData = {
      labels: res.years,
      datasets: [{data:res.total}]
    }
  },
  components: {Bar}
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