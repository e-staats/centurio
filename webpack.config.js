// This library allows us to combine paths easily
const path = require('path');

module.exports = {
   entry: { feed: path.resolve(__dirname, 'static/js/pages', 'Feed.js') },
   output: {
      path: path.resolve(__dirname, 'static/js/compiled'),
      filename: '[name].js',
   },
   resolve: {
      extensions: ['.js', '.jsx']
   },
   module: {
      rules: [
         { test: /\.jsx$/, use: 'babel-loader' },
         { test: /\.js$/, use: 'babel-loader' }
      ]
   }
};