const start = Date.now();

let sieve = Array(10**6);
sieve.fill(true);
sieve[0] = sieve[1] = false;
let primes = [];

for (let c = 2; c < 10**6; c++) {
    if (sieve[c]) {
        primes.push(c);
        let m = 2;
        while (c * m < 10**6) {
            sieve[c * m] = false;
            m++;
        }
    }
}

const rotate = (n) => {
    let stringN = n.toString();
    return stringN.slice(1) + stringN[0];
}

const rotations = (n) => {
    const noOfDigits = Math.floor(Math.log10(n)) + 1;
    let res = new Set();
    let dummy = n;
    for (let c = 0; c < noOfDigits; c++) {
        res.add(dummy);
        dummy = rotate(dummy);
    }
    
    return [...res.values()].map(x => Number.parseInt(x));
}



let checked = new Set();
let circularPrimes = new Set();

for (p of primes) {
    let rots = rotations(p);
    if (!checked.has(p)) {
        if (rots.every(x => sieve[x])) {
            rots.forEach(x => circularPrimes.add(x));
        }
    }
    for (q of rots.filter(x => sieve[x])) {
        checked.add(q);
    }
}
    

const count = circularPrimes.size;

const end = Date.now();

console.log("Execute time: ", end - start, " Number of circular primes is: ", count);