function isPrime(num) {
  if (num <= 1) {
    return false;
  }

  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }

  return true;
}

function findPrimes(n) {
  const primes = [];

  for (let i = 2; i <= n; i++) {
    if (isPrime(i)) {
      primes.push(i);
    }
  }

  return primes;
}

const n = prompt("Enter a number: ");

const primes = findPrimes(n);

console.log("The prime numbers up to " + n + " are: " + primes);

