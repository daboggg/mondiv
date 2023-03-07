<template>
  <div class="container">
    <table class="striped">
      <thead>
      <tr>
        <th>#</th>
        <th>Лого</th>
        <th>Тикер</th>
        <th>Название</th>
        <th>Валюта</th>
        <th>Выплата</th>
        <th>Дата</th>
        <th>Счет</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="div in dividends" :key="div.id">
        <td>*</td>
        <td><img class="icon_min" :src="div.company.icon_image" alt=""></td>
        <td>{{ div.company.ticker }}</td>
        <td>{{ div.company.name }}</td>
        <td>{{ div.currency.name }}</td>
        <td>{{ div.payoff }}</td>
        <td>{{ div.date_of_receipt }}</td>
        <td>{{ div.account.name }}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "Dividends",
  data: () => ({
    dividends: []
  }),
  async mounted() {
    try {
      if (!this.$store.getters.dividends.length) {
        this.$store.dispatch('getDividends')
      }
      this.dividends = this.$store.getters.dividends;
    } catch (e) {
      console.log(e)
    }
  },
  methods: {}
}
</script>

<style scoped>
img.icon_min {
  height: 50px;
  width: 50px;
}
</style>