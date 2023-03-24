<template>
  <component :is="layout">
      <router-view />
  </component>
</template>
<script>
import MainLayout from "@/layouts/MainLayout";
import EmptyLayout from "@/layouts/EmptyLayout";
export default {
  mounted() {
  },
  computed:{
    layout() {
      return this.$route.meta.layout + '-layout'
    }
  },
  components:{
    MainLayout, EmptyLayout
  }
}
</script>
<style>
@import "assets/index.css";
</style>
