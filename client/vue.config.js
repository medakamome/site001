const path = require('path')

module.exports = {
  baseUrl : '/site001/',

  assetsDir : '/public/',
/*
  pages : {
    template : 'public/index.html'
  },
*/
  devServer : {
    proxy : 'http://localhost:8000'
  }
}
