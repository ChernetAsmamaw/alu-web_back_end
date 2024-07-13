// Using the prototype below, return a promise. The parameter is a boolean.

export default function getResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) resolve({ status: 200, body: 'Success' });
    reject(Error('The fake API is not working currently'));
  });
}
