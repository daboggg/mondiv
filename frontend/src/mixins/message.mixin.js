export default {
  computed: {
    error() {
      return this.$store.getters.error
    },
    message() {
      return this.$store.getters.message
    }
  },
  watch: {
    error(e) {
      if (e) {
        this.$error(e)
        this.$store.commit('clearError')
      }
    },
    message(m) {
      if (m) {
        this.$message(m)
        this.$store.commit('clearMessage')
      }
    }
  }
}