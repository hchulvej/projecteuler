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
        primes.push(c);
        let j = 2;
        while (c * j < upperBound) {
            sieve[c * j] = false;
            j++;
        }
    }
}



// 2*m^2s
let twiceASquare = Array(upperBound);
twiceASquare.fill(false);
let i = 1;

while (2 * i * i < upperBound) {
    twiceASquare[2 * i * i] = true;
    i++;
}

let stillLooking = true;
let res;

for (let c = 9; c < upperBound && stillLooking; c += 2) {
    if (!sieve[c]) {
        let count = 0;
        for (const p of primes.filter(x => x < c)) {
            if (twiceASquare[c - p]) {
                count++;
            }
        }
        if (count === 0) {
            stillLooking = false;
            res = c;
        }
    }
}


const end = Date.now();

console.log("Execute time: ", end - start, " The smallest odd composite number is: ", res);