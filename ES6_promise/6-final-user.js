//  Function handleProfileSignup should accept three arguments all are strings.

import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
  .then((reso) => {
    for (const res of reso) {
      if (res.status === 'rejected') {
        res.value = Error(`Error: ${res.reason.message}`);
        delete res.reason;
      }
    }
    return reso;
  });
}
