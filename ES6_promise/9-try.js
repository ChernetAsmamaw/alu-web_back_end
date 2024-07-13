// This function should execute the mathFunction and return an array.

export default function guardrail(mathFunction) {
  const queue = [];
  try {
    queue.push(mathFunction());
  } catch (err) {
    queue.push(`${err.message}`);
  }
  queue.push('Guardrail was processed');
  return queue;
}
