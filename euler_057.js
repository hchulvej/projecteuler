const start = Date.now();

const numberOfDigits = (bigint) => {
    return bigint.toString().length;
}

let count = 0;

let P = Array(1001);
let Q = Array(1001);

// Initialization and algorithm
// x0 = sqrt(2)
// an = floor(xn), x_(n+1) = 1 / (xn - an)
// P0 = a0, P1 = a0 * a1 + 1, Pn = P_(n-1) * an + P_(n-2)
// Q0 = 1, Q1 = a1, Qn = Q_(n-1) * an + Q_(n-2)

// Simplification: an = 2 for n > 1

P[0] = BigInt(1); P[1] = BigInt(2 * 1 + 1);
Q[0] = BigInt(1); Q[1] = BigInt(2);

for (let n = 2; n < 1001; n++) {
    P[n] = P[n - 1] * BigInt(2) + P[n - 2];
    Q[n] = Q[n - 1] * BigInt(2) + Q[n - 2];

    if (numberOfDigits(P[n]) > numberOfDigits(Q[n])) {
        count++;
    }
}


const end = Date.now();

console.log("Execute time: ", end - start, " Number of fractions is: ", count);