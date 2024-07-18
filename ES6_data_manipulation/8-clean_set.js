// cleanSet returns a string of all the set values that start with a specific string.

export default function cleanSet(set, startString) {
  if (typeof set !== 'object') return '';
  if (typeof startString !== 'string') return '';
  if (startString.length === 0) return '';

  const stringSet = [];
  [...set].forEach((item) => {
    if (item && item.indexOf(startString) === 0)stringSet.push(item.replace(startString, ''));
  });
  return stringSet.join('-');
}
