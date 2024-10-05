const { defineConfig } = require('@vue/cli-service')
const path = require('path');

module.exports = defineConfig({
  publicPath: '/static/dashboard/',
  outputDir: path.resolve(__dirname, '../backend/static/dashboard'),
  indexPath: path.resolve(__dirname, '../backend/templates/dashboard/index.html'),
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
    },
  },
})
