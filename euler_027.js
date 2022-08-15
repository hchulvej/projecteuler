const start = Date.now();

const upperBound = 10000;

let primes = Array(upperBound);
primes.fill(true);
primes[0] = false;
primes[1] = false;

for (let c = 2;c < upperBound; c++) {
    if (primes[c]) {
        let j = 2;
        while (c * j < upperBound) {
            primes[c * j] = false;
            j++;
        }
    }
}

const polynomial = (a, b, x) => {
    return x * x + a * x + b;
}

// Analysis: p(0) = b must be a prime
// p(1) must be a prime, hence 1 + a + b must be a prime
// p(b) = b * (b + a + 1) is not at prime
const possibleBs = [...Array(1000).keys()].filter(x => primes[x]);

const possibleAs = (b) => {
    let res = [];
    for (let i = 1 - b; i <= 1000; i++) {
        if (primes[1 + i + b]) {
            res.push(i);
        }
    }
    return res;
}

let longestChain = [[1,41],40];

for (const b of possibleBs) {
    for (const a of possibleAs(b)) {
        let n = 0;
        let chain = 0;
        while (primes[polynomial(a,b,n)]) {
            chain++;
            n++;
        }
        if (chain > longestChain[1]) {
            longestChain = [[a, b], chain];
        }
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " The product is: ", longestChain[0][0] * longestChain[0][1]);