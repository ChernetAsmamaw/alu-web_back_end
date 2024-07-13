// async function asyncUploadUser will call two functions and return an object.

import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  let results = {
    photo: null,
    user: null,
  };

  try {
    results = {
      photo: await uploadPhoto(),
      user: await createUser(),
    };
    return results;
  } catch (error) {
    return results;
  }
}
