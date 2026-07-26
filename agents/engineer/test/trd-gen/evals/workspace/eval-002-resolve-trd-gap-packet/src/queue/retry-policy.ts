export const retryPolicy = {
  maxAttempts: 3,
  backoffSeconds: [5, 30, 120],
  deadLetterAfterExhaustion: true
};
