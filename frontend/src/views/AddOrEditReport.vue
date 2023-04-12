<template>

  <div class="container-fluid">
    <div class="row">
      <div class="col-xs-12 col-md-8 offset-md-2 col-xl-4 offset-xl-4">
        <div class="card text-white mt-5" style="background-color: #00796b">
          <div class="h5 card-header"><i class="bi-plus-circle fs-5 me-2"></i>{{id?'Изменить':'Добавить'}} отчет</div>
          <div class="card-body">
            <form class="" @submit.prevent="submitHandler">

              <!--              дата отчета-->
              <div class="mb-3">
                <i class="bi-calendar3 fs-5 me-2"></i>
                <label for="chooseDate" class="form-label">Дата отчета</label>
<!--                <datepicker v-model="datepicker.date"-->
<!--                            id="chooseDate"-->
<!--                            :inputFormat="datepicker.inputFormat"-->
<!--                            :locale="datepicker.ru"-->
<!--                            :upperLimit="datepicker.upperLimit"-->
<!--                            :typeable="datepicker.typeable"-->
<!--                            class="form-control"-->
<!--                />-->
                <input v-model="datepicker.date"
                       type="month"
                       id="chooseDate"
                       class="form-control"
                       :max="moment().format('YYYY-MM')"
                >
                <div
                    class="invalid form-text"
                    v-for="e in v$.datepicker.date.$errors"
                    :key="e.$uid"
                >{{ e.$message }}
                </div>
              </div>

              <!--сумма-->
              <div class="mb-3">
                <i class="bi-coin fs-5 me-2"></i>
                <label for="payment" class="form-label">Сумма</label>
                <input v-model="amount" type="number" step="0.01" class="form-control" id="payment">
                <div
                    class="invalid form-text"
                    v-for="e in v$.amount.$errors"
                    :key="e.$uid"
                >{{ e.$message }}
                </div>
              </div>


              <!--           валюта-->
              <div class="mb-3">
                <i class="bi-currency-exchange fs-5 me-2"></i>
                <label class="form-label" for="id_currency">Валюта</label>
                <select v-model="currency" name="currency" class="form-select"
                        id="id_currency">
                  <option v-for="cur in $store.getters.currencies"
                          :value="cur.id">{{ cur.name }}
                  </option>
                </select>
                <div
                    class="invalid form-text"
                    v-for="e in v$.currency.$errors"
                    :key="e.$uid"
                >{{ e.$message }}
                </div>
              </div>


              <!--          счет-->
              <div class="mb-3">
                <i class="bi-receipt fs-5 me-2"></i>
                <label class="form-label" for="id_account">Счет</label>
                <select v-model="account" name="account" class="form-select"
                        id="id_account">
                  <option v-for="acc in $store.getters.accounts"
                          :value="acc.id">{{ acc.name }}
                  </option>
                </select>
                <div
                    class="invalid form-text"
                    v-for="e in v$.account.$errors"
                    :key="e.$uid"
                >{{ e.$message }}
                </div>
              </div>

              <button type="submit"
                      class="border-3 border border-white mt-3 btn-login btn-outline-light btn float-end">
                <strong>{{id?'Изменить':'Добавить'}}</strong><i class="ms-2 mt-1 bi-play-fill"></i></button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {useVuelidate} from "@vuelidate/core"
import {helpers, required} from "@vuelidate/validators";
import {ru} from "date-fns/locale";
import Datepicker from 'vue3-datepicker'
import moment from 'moment'


export default {
  name: "AddOrEditReport",
  props: ['id'],
  setup() {
    return {
      v$: useVuelidate()
    }
  },
  data: () => ({
    moment: moment,
    amount: '',
    account: '',
    currency: '',
    datepicker: {
      date: null,
      ru: ru,
      upperLimit: new Date(),
      inputFormat: 'dd MMMM yyyy',
      typeable: false
    },
    editableReport: {}
  }),
  validations() {
    return {
      account: {
        required: helpers.withMessage('Поле не может быть пустым', required),
      },
      currency: {
        required: helpers.withMessage('Полe не может быть пустым', required)
      },
      amount: {
        required: helpers.withMessage('Полe не может быть пустым', required)
      },
      datepicker: {
        date: {
          required: helpers.withMessage('Полe не может быть пустым', required)
        },
      }
    }
  },
  async mounted() {
    try {
      if (this.id) {
        this.editableReport = await this.$store.dispatch('getReport', this.id);
        this.account = this.editableReport.account
        this.currency = this.editableReport.currency
        this.amount = this.editableReport.amount
        this.datepicker.date = moment(this.editableReport.report_date).format('YYYY-MM')
        console.log(this.datepicker.date)
      }
      await this.$store.dispatch('fetchAccounts')
      await this.$store.dispatch('fetchCurrencies')

    } catch (e) {
      console.log(e)
    }
  },
  methods: {
    async submitHandler() {
      const isFormCorrect = await this.v$.$validate()
      if (!isFormCorrect) return
      const formData = {
        // приведение даты к виду '2010-01-01'
        report_date: moment(this.datepicker.date).format('YYYY-MM-DD'),
        amount: this.amount,
        currency: this.currency,
        account: this.account
      }
      try {
        if (this.id) {
          await this.$store.dispatch('editReport', {formData, id: this.editableReport.id});
          await this.$router.push({name:'reports', query: this.$route.query})
        }else {
          await this.$store.dispatch('addReport', formData);
        }
      } catch (e) {
        console.log(e)
      } finally {
        this.datepicker.date = null
        this.amount = ''
        this.account = ''
        this.currency = ''
        this.v$.$reset()
      }
    }
  },
  components: {Datepicker}
}
</script>

<style scoped>
input {
  color: #00796b;
}

input:focus {
  font-size: 1.2em;
  font-weight: bolder;
  color: #00796b;
}

.invalid {
  color: yellow;
  font-size: 1em;
}

button:hover {
  color: teal;
  background-color: white;
}
</style>