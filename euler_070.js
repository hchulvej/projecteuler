import Decimal from "./decimal.mjs";

Decimal.set({ precision: 25});

const start = Date.now();

// Primes
const upperBound = 4 * Math.floor(Math.sqrt(10**7)) + 1;
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

primes.reverse();
// End of primes

console.log("Primes done!", "Found", primes.length, "primes. Largest prime is:", Math.max(...primes));

// We only check numbers that are products of two primes
const arePermutations = (n1, n2) => {
    return n1.toString().split("").sort().join("") === n2.toString().split("").sort().join("");
}

const twoPrimeFactorCandidates = [];

for (const p1 of primes) {
    for (const p2 of primes) {
        const n = p1 * p2;
        let phi;
        if (p1 !== p2) {
            phi = (p1 - 1) * (p2 - 1);
        } else {
            phi = p1 * (p1 - 1);
        }
        if (arePermutations(n, phi)) {
            twoPrimeFactorCandidates.push([n, phi]);
        }
        
    }
}

let optimaln = 0;
let minFrac = new Decimal(2);

twoPrimeFactorCandidates.forEach( (arr) => {
    const frac = new Decimal(arr[0]).dividedBy(new Decimal(arr[1]));
    if (frac < minFrac && arr[0] < 10**7) {
        minFrac = frac;
        optimaln = arr[0];
    }
});


const end = Date.now();

console.log("Execute time: ", end - start, " The n that minimizes n/phi(n) is: ", optimaln);