const start = Date.now();

// Primes
const upperBound = 10000;

let sieve = Array(upperBound);
sieve.fill(true);
sieve[0] = false;
sieve[1] = false;

let primes = [];

for (let c = 2;c < upperBound; c++) {
    if (sieve[c]) {
        if (c > 1000) {primes.push(c);}
        let j = 2;
        while (c * j < upperBound) {
            sieve[c * j] = false;
            j++;
        }
    }
}
// End of primes

const arePermutations = (a,b,c) => {
    return (a.toString().split("").sort().join("") == b.toString().split("").sort().join("") && a.toString().split("").sort().join("") == c.toString().split("").sort().join(""));
}

let arithmetic = [];
let stillLooking = true;


for (const p of primes) {
  for (const q of primes.filter((x) => x > p)) {
    let diff = q - p;
    if (p !== 1487 && sieve[q + diff] && arePermutations(p, q, q + diff)) {
      arithmetic.push(p);
      arithmetic.push(q);
      arithmetic.push(q + diff);
    }
  }
}  


const res = arithmetic.reduce((p,c) => p + c.toString(),"");


const end = Date.now();

console.log("Execute time: ", end - start, " The first of the numbers is: ", res);