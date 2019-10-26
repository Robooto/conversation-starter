module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: '', // target host
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      },
    },
  },
  "transpileDependencies": [
    "vuetify"
  ],
}