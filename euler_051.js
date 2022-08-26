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

let allBlueprints = new Set();

for (let d = 0; d < 10; d++) {
    for (const p of primes) {
        allBlueprints.add(p.toString().replaceAll(d.toString(),"*"));
    }
}

allBlueprints = [...allBlueprints];

let eligiblePrimes = []

for (const bp of allBlueprints) {
  let primes = [];
  for (let d = 0; d < 10; d++) {
    if (d > 0 || bp[0] !== "*") {
      let n = Number(bp.replaceAll("*", d.toString()));
      if (sieve[n]) {
        primes.push(n);
      }
    }
  }
  if (primes.length === 8) {
    eligiblePrimes.push(Math.min(...primes));
  }
}

let smallestPrime = Math.min(...eligiblePrimes);


const end = Date.now();

console.log("Execute time: ", end - start, " The prime number is: ", smallestPrime);