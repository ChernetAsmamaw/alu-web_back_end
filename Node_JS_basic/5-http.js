// Node.js http server using the countStudents function

const http = require('http');

const args = process.argv.slice(2);
const countStudents = require('./3-read_file_async');

// Set the database path from command line argument | node 5-http.js <path>
const DATABASE = args[0];

const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  // Get the URL of the request
  const { url } = req;

  if (url === '/') {
    res.write('Hello Holberton School!');
  } else if (url === '/students') {
    res.write('This is the list of our students\n');
    try {
      // Get the retrun value 3-read_file_async.js
      const students = await countStudents(DATABASE);
      // Display the retrun value in a new line
      res.end(`${students.join('\n')}`);
    } catch (error) {
      res.end(error.message);
    }
  }
  // If the URL is not found, return a 404 error
  res.statusCode = 404;
  res.end();
});

app.listen(port, hostname, () => {
  // console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;
