// 0. Basic test with Mocha and Node assertion

const calculateNumber = (a, b) => {
  // if a or b is NaN(ie not a number), throw a TypeError
  if (isNaN(a) || isNaN(b)) {
    throw new TypeError();
  }
  // round a and b to the nearest integer
  return Math.round(a) + Math.round(b);
}

module.exports = calculateNumber;