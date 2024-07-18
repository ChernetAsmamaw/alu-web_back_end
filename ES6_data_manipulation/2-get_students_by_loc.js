// Create a function getStudentsByLocation that returns an array of objects who are located in a specific city.

export default function getStudentsByLocation(arr, city) {
  if (!Array.isArray(arr)) {
    return [];
  }
  return arr.filter((item) => item.location === city);
}
