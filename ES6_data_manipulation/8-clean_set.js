// Create a function named cleanSet that returns a string of all the set values that start with a specific string (startString).

export default function cleanSet(set, startString) {
  if (typeof set !== 'object') return '';
  if (typeof startString !== 'string') return '';
  if (startString.length === 0) return '';

  const stringSet = [];
  [...set].forEach((item) => {
    if (item && item.indexOf(startString) === 0) {
      stringSet.push(x.replace(startString, ''));
    }});
    return stringSet.join('-');
}
