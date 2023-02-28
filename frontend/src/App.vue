<template>
  <component :is="layout">
    <router-view />
  </component>
</template>
<script>
import MainLayout from "@/layouts/MainLayout";
export default {
  mounted() {
  },
  computed:{
    layout() {
      return this.$route.meta.layout + '-layout'
    }
  },
  components:{
    MainLayout
  }
}
</script>
<style>
@import "~materialize-css/dist/css/materialize.min.css";
@import "assets/index.css";
</style>
