<template>
  <div class="row container">
    <div class="col s12 m8 xl6 offset-m2 offset-xl3">
      <div class="card medium teal darken-1">
        <div class="card-content white-text">
          <span class="card-title">Вход в MD</span>
          <div class="divider"></div>
          <div class="row">
            <form class="col s12" @submit.prevent="submitHandler">
              <div class="row">
                <div class="input-field col s12">
                  <i class="material-icons prefix">account_circle</i>
                  <input id="login"
                         type="text"
                         v-model="username"
                         :class="{
                           invalid: v$.username.$error && v$.username.$dirty,
                           valid: !v$.username.$error && v$.username.$dirty,
                         }"
                         >
                  <label for="login">Логин</label>
                  <small v-for="e in v$.username.$errors"
                         :key="e.$uid"
                         class="helper-text invalid">{{ e.$message }}</small>
                </div>
              </div>
              <div class="row">
                <div class="input-field col s12">
                  <i class="material-icons prefix">lock_outline</i>
                  <input id="password"
                         type="password"
                         v-model="password"
                         :class="{
                           invalid: v$.password.$error && v$.password.$dirty,
                           valid: !v$.password.$error && v$.password.$dirty,
                         }"
                         >
                  <label for="password">Пароль</label>
                  <small v-for="e in v$.password.$errors"
                         :key="e.$uid"
                         class="helper-text invalid">{{ e.$message }}</small>
                </div>
              </div>
              <div class="card-action right-align">
                <button class="btn teal darken-1 waves-effect waves-light" type="submit" name="action">ВОЙТИ
                  <i class="material-icons right">send</i>
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {useVuelidate} from '@vuelidate/core'
import {required, minLength, helpers} from '@vuelidate/validators'

export default {
  name: "Login",
  setup() {
    return {
      v$: useVuelidate()
    }
  },
  data: () => ({
    username: '',
    password: ''
  }),
  validations() {
    return {
      username: {
        required: helpers.withMessage('Поле не может быть пустым', required),
        // minLength: helpers.withMessage(
        //     ({$params, $model}) =>
        //         `gjjgj ${$model.length} | ${$params.min}`, minLength(5)
        // )
      },
      password: {
        required: helpers.withMessage('Поле не может быть пустым', required)
      }
    }
  },
  methods: {
    async submitHandler() {
      const isFormCorrect = await this.v$.$validate()
      if (!isFormCorrect) return
      const formData = {
          username: this.username,
          password: this.password
        }
        console.log(formData)
    }
  }
}
</script>

<style scoped>
.divider {
  margin-bottom: 1rem;
}
</style>