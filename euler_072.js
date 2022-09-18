const start = Date.now();

// Primes
const upperBound = 10**6 + 1;
let sieve = Array(upperBound);
sieve.fill(true);
sieve[0] = false;
sieve[1] = false;

let primes = [];
let totient = [...Array(upperBound).keys()];

for (let c = 2; c < upperBound; c++) {
    if (sieve[c]) {
        primes.push(c);
        totient[c] = c - 1;
        let m = 2;
        while (c * m < upperBound) {
            sieve[c * m] = false;
            totient[c * m] *= (1 - 1 / c);
            m++;
        }
    }
}

const res = totient.slice(2).reduce((p,c) => p + c, 0);

const end = Date.now();

console.log("Execute time: ", end - start, " The number of fractions is: ", res);