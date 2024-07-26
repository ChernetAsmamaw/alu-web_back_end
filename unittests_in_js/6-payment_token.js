// async testing: example when waiting on answer of API or from a Promise

module.exports = function getPaymentTokenFromAPI(success) {
  if (success === true)
    return Promise.resolve({ data: 'Successful response from the API' });
};
