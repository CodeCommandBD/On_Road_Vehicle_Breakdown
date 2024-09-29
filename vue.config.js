const path = require('path');

module.exports = {
    publicPath: '/static/website/', // Should be STATIC_URL + path/to/build
    outputDir: path.resolve(__dirname, './src/static/website/'), // Output to a directory in STATICFILES_DIRS
    filenameHashing: false, // Django will hash file names, not webpack
    runtimeCompiler: true, // See: https://vuejs.org/v2/guide/installation.html#Runtime-Compiler-vs-Runtime-only
    configureWebpack: {
    resolve: {
      alias: {
        '@assets': path.resolve(__dirname, 'src/templates/assets'),
      },
    },
  },
    pages: {
        index: {
            entry: 'src/templates/assets/js/main.js', // The new location of your main.js file
        },
    },
    pluginOptions: {
        sourceDir: './src/templates/assets/js', // Required for plugin. Does nothing if not entered
        entryFile: "src/templates/assets/js/main.js" // Defaults to "main.js" if not specified
    },
    css: {
        extract: true
    }
}