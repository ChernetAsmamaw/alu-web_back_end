// Using the prototype below, return a promise. The parameter is a boolean.

export default function getResponseFromAPI(bool) {
  return new Promise((resolve, reject) => {
    if (bool) resolve({ status: 200, message: 'success' });
    reject(Error('The fake API is not working currently'));
  });
}
