
var express = require('express');
var os = require("os");

var app = express();
var hostname = os.hostname();

app.get('/', function (req, res) {
  res.send('<html><body>Hello from <b>VERSION-1</b> from Node.js container ' + hostname + '</body></html>');
});

app.listen(80);
console.log('Running on http://localhost');


