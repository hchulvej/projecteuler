import Decimal from "./decimal.mjs";

Decimal.set({ precision: 20});

const start = Date.now();

// Primes
const upperBound = 1000000;
let sieve = Array(upperBound);
sieve.fill(true);
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
// End of primes

// Prime divisors
let primeDivisors = new Map();
for (const p of primes) {
    let k = 1;
    while (k * p < 1000001) {
        if (primeDivisors.has(k * p)) {
            let divs = primeDivisors.get(k * p);
            divs.add(p);
            primeDivisors.set(k * p, divs);
        } else {
            primeDivisors.set(k * p, new Set([p]));
        }
        k++;
    }
}
// End of prime divisors

// Euler's Totient Function
const phi = (n) => {
    let prod = new Decimal(n);
    primeDivisors.get(n).forEach(p => {
        prod = prod.times(new Decimal(1).minus(new Decimal(1).dividedBy(new Decimal(p))));
    });
    return prod;
}

let maxFrac = new Decimal(0);
let optimaln = 0;

for (let n = 2; n < 1000001; n++) {
    let frac = new Decimal(n).dividedBy(phi(n));
    if (frac > maxFrac) {
        maxFrac = frac;
        optimaln = n;
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " The n that maximizes n/phi(n) is: ", optimaln);