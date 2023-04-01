<template>
  <!--  спиннер-->
  <div v-if="loading" class="text-center mt-5">
    <div class="spinner-border mt-5" role="status">
      <span class="visually-hidden">Загрузка...</span>
    </div>
  </div>

  <div v-else class="container p-3 my-3 bg-body">
    {{company}}
    <bar
        id="my-chart-id"
        :options="chartOptions"
        :data="chartData"
    />
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import {Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

export default {
  name: "Company",
  props:['id'],
  data:()=>({
    loading: true,
    company: {},
    chartData: {
        labels: [ 'January', 'February', 'March' ],
        datasets: [ { data: [40, 20, 12] } ]
      },
      chartOptions: {
        responsive: true
      }
  }),
  async mounted() {
    this.company = await this.$store.dispatch('getCompany', this.id)
    this.loading = false
  },
  components:{
    Bar
  }
}
</script>

<style scoped>

</style>