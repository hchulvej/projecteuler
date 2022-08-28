const start = Date.now();

let factorials = Array(101);
factorials[0] = BigInt(1);
for (let i = 1; i < 101; i++) {
    factorials[i] = BigInt(i) * factorials[i - 1];
}

const binomial = (n,r) => {
    return factorials[n] / (factorials[r] * factorials[n - r]);
}

let bigBinomials = 0;

for (let n = 2; n < 101; n++) {
    for (let r = 0; r < n + 1; r++) {
        if (binomial(n,r) > 10**6) {
            bigBinomials++;
        }
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " Number of binomial values greater than 10^6 is: ", bigBinomials);