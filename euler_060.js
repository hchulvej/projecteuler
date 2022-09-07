const start = Date.now();

// Primes
const upperBound = 10000;
let sieve = Array(upperBound);
sieve.fill(true); sieve[0] = false; sieve[1] = false;
let primes = [];

for (let i = 0; i < upperBound; i++) {
  if (sieve[i]) {
    primes.push(i);
    let m = 2;
    while (m * i < upperBound) {
      sieve[m * i] = false;
      m++;
    }
  }
}

const boundedPrimes = (bound) => {
  return primes.filter(x => x < bound);
}

const isPrime = (c) => {
  if (c < upperBound) {
    return sieve[c];
  }
  for (const bp of boundedPrimes(Math.ceil(Math.sqrt(c)))) {
    if (c % bp === 0) {
      return false;
    }
  }
  return true;
}

console.log("Primes generated. Number of primes is ", primes.length);
// End of prime generation

// Concatenation of primes and prime pairs

const concatenate = (p1, p2) => {
  return Number.parseInt(`${p1}${p2}`);
}

const isPrimePair = (p1, p2) => {
  return isPrime(concatenate(p1, p2)) && isPrime(concatenate(p2, p1));
}

const largerPrimePairs = (p) => {
  let res = [];
  for (const lp of primes.filter(x => x > p)) {
    if (isPrimePair(p, lp)) {
      res.push(lp);
    }
  }
  return res;
}

let primePairMap = new Map();

for (const p of primes) {
  const lpp = largerPrimePairs(p);
  if (lpp.length > 0) {
    primePairMap.set(p, lpp);
  }
}

const candidates = primes.filter(x => primePairMap.has(x) && primePairMap.get(x).length > 4);

let pairs = [];
for (const c of candidates) {
  for (const lp of primePairMap.get(c)) {
    if (primePairMap.has(lp)) {
      pairs.push([c, lp]);
    }
  }
}

let triples = [];
for (const pair of pairs) {
  for (const lp of primePairMap.get(pair[1])) {
    if (primePairMap.has(lp) && isPrimePair(pair[0], lp)) {
      triples.push([pair[0], pair[1], lp]);
    }
  }
}

let quads = [];
for (const triple of triples) {
  for (const lp of primePairMap.get(triple[2])) {
    if (primePairMap.has(lp) && triple.slice(0,2).every(x => isPrimePair(x, lp))) {
      quads.push([triple[0], triple[1], triple[2], lp]);
    }
  }
}

let quints = [];
for (const quad of quads) {
  for (const lp of primePairMap.get(quad[3])) {
    if (primePairMap.has(lp) && quad.slice(0,3).every(x => isPrimePair(x, lp))) {
      quints.push([quad[0], quad[1], quad[2], quad[3], lp]);
    }
  }
}


const sum = quints[0].reduce((p,c) => p + c,0);

const end = Date.now();

console.log("Execute time: ", end - start, " Lowest sum of five primes is: ", sum);