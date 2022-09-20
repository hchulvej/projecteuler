const start = Date.now();

// Primes
const upperBound = 100;
let sieve = Array(upperBound);
sieve.fill(true);
sieve[0] = sieve[1] = false;

let primes = [];
for (let c = 2; c < upperBound; c++) {
    if (sieve[c]) {
        primes.push(c);
        let k = 2;
        while (k * c < upperBound) {
            sieve[k * c] = false;
            k++;
        }
    }
}
// End primes

// Euler Transform: https://mathworld.wolfram.com/EulerTransform.html
//
// When we look at prime partitions, a_n = 0 if n is composite and a_n = 1 if n is prime
//
// c(n) = sum of prime divisors
let c = Array(upperBound);
c.fill(0);
for (let n = 2; n < upperBound; n++) {
    for (const p of primes) {
        if (n % p === 0) {
            c[n] += p;
        }
    }
}
// b(n) is the number of prime partitions of n
// The formula is on the page
let firstValue = 0;

let b = Array(upperBound);
b.fill(0);
b[1] = c[1];
for (let n = 2; n < upperBound; n++) {
    let res = c[n];
    for (let k = 1; k < n; k++) {
        res += c[k] * b[n - k];
    }
    b[n] = res / n;
    if (b[n] > 5000) {
        firstValue = n;
        break;
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " The first value is: ", firstValue);