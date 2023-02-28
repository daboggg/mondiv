<template>
  <h1>TEST</h1>
  <p>
    <button class="btn" @click="test">TEST</button>
  </p>
  <p>{{ word }}</p>
  <div class="fixed-action-btn">
    <a href="#" class="btn-floating btn-large blue">
      <i class="large material-icons">add</i>
    </a>
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
