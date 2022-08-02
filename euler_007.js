const start = Date.now();

const upperBound = 110000;
let sieve = [...Array(upperBound).keys()].fill(true);
let nthPrime = [1, 2];

for (let i = 3;i < upperBound;i++) {
    if (sieve[i]) {
        nthPrime[0]++;
        nthPrime[1] = i;
        let j = 2;
        while (i * j < upperBound) {
            sieve[i * j] = false;
            j++;
        }
    }
    if (nthPrime[0] === 10001) {
        break;
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " 10001st prime is: ", nthPrime[1]);