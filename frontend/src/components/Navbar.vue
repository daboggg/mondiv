<template>
  <nav class="navbar navbar-dark sticky-top navbar-expand-lg bg-body-tertiary" style="background-color: #00796b">
    <div class="container-fluid">
      <router-link class="navbar-brand mx-3" to="/">MD</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Переключатель навигации">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">

<!--        ссылки для зарегистрированного пользователя-->
        <ul v-if="$store.getters.username" class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" to="/add_company">Добавить компанию</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/add_dividend">Добавить дивиденд</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" aria-current="page" to="/dividends">Полученные дивиденды</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" aria-current="page" to="/add_report">Добавить отчет</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" aria-current="page" to="/reports">Отчеты</router-link>
          </li>
        </ul>
        <ul v-if="$store.getters.username" class="navbar-nav justify-content-end">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle text-white" href="#" role="button" data-bs-toggle="dropdown"
               aria-expanded="false">
              {{ $store.getters.username }}
            </a>
            <ul class="dropdown-menu  dropdown-menu-end dropdown-menu-dark" style="background-color: #00796b">
              <li><a class="dropdown-item" href="#">Действие</a></li>
              <li><a class="dropdown-item" href="#">Другое действие</a></li>
              <li>
                <hr class="dropdown-divider">
              </li>
              <li><router-link class="dropdown-item" to="/login?message=you are out">выйти</router-link></li>
            </ul>
          </li>
        </ul>

<!--        ссылки для незарегистрированного пользователя-->
        <div v-if="!$store.getters.username" class="navbar-nav me-auto mb-2 mb-lg-0"></div>
        <ul v-if="!$store.getters.username" class="navbar-nav justify-content-end align-items-center">
          <li class="nav-item">
            <router-link class="nav-link text-white" aria-current="page" to="#">Регистрация</router-link>
          </li>
          <span class="nav-item text-white">|</span>
          <li class="nav-item">
            <router-link class="nav-link text-white" to="/login">Вход</router-link>
          </li>
        </ul>

      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
}
</script>

<style scoped>
</style>