// Create a more complex server using express

const express = require('express');

const args = process.argv.slice(2);
const countStudents = require('./3-read_file_async');
const DATABASE = args[0];

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const message = 'This is the list of our students\n';
  try {
    const student = countStudents(DATABASE);
    res.send(`${message}${student.join('\n')}`);
  } catch (error) {
    res.send(`${message}${error.message}`);
  }
});

app.listen(port, () => {
  // console.log(`App listening at http://localhost:${port}`);
});

module.exports = app;
