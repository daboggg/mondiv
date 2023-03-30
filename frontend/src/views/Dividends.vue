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
      <div class="col-md-12 col-xl-8 offset-xl-2">
        <form class=" input-group justify-content-center my-4" @submit.prevent="qParams.page = 1; fetchDividends()">

        <span class="input-group-text">С</span>
        <input v-model="qParams.date_start" type="date"
               class="form-control" min="2019-01-01"
               :max="new Date().toLocaleDateString('en-CA')"
               style="font-weight: bold"
        />
        <button type="button" @click="qParams.date_start = ''; fetchDividends()" class="input-group-btn btn btn-light ms-1"><i
            class="bi-x-lg text-danger"></i></button>

        <span class="input-group-text ms-3">По</span>
        <input v-model="qParams.date_end" type="date"
               class="form-control" min="2019-01-01"
               :max="new Date().toLocaleDateString('en-CA')"
               style="font-weight: bold"

        />
        <button type="button" @click="qParams.date_end = ''; fetchDividends()" class="input-group-btn btn btn-light ms-1"><i
            class="bi-x-lg text-danger"></i></button>

        <button class="btn btn-light ms-3 btn-outline-dark" type="submit">Выбрать</button>
      </form>
      </div>
    </div>

    <!--      поиск -->
    <div class="row justify-content-center">
      <div class="col-6">
        <div class="input-group">
          <span class="input-group-text">Поиск</span>
          <input @input="qParams.page = 1; fetchDividends()" v-model="qParams.search" type="text" class="form-control">
          <button type="button" @click="qParams.search = ''; fetchDividends()" class="input-group-btn btn btn-light ms-1"><i
            class="bi-x-lg text-danger"></i></button>
        </div>
      </div>
    </div>

    <!--    счетчик записей-->
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
            <th>{{ (index + 1) + (qParams.page - 1) * qParams.page_size }}</th>
            <td><img class="icon_min img-thumbnail" :src="div.company.icon_image" alt=""></td>
            <td>{{ div.company.ticker }}</td>
            <td>{{ div.company.name }}</td>
            <td>{{ div.currency.name }}</td>
            <td>{{ parseFloat(div.payoff).toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, "$1 ").replace('.', ',') }}</td>
            <td>{{ localeDate(div.date_of_receipt) }}</td>
            <td>{{ div.account.name }}</td>
            <td>
              <router-link
                  :to="{ name: 'edit_dividend', params: { id: div.id }, query: qParams}">
                <i
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

            <input @change="qParams.page = 1; fetchDividends()" v-model="qParams.page_size" value="10" type="radio"
                   class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked>
            <label class="btn btn-outline-primary" for="btnradio1">10</label>

            <input @change="qParams.page = 1; fetchDividends()" v-model="qParams.page_size" value="20" type="radio"
                   class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
            <label class="btn btn-outline-primary" for="btnradio2">20</label>

            <input @change="qParams.page = 1; fetchDividends()" v-model="qParams.page_size" value="50" type="radio"
                   class="btn-check" name="btnradio" id="btnradio3" autocomplete="off">
            <label class="btn btn-outline-primary" for="btnradio3">50</label>

            <input @change="qParams.page = 1; fetchDividends()" v-model="qParams.page_size" value="100" type="radio"
                   class="btn-check" name="btnradio" id="btnradio4" autocomplete="off">
            <label class="btn btn-outline-primary" for="btnradio4">100</label>
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
        {{ qParams.page }}
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: "Dividends",
  data: () => ({
    idForDelete: null,
    loading: true,
    qParams: {
      page: 1,
      page_size: 10,
      date_start: '',
      date_end: '',
      search: '',
    },
  }),
  async mounted() {
    if (this.$route.query) {
      this.qParams = {...this.qParams, ...this.$route.query}
      this.qParams.page = parseInt(this.qParams.page)
    }

    await this.fetchDividends();
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
          page: this.qParams.page,
          page_size: this.qParams.page_size,
          search: this.qParams.search,
          // приведение даты к виду '2010-01-01' (.toISOString().split('T')[0])
          date_start: this.qParams.date_start ? this.qParams.date_start : '2010-01-01',
          date_end: this.qParams.date_end ? this.qParams.date_end : new Date().toISOString().split('T')[0]
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
  }
}
</script>
<style>
</style>