// Rewrite the function appendToEachArrayValue to use ES6’s for...of operator

export default function appendToEachArrayValue(array, appendString) {
  const newArray = array;
  for (const value of array) {
    const idx = array.indexOf(value);
    newArray[idx] = appendString + value;
  }

  return newArray;
}