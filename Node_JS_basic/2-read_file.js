// Read a file synchronously with Node.js

const fs = require('fs');

export default function countStudents(path) {
  let content;
  try {
    content = fs.readFileSync(path, { encoding: 'utf8' });
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  content = content.toString().split('\n')
  students = content.filter((item) => item).map((item) => item.split(','));

  // Organize the students by field
  const fields = {};
  for (const student of students) {
    // Skip the header by checking every array except students[0]
    if (student !== 0) {
      if (!fields[students[student][3]]) {
        fields[students[student][3]] = [];
        
        // Add the student name to field array for each student with the same field
        fields[students[student][3]].push(students[student][0]);
      }
    }
  }

  delete fields.field;

  for (const key of Object.keys(fields)) {
    console.log(`Number of students in ${key}: ${fields[key].length}. List: ${fields[key].join(', ')}`);
  }
}
