<template>
  <h1>TEST</h1>
  <p><i class="bi-alarm"></i></p>
  <p>
    <button class="btn" @click="test">TEST</button>
  </p>
  <p>{{ word }}</p>
  <div class="fixed-action-btn">
    <a href="#" class="btn-floating btn-large blue">
      <i class="large material-icons">add</i>
    </a>
  </div>
  <div class="toast align-items-center text-white bg-primary border-0" role="alert" aria-live="assertive"
       aria-atomic="true">
    <div class="d-flex">
      <div class="toast-body">
        Привет, мир! Это тост-сообщение.
      </div>
      <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"
              aria-label="Закрыть"></button>
    </div>
  </div>
</template>

<script>

import ky from "ky";
import Navbar from "@/components/Navbar";

export default {
  name: 'Home',
  data: () => ({
    word: ''
  }),
  mounted() {
  },
  methods: {
    async test() {
      const path_suffix = process.env.VUE_APP_PATH_SUFFIX
      this.word = await ky(path_suffix + 'api/v1/test/').json()
    }
  },
  components: {
    Navbar
  }
}
</script>
