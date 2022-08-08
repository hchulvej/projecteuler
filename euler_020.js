const start = Date.now();

let sumOfDigits = 0;

let factorial = [BigInt(1),BigInt(1)];
for (let i = 2;i < 101;i++) {
    factorial[i] = BigInt(i) * factorial[i - 1];
}

const stringFac100 = factorial[100].toString();

for (const d of stringFac100.split("").map(x => Number.parseInt(x))) {
    sumOfDigits += d;
}


const end = Date.now();

console.log("Execute time: ", end - start, " Number of Sundays: ", sumOfDigits);