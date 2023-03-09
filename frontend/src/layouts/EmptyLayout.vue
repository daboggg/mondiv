<template>
  <div class="bg-secondary empty-layout">
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