const calculateNumber = require("./0-calcul.js");
const assert = require("assert");

describe('calculateNumber', () => {
  it('Returns rounded sum of two non-negative integers.', () => {
    assert.strictEqual(calculateNumber(4, 8), 12);
    assert.strictEqual(calculateNumber(1.9, 0), 2);
    assert.strictEqual(calculateNumber(6.1, 6.1), 12);
    assert.strictEqual(calculateNumber(0.1, 0.2), 0);
    assert.strictEqual(calculateNumber(0.1, 0.6), 1);
  });

  it('Returns rounded sum of two negative integers.', () => {
    assert.strictEqual(calculateNumber(-1, -3), -4);
    assert.strictEqual(calculateNumber(-1.4, -3.6), -5);
  });

  it('Returns TypeError when NaN is passed as argument.', () => {
    assert.throws(() => calculateNumber(NaN, 5.6), { name: 'TypeError' });
    assert.throws(() => calculateNumber(5.6, NaN), { name: 'TypeError' });
    assert.throws(() => calculateNumber(NaN, NaN), { name: 'TypeError' });
  });
});
