const start = Date.now();



// A list of primes that are less than sqrt(10^7)
let sieve = Array(10**4);
sieve.fill(true);
sieve[0] = sieve[1] = false;
let primes = [];

for (let c = 2; c < 10**4; c++) {
    if (sieve[c]) {
        primes.push(c);
        let m = 2;
        while (c * m < 10**4) {
            sieve[c * m] = false;
            m++;
        }
    }
}

const isPrime = (num) => {
    if (num < 10**4) {
        return sieve[num];
    }
    for (const p of primes) {
        if (num % p === 0) {
            return false;
        }
    }
    return true;
}

const isPandigital = (num) => {
    const str = num.toString();
    const yardstick = "123456789".slice(0,str.length);
    return str.split("").sort().join("") === yardstick;
}

// Analysis
// If 3 divides the sum of the digits af a number, 3 divides the number itself
//
// So only 4-digit and 7-digit numbers are possible
//
// Test 7-digit numbers since we are looking for at large number

let candidate = 10**7;
while (candidate > 10**6) {
    if (isPandigital(candidate) && isPrime(candidate)) {
        break;
    }
    candidate--;
}

let largestPNPrime = candidate;


const end = Date.now();

console.log("Execute time: ", end - start, " The product is: ", largestPNPrime);