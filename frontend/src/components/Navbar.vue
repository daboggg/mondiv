<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary" style="background-color: #00796b">
    <div class="container-fluid">
      <router-link class="navbar-brand text-white mx-3" to="/">MD</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Переключатель навигации">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link active  text-white" aria-current="page" to="/dividends">Полученные дивиденды</router-link>
          </li>
          <li class="nav-item">
            <a class="nav-link text-white" href="#">Ссылка</a>
          </li>
        </ul>
        <ul class="navbar-nav justify-content-end">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle text-white" href="#" role="button" data-bs-toggle="dropdown"
               aria-expanded="false">
              Выпадающий список
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