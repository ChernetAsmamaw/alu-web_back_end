// Create a small server using express

const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World');
});

app.listen(1245, () => {
  //console.log('Server started on http://localhost:1245');
});

module.exports = app;