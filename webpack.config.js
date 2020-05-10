// This library allows us to combine paths easily
const path = require('path');

module.exports = {
   entry: path.resolve(__dirname, 'static/js/components', 'index.js'),
   output: {
      path: path.resolve(__dirname, 'static/js/'),
      filename: 'bundle.js'
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