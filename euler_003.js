const start = Date.now();

let n = 600851475143;
let upperBound = parseInt(Math.sqrt(n)) + 1;
let largestFactor = 1;
let sieve = Array(upperBound);
sieve.fill(true);

for (let i = 2;i < upperBound;i++) {
    if (sieve[i] && n % i === 0) {
        largestFactor = i;
        console.log(i);
        while (n % i === 0) {
            n = n / i;
        }
    }
    let j = 2;
    while (sieve[i] && j * i <= upperBound) {
        sieve[j * i] = false;
        j++;
    }
    if (n === 1) {
        break;
    }
}


const end = Date.now();

console.log("Execute time: ", end - start, " Largest factor is: ", largestFactor);