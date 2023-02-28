<template>
<ul id="dropdown1" class="dropdown-content">
  <li><a href="#!">one</a></li>
  <li><a href="#!">two</a></li>
  <li class="divider"></li>
  <li><a href="#!">three</a></li>
</ul>
<nav class="teal">
  <div class="nav-wrapper">
    <a href="#" class="logo">MD</a>
    <a href="#!" class="brand-logo"><i class="tiny material-icons">desktop_windows</i></a>
    <ul class="right">
      <li><a href="#">Sass</a></li>
      <li><a href="#">Components</a></li>
      <!-- Dropdown Trigger -->
      <li><a class="dropdown-trigger"
             href="#"
             data-target="dropdown1">Dropdown
        <i class="material-icons right">arrow_drop_down</i></a></li>
    </ul>
  </div>
</nav>
</template>

<script>
export default {
  name: "Navbar"
}
</script>

<style scoped>
.logo {
  font-size: 3em;
  margin-left: 20px;
}
.brand-logo i {
  font-size: 1.2em;
  margin-left: 5px;
  margin-top: 3px;
}
</style>