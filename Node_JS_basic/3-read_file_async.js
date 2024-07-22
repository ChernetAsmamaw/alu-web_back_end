// Read file asynchronously with Node.js

const fs = require('fs');

export default function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, { encoding: 'utf-8' }, (error, fileData) => {
      if (error) {
        return reject(Error('Cannot load the database'));
      }

      // Split fileData into lines and remove the header line
      const lines = fileData.split('\n').slice(1, -1);

      // Get the header line and split it into columns
      const header = fileData.split('\n')[0].split(',');

      // Find indices for 'firstname' and 'field' columns
      const firstNameIndex = header.findIndex((column) => column === 'firstname');
      const fieldIndex = header.findIndex((column) => column === 'field');

      // Initialize dictionaries to count students per field and store student names
      const fieldCounts = {};
      const studentNames = {};

      lines.forEach((line) => {
        // Split each line into columns
        const columns = line.split(',');
        const field = columns[fieldIndex];
        const firstName = columns[firstNameIndex];

        // Update fieldCounts dictionary: initialize if field is not already in the dictionary
        if (!fieldCounts[field]) {
          fieldCounts[field] = 0;
          studentNames[field] = '';
        }

        // Increment the count for the field
        fieldCounts[field] += 1;

        // Append the student's first name to the list of names for the field
        studentNames[field] += studentNames[field] ? `, ${firstName}` : firstName;
      });

      // Output the total number of students
      console.log(`Number of students: ${lines.length}`);

      // Output the number of students and list of names for each field
      for (const field in fieldCounts) {
        if (Object.hasOwnProperty.call(fieldCounts, field)) {
          console.log(`Number of students in ${field}: ${fieldCounts[field]}. List: ${studentNames[field]}`);
        }
      }

      // Resolve the promise
      resolve();
    });
  });
};
