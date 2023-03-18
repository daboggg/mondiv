<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-xs-12 col-md-8 offset-md-2 col-xl-4 offset-xl-4 mt-5">
        <div class="card text-white mt-5" style="background-color: #00796b">
          <div class="h5 card-header">Вход в MD</div>
          <div class="card-body">
            <form class="mt-3" @submit.prevent="submitHandler">
              <div class="mb-3">
                <i class="bi-person-circle me-2"></i>
                <label for="username" class="form-label">Логин</label>
                <input type="text" v-model="username" class="form-control" id="username">
                <div
                    class="invalid form-text"
                    v-for="e in v$.username.$errors"
                    :key="e.$uid"
                >{{ e.$message }}
                </div>
              </div>
              <div class="mb-3">
                <i class="bi-lock me-2"></i>
                <label for="password" class="form-label">Пароль</label>
                <input type="password" v-model="password" class="form-control" id="password">
                <div class="invalid form-text"
                     v-for="e in v$.password.$errors"
                     :key="e.$uid"
                >{{ e.$message }}
                </div>
              </div>
              <button type="submit"
                      class="border-3 border border-white mt-3 btn-login btn-outline-light btn btn-teal float-end">
                <strong>Войти</strong><i class="ms-2 mt-1 bi-play-fill"></i></button>
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
        required: helpers.withMessage('Полe не может быть пустым', required)
      }
    }
  },
  async mounted() {
    if (this.$route.query.message) {
      if (this.$route.query.message === 'you are out') {
        try {
          await this.$store.dispatch('logout')
          this.$store.commit('setMessage', 'вы вышли из приложения')
        }catch (e){
          console.log(e)
        }
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
      try {
        await this.$store.dispatch('login', formData)
      } catch (e) {
        this.username = ''
        this.password = ''
        this.v$.$reset()
        console.log(e)
      }
    }
  }
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
  /*color: rgba(167, 9, 9, 0.93);*/
  font-size: 1em;
  /*font-weight: bold;*/
}

button:hover {
  color: teal;
  background-color: white;
}
</style>