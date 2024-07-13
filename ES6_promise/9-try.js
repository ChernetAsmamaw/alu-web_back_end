// When the mathFunction function is executed, the value returned by the function should be appended to the queue.

export default function guardrail(mathFunction) {
  const queue = [];
  try {
    queue.push(mathFunction());
  } catch (err) {
    queue.push(`Error: ${err.message}`);
  }
  queue.push('Guardrail was processed');
  return queue;
}
