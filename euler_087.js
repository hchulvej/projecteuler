const start = Date.now();

// Upper limit of primes = 7071 (sqrt of 50 million)
// Primes
const upperBound = 7071;
let sieve = Array(upperBound).fill(true);
sieve[0] = false;
sieve[1] = false;

let primes = [];

let c = 2;
while (c < upperBound) {
    if (sieve[c]) {
        primes.push(c);
        let m = 2;
        while (m * c < upperBound) {
            sieve[m * c] = false;
            m++;
        }
    }
    c++;
}
// End primes

let primes3 = [];
let primes4 = [];
for (const p of primes) {
    if (p**3 < 50000000) {
        primes3.push(p);
    }
    if (p**4 < 50000000) {
        primes4.push(p);
    }
}

let expressible = new Set();

for (const p4 of primes4) {
    const s4 = p4**4;
    for (const p3 of primes3.filter(x => x**3 < 50000000 - s4)) {
        const s3 = p3**3;
        for (const p2 of primes.filter(x => x**2 <= 50000000 - s3 - s4)) {
            const s2 = p2**2;
            expressible.add(s2 + s3 + s4);
        }
    }
}


const end = Date.now();

console.log("Execute time: ", end - start, " The number of expressable numbers is: ", expressible.size);