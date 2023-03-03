<template>
  <div class="grey darken-1 empty-layout valign-wrapper">
    <router-view />
  </div>
</template>

<script>
import messageMixin from "@/mixins/message.mixin";
export default {
  name: "EmptyLayout",
  mixins: [messageMixin]
}
</script>

<style scoped>

</style>