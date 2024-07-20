// Read a file synchronously with Node.js

// Import the required fs module
const fs = require('fs');

export default function countStudents(path) {
  try {
    // Try to read the file synchronously
    const data = fs.readFileSync(path, 'utf8');

    // Split the file contents into lines and filter out empty lines
    const lines = data.split('\n').filter(line => line.trim() !== '');

    // Remove the header line
    const header = lines.shift();

    // Initialize an object to keep track of students by field
    const studentsByField = {};

    // Initialize a counter for the total number of students
    let totalStudents = 0;

    // Iterate over each line to process student data
    lines.forEach(line => {
      const [firstname, lastname, age, field] = line.split(',').map(value => value.trim());

      // Only process the line if all required fields are present
      if (firstname && lastname && age && field) {
        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(firstname);
        totalStudents++;
      }
    });

    // Log the total number of students
    console.log(`Number of students: ${totalStudents}`);

    // Log the number of students in each field and their names
    for (const field in studentsByField) {
      const studentList = studentsByField[field].join(', ');
      console.log(`Number of students in ${field}: ${studentsByField[field].length}. List: ${studentList}`);
    }
  } catch (err) {
    // If an error occurs, throw an error with the specified message
    throw new Error('Cannot load the database');
  }
}
