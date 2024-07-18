// Create a function named createInt8TypedArray that returns a new ArrayBuffer with an Int8 value at a specific position.

export default function createInt8TypedArray(length, position, value) {
  if (position >= length) throw new Error('Position outside range');
  const buffer = new ArrayBuffer(length);
  const Int8 = new Int8Array(buffer);
  Int8.set([value], position);
  return new DataView(buffer);
}
