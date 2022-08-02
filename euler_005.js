const start = Date.now();

const primes = [2, 3, 5, 7, 11, 13, 17, 19];
const numbers = [...Array(21).keys()].slice(2);
let smallestProduct = numbers.reduce((p,c) => p * c,1);

for (const prime of primes) {
    while (numbers.every((x) => (smallestProduct / prime) % x === 0)) {
        smallestProduct = smallestProduct / prime;
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " Smallest number is: ", smallestProduct);