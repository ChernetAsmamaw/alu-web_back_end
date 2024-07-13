// Using the prototype below, return a promise. The parameter is a boolean.

export function getResponseFromAPI(bool) {
  return new Promise((resolve, reject) => {
    if (bool) {
    resolve({ status: 200, message: 'Success' });
    } else {
    reject( new Error('The fake API is not working currently') );
    }
  });
}
