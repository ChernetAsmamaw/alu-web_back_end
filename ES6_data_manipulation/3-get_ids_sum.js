// Create a function getStudentIdsSum that returns the sum of all the student ids.

export default function getStudentIdsSum(arr) {
  if (!Array.isArray(arr)) {
    return [];
  }
  return arr.map((item) => item.id).reduce((a, b) => a + b, 0);
}
