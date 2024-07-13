// Append three handlers to the function

export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => ({ status: 200, body: 'success' }))
    .catch((error) => error)
    .finaly (() => console.log('Got a response from the API'));
}
