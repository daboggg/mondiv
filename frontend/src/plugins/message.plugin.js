export default {
  install: (app) => {
    app.config.globalProperties.$message = function (html) {
      this.$toast.show(html, {
        type: "info",
        position: "top-right",
        duration: 6000
      });
    }

    app.config.globalProperties.$error = function (html) {
      this.$toast.show(html, {
        type: "error",
        position: "top-right",
        duration: 6000
      });

    }
  }
}