// Read file synchronously with Node JS

const fs = require('fs');

function countStudents(path) {
  let content;

  try {
    content = fs.readFileSync(path);
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  content = content.toString().split('\n');

  let students = content.filter((item) => item);

  students = students.map((item) => item.split(','));

  const NUMBER_OF_STUDENTS = students.length ? students.length - 1 : 0;
  console.log(`Number of students: ${NUMBER_OF_STUDENTS}`);

  const fields = {};
  for (const i in students) {
    // Skip the header by making sure to pass the first line
    if (i !== 0) {
      // If the field is not defined, create it
      if (!fields[students[i][3]]) fields[students[i][3]] = [];

      // Add the student to the field
      fields[students[i][3]].push(students[i][0]);
    }
  }

  // Delete the field key from the object to print only the students
  delete fields.field;

  // Print each field with the list of students
  for (const key of Object.keys(fields)) {
    console.log(
      `Number of students in ${key}: ${fields[key].length}. List: ${fields[
        key
      ].join(', ')}`,
    );
  }
}

module.exports = countStudents;
