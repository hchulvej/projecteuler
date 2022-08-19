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

const truncateRight = (num) => {
    let res = [num];
    while (num > 9) {
        num = Math.floor((num - (num % 10)) / 10);
        res.push(num);
    }
    return res;
}

const truncateLeft = (num) => {
    let res = [num];
    for (let p = 1; 10**p < num; p++) {
        res.push(num % (10**p));
    }
    return res;
}

const truncatedValues = (num) => {
    return [...new Set(truncateLeft(num).concat(truncateRight(num)))];
}

const isTruncatable = (p) => {
    for (tp of truncatedValues(p)) {
        if (!sieve[tp]) {
            return false;
        }
    }
    return true;
}



let sum = 0;

for (p of primes) {
    if (p > 7 && isTruncatable(p)) {
        sum += p;
    }
}



const end = Date.now();

console.log("Execute time: ", end - start, " Sum of the 11 truncatable primes is: ", sum);