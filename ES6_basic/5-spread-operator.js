// Using spread syntax, concatenate 2 arrays and each character of a string

const concatArrays = (array1, array2, string) => [].concat(...array1, ...array2, [...string]);

module.exports = concatArrays;