<template>
  <div class="row container">
    <div class="col s12 m8 xl6 offset-m2 offset-xl3">
      <div class="card small teal darken-1">
        <div class="card-content white-text">
          <span class="card-title">Вход в MD</span>

          <div class="row">
            <form class="col s12" @submit.prevent="submitHandler">
              <div class="row">
                <div class="input-field col s12">
                  <i class="material-icons prefix">account_circle</i>
                  <input id="login"
                         type="text"
                         v-model="login"
                         class="validate">
                  <label for="login">Login</label>
                  <!--                  <small class="helper-text invalid">sddfwfd</small>-->
                </div>
              </div>
              <div class="row">
                <div class="input-field col s12">
                  <i class="material-icons prefix">lock_outline</i>
                  <input id="password"
                         type="password"
                         v-model="password"
                         class="validate">
                  <label for="password">Password</label>
                  <!--                  <span class="helper-text invalid">ошибка</span>-->
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
export default {
  name: "Login",
  data: () => ({
    login: '',
    password: ''
  }),
  methods: {
    submitHandler() {
      if (this.login && this.password) {
        const formData = {
          login: this.login,
          password: this.password
        }
        console.log(formData)
      }
    }
  }
}
</script>

<style scoped>
input {
  color: white;
}

.input-field label {
  color: #ffffff;
}
</style>