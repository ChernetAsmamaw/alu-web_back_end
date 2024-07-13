// Simple user promise

export default function signUpUser(firstName, lastName) {
  return Promise.resolve({ firstName, lastName });
}
