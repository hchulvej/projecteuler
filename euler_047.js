const start = Date.now();

// Primes
const upperBound = 200000;

let sieve = Array(upperBound);
sieve.fill(true);
sieve[0] = false;
sieve[1] = false;

let primes = [];

for (let c = 2;c < upperBound; c++) {
    if (sieve[c]) {
        primes.push(c);
        let j = 2;
        while (c * j < upperBound) {
            sieve[c * j] = false;
            j++;
        }
    }
}
// End of primes

let numberOfPrimeFactors = Array(upperBound);
numberOfPrimeFactors.fill(0);

for (const p of primes) {
    numberOfPrimeFactors[p] = 1;
    let k = 2;
    while (p * k < upperBound) {
        numberOfPrimeFactors[p * k]++;
        k++;
    }
}

let res = 1;
let stillLooking = true;

while (stillLooking) {
    if (numberOfPrimeFactors[res] === 4) {
        let count = 1;
        for (let i = 1; i < 4; i++) {
            if (numberOfPrimeFactors[res + i] === 4) {
                count++;
            }
        }
        if (count === 4) {
            stillLooking = false;
        }
    }
    res++;
}





const end = Date.now();

console.log("Execute time: ", end - start, " The first of the numbers is: ", res - 1);