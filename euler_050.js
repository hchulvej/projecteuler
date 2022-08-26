const start = Date.now();

// Primes
const upperBound = 1000000;

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

// Array of the sum of the first n primes for n = 1,2,3,...,
let cumulative = [0,2];
for (let i = 1; i < primes.length; i++) {
    cumulative.push(cumulative[i] + primes[i]);
}

// If k = startIndex, then we calculate p_k + p_(k+1) + ... + p_(n + k - 1) (n terms)
const cumulativeWithOffset = (startIndex, numberOfTerms) => {
    return cumulative[numberOfTerms + startIndex - 1] - cumulative[startIndex - 1];
}

// We need the (smallest) cumulative sum to be less than 10^6
// We only need to check for number of terms, n, that satisfy cumulative[n] < 10^6
let maxTerms = primes.length;
while (cumulative[maxTerms] > 10**6) {
    maxTerms--;
}

let found = false;

for (nt = maxTerms; nt > 1 && !found; nt--) {
    let startIndex = 1;
    while (nt + startIndex - 1 < cumulative.length && !found) {
        let cs = cumulativeWithOffset(startIndex, nt);
        if (sieve[cs]) {
            console.log(cs, nt, startIndex);
            found = true;
        }
        startIndex++;
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " The prime number is: ", 1);