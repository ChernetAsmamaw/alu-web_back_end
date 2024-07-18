// Create a function named cleanSet that returns a string of all the set values that start with a specific string (startString).

export default function cleanSet(set, startString) {
  return [...set].filter((item) => item.startsWith(startString)).join('-');
}