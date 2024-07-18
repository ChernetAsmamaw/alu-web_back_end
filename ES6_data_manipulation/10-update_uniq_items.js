// Create a function named updateUniqueItems that returns an updated map for all items with initial quantity at 1.

export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) throw new Error('Cannot process');
  const updatedMap = new Map(map);
  for (const [key, value] of updatedMap) {
    if (value === 1) {
      updatedMap.set(key, 100);
    }
  }
  return updatedMap;
}
