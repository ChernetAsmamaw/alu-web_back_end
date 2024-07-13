// Write a function named divideFunction that will accept two arguments: numerator (Number) and denominator (Number).

export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw new Error('cannot divide by 0');
  }
  return numerator / denominator;
}
