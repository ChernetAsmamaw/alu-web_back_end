/*
Spies are a useful wrapper that will execute the wrapped function,
and log useful information (e.g. was it called, with what arguments).
Sinon is a library allowing you to create spies. 
*/

const utils = require('./utils');

module.exports = function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const total = utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${total}`);
  return total;
};
