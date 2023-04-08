<template>
  <div class="container  p-3 my-3 bg-body">

    <div class="col text-center my-4 display-6">Статистика по дивидендам</div>

    <div class="row">
      <div class="col">
        <div class="card text-center">
          <div class="card-header text-center h3">
            Статистика в USD
          </div>
          <div class="card-body">

            <!--  спиннер-->
            <div v-if="loading" class="text-center mt-5">
              <div class="spinner-border mt-5" role="status">
                <span class="visually-hidden">Загрузка...</span>
              </div>
            </div>

            <ul v-else class="list-group my-3">
              <li class="list-group-item list-group-item-success d-flex justify-content-between align-items-start">
                <h5 class="text-start">Минимальная выплата у {{statisticDataInUSD.minPayment.company__name }}</h5>
                <h5><span class="badge bg-primary rounded-pill">{{statisticDataInUSD.minPayment.payoff}}</span></h5>
              </li>
              <li class="list-group-item list-group-item-success d-flex justify-content-between align-items-start">
                <h5 class="text-start">Максимальная выплата у {{statisticDataInUSD.maxPayment.company__name }}</h5>
                <h5><span class="badge bg-primary rounded-pill">{{statisticDataInUSD.maxPayment.payoff}}</span></h5>
              </li>
              <li class="list-group-item list-group-item-success d-flex justify-content-between align-items-start">
                <h5 class="text-start">Общее число выплат дивидендов</h5>
                <h5><span class="badge bg-primary rounded-pill">{{statisticDataInUSD.totalPayments}}</span></h5>
              </li>
              <li class="list-group-item list-group-item-success d-flex justify-content-between align-items-start">
                <h5 class="text-start">Общее сумма дивидендов</h5>
                <h5><span class="badge bg-primary rounded-pill">{{statisticDataInUSD.total}}</span></h5>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card text-center">
          <div class="card-header text-center h3">
            Статистика в RUB
          </div>
          <div class="card-body">

            <!--  спиннер-->
            <div v-if="loading" class="text-center mt-5">
              <div class="spinner-border mt-5" role="status">
                <span class="visually-hidden">Загрузка...</span>
              </div>
            </div>

            <ul v-else class="list-group my-3">
              <li class="list-group-item list-group-item-success d-flex justify-content-between align-items-start">
                <h5 class="text-start">Минимальная выплата у {{statisticDataInRUB.minPayment.company__name }}</h5>
                <h5><span class="badge bg-primary rounded-pill">{{statisticDataInRUB.minPayment.payoff}}</span></h5>
              </li>
              <li class="list-group-item list-group-item-success d-flex justify-content-between align-items-start">
                <h5 class="text-start">Максимальная выплата у {{statisticDataInRUB.maxPayment.company__name }}</h5>
                <h5><span class="badge bg-primary rounded-pill">{{statisticDataInRUB.maxPayment.payoff}}</span></h5>
              </li>
              <li class="list-group-item list-group-item-success d-flex justify-content-between align-items-start">
                <h5 class="text-start">Общее число выплат дивидендов</h5>
                <h5><span class="badge bg-primary rounded-pill">{{statisticDataInRUB.totalPayments}}</span></h5>
              </li>
              <li class="list-group-item list-group-item-success d-flex justify-content-between align-items-start">
                <h5 class="text-start">Общее сумма дивидендов</h5>
                <h5><span class="badge bg-primary rounded-pill">{{statisticDataInRUB.total}}</span></h5>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Statistics",
  data: () => ({
    loading: true,
    statisticDataInUSD: null,
    statisticDataInRUB: null,
  }),
  async mounted() {
    try {
      await this.getStatisticData();
      this.loading = false
    } catch (e) {
      console.log(e)
    }
  },
  methods: {
    async getStatisticData() {
      this.statisticDataInUSD = await this.$store.dispatch('dividendsForChart', {
        currency: 'USD',
        type: 'statistics'
      })
      this.statisticDataInRUB = await this.$store.dispatch('dividendsForChart', {
        currency: 'RUB',
        type: 'statistics'
      })
    }
  }
}
</script>

<style scoped>
.badge {
  background-color: #00796b !important;
}
</style>