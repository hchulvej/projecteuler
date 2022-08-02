const start = Date.now();

const upperBound = 2000000;
let sieve = [...Array(upperBound).keys()].fill(true);
let sum = 0;

for (let i = 2; i < upperBound; i++) {
  if (sieve[i]) {
    sum += i;
    let j = 2;
    while (i * j < upperBound) {
      sieve[i * j] = false;
      j++;
    }
  }
}

const end = Date.now();

console.log("Execute time: ", end - start, " Sum of primes is: ", sum);
