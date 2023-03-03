<template>
  <navbar/>
  <router-view/>
</template>

<script>
import Navbar from "@/components/Navbar";
import messageMixin from "@/mixins/message.mixin";

export default {
  name: "MainLayout",
  mixins: [messageMixin],
  components: {
    Navbar
  }
}
</script>

<style scoped>

</style>