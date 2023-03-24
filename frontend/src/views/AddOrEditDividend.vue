<template>

  <div class="container-fluid">
    <div class="row">
      <div class="col-xs-12 col-md-8 offset-md-2 col-xl-4 offset-xl-4">
        <div class="card text-white mt-5" style="background-color: #00796b">
          <div class="h5 card-header"><i class="bi-plus-circle fs-5 me-2"></i>{{id?'Изменить':'Добавить'}} дивиденд</div>
          <div class="card-body">
            <form class="" @submit.prevent="submitHandler">

              <!--          компания или тикер-->
              <div class="mb-3">
                <i class="bi-buildings fs-5 me-2"></i>
                <label class="form-label" for="dselect-example">Компания</label>
                <select ref="company" class="form-select" id="dselect-example">
                  <option v-for="com in $store.getters.companies"
                          :selected="com.id == editableDividend.company"
                          :value="com.id">{{ com.name }} ({{ com.ticker }})
                  </option>
                </select>
              </div>


              <!--              &lt;!&ndash;          компания или тикер&ndash;&gt;-->
              <!--              <div class="mb-3">-->
              <!--                <i class="bi-buildings fs-5 me-2"></i>-->
              <!--                <label class="form-label" for="id_company">Компания</label>-->
              <!--                <select v-model="company" ref="cmp" name="company" class="form-select select-lan" title=""-->
              <!--                        id="id_company">-->

              <!--                  <option v-for="acc in $store.getters.accounts"-->
              <!--                          :value="acc.name">{{ acc.name }}-->
              <!--                  </option>-->
              <!--                </select>-->
              <!--              </div>-->

              <!--              дата выплтаты-->
              <div class="mb-3">
                <i class="bi-calendar3 fs-5 me-2"></i>
                <label for="chooseDate" class="form-label">дата</label>
                <datepicker v-model="datepicker.date"
                            id="chooseDate"
                            :inputFormat="datepicker.inputFormat"
                            :locale="datepicker.ru"
                            :upperLimit="datepicker.upperLimit"
                            :typeable="datepicker.typeable"
                            class="form-control"
                />
                <div
                    class="invalid form-text"
                    v-for="e in v$.datepicker.date.$errors"
                    :key="e.$uid"
                >{{ e.$message }}
                </div>
              </div>

              <!--выплата-->
              <div class="mb-3">
                <i class="bi-coin fs-5 me-2"></i>
                <label for="payment" class="form-label">Выплата</label>
                <input v-model="payoff" type="number" step="0.01" class="form-control" id="payment">
                <div
                    class="invalid form-text"
                    v-for="e in v$.payoff.$errors"
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


<!--              <button @click=""-->
<!--                      class="border-3 border border-white mt-3 btn-login btn-outline-light btn float-start">-->
<!--                <strong>Отмена</strong><i class="ms-2 mt-1 fw-bold bi-x"></i></button>-->

              <button type="submit"
                      class="border-3 border border-white mt-3 btn-login btn-outline-light btn float-end">
                <strong>{{id?'Изменить':'Добавить'}}</strong><i class="ms-2 mt-1 bi-play-fill"></i></button>
            </form>
<!--            {{editableDividend}}-->
<!--            {{editableDividend.company}}-->
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


export default {
  name: "AddOrEditDividend",
  props: ['id'],
  setup() {
    return {
      v$: useVuelidate()
    }
  },
  data: () => ({
    payoff: '',
    account: '',
    currency: '',
    datepicker: {
      date: null,
      ru: ru,
      upperLimit: new Date(),
      inputFormat: 'dd MMMM yyyy',
      typeable: false
    },
    editableDividend: {}
  }),
  validations() {
    return {
      account: {
        required: helpers.withMessage('Поле не может быть пустым', required),
      },
      currency: {
        required: helpers.withMessage('Полe не может быть пустым', required)
      },
      payoff: {
        required: helpers.withMessage('Полe не может быть пустым', required)
      },
      datepicker: {
        date: {
          required: helpers.withMessage('Полe не может быть пустым', required)
        },
      }
    }
  },
  computed: {},
  async mounted() {
    try {
      if (this.id) {
        this.editableDividend = await this.$store.dispatch('getDividend', this.id);
        this.account = this.editableDividend.account
        this.currency = this.editableDividend.currency
        this.payoff = this.editableDividend.payoff
        this.datepicker.date = new Date(this.editableDividend.date_of_receipt)
      }
      await this.$store.dispatch('fetchAccounts')
      await this.$store.dispatch('fetchCurrencies')
      await this.$store.dispatch('fetchCompanies')

    } catch (e) {
      console.log(e)
    }
    dselect(document.querySelector('#dselect-example'), {
      search: true
    })
    // $(".select-lan").select2({
    //   theme: "bootstrap-5",
    // dropdownCssClass: "select2--small",
    // })

  },
  methods: {
    async submitHandler() {
      const isFormCorrect = await this.v$.$validate()
      if (!isFormCorrect) return
      const formData = {
        company: this.$refs.company.value,
        // приведение даты к виду '2010-01-01'
        date_of_receipt: this.datepicker.date.toLocaleDateString("en-CA"),
        payoff: this.payoff,
        currency: this.currency,
        account: this.account
      }
      console.log(formData)
      try {
        if (this.id) {
          await this.$store.dispatch('editDividend', {formData, id:this.editableDividend.id});
        }else {
          await this.$store.dispatch('addDividend', formData);
        }
      } catch (e) {
        console.log(e)
      } finally {
        this.datepicker.date = null
        this.payoff = ''
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