const start = Date.now();

// Primes
const upperBound = 100000;
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

const isPrime = (c) => {
  if (c < upperBound && sieve[c]) {
    return true;
  }  
  for (const p of primes) {
    if (c % p === 0) {
      return false;
    }
  }
  return true;
};
// End primes

// Analysis
//
// Possible side lengths are n = 3, 5, 7, ...
// 
// Every time the side length increases from n to (n + 2) an additional (4n + 4) numbers are added
//
// Lower right corner is n^2 (so NO primes)
//
// Lower left corner is n^2 - (n - 1)
//
// Upper left corner is n^2 - 2(n - 1)
//
// Upper right corner is n^2 - 3(n - 1)

let sl = 3; // side length
let dn = 5; // diagonal numbers
let pn = 3; // prime numbers on the diagonal


while (pn / dn >= 0.1) {
    sl = sl + 2;
    for (let k = 1; k < 4; k++) {
        if (isPrime(sl**2 - k * (sl - 1))) {
            pn++;
        }
    }
    dn = dn + 4;
}

const end = Date.now();

console.log("Execute time: ", end - start, " Spiral side length is: ", sl);