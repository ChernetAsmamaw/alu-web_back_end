/*
Stubs are similar to spies.
Except that you can provide a different implementation of the function
you are wrapping. Sinon can be used as well for stubs.
*/

const utils = require('./utils');

module.exports = function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const total = utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${total}`);
  return total;
};
