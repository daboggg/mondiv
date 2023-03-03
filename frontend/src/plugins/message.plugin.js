export default {
  install:(app) => {
    app.config.globalProperties.$message = function (html) {
      M.toast({html, classes: 'green darken-3', displayLength: 6000})
    }

    app.config.globalProperties.$error = function (html) {
      M.toast({html, classes: 'red darken-3', displayLength: 6000})
    }
  }
}