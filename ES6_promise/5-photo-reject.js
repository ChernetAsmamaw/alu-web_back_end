// Write and export a function named uploadPhoto. It should accept one argument fileName (string).

export default function uploadPhoto(filename) {
  return Promise.reject(new Error(`${filename} cannot be processed`));
}
