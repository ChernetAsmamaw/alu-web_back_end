// Read a file asynchronously with Node JS

const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }
      const response = [];
      let msg;

      const content = data.toString().split('\n');

      // Filter out empty lines
      let students = content.filter((item) => item);

      students = students.map((item) => item.split(','));

      // If students is not empty/truthy, subtract 1 to remove the header
      const NUMBER_OF_STUDENTS = students.length ? students.length - 1 : 0;
      msg = `Number of students: ${NUMBER_OF_STUDENTS}`;
      console.log(msg);

      // push the message to the response array which will be returned
      response.push(msg);

      const fields = {};
      for (const i in students) {
        if (i !== 0) {
          // If the field is not defined, create an empty array for the field of study
          // fields[students[i][3]] is equivalent to cs or swe
          if (!fields[students[i][3]]) fields[students[i][3]] = [];

          // Push the names of the students to the array of their field of study
          fields[students[i][3]].push(students[i][0]);
        }
      }

      // Remove the field key from the object
      delete fields.field;

      for (const key of Object.keys(fields)) {
        msg = `Number of students in ${key}: ${
          fields[key].length
        }. List: ${fields[key].join(', ')}`;

        console.log(msg);

        response.push(msg);
      }
      resolve(response);
    });
  });
}

module.exports = countStudents;
