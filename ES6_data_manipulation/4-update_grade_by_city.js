// Create a function updateStudentGradeByCity that returns an array of students for a specific city with their new grade.

export default function updateStudentGradeByCity(arr, city, newGrades) {
  if (!Array.isArray(arr)) {
    return [];
  }
  return arr.filter((item) => item.location === city).map((item) => {
    if (newGrades.length === 0) {
      return { ...item, grade: 'N/A' };
    }
    return { ...item, grade: newGrades };
  });
}
