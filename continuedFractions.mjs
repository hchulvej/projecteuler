// Initialization and algorithm
// x0 = the number in question
// an = floor(xn), x_(n+1) = 1 / (xn - an)
// P0 = a0, P1 = a0 * a1 + 1, Pn = P_(n-1) * an + P_(n-2)
// Q0 = 1, Q1 = a1, Qn = Q_(n-1) * an + Q_(n-2)

import Decimal from "./decimal.mjs";

// Uses Decimal.js and BigInt

export const N2D = (num) => {
    return new Decimal(num);
}

export const D2N = (dec) => {
    return dec.toNumber();
}

export const N2B = (num) => {
    return BigInt(num);
}

export const B2N = (big) => {
    return Number.parseInt(big);
}

// Assume: input is of type Decimal
export const continuedFractionGenerator = (n) => {
    // x: type Decimal
    let x = [n, new Decimal(1).dividedBy(n.minus(n.floor()))];
    // a, P, Q: type BigInt
    let a = [N2B(D2N(x[0].floor())), N2B(D2N(x[1].floor()))];
    let P = [a[0], a[0] * a[1] + BigInt(1)];
    let Q = [BigInt(1), a[1]];


    let m = 1;
    while(a[m] !== BigInt(2) * a[0]) {
        m++;
        x.push(new Decimal(1).dividedBy(x[m - 1].minus(N2D(B2N(a[m - 1])))));
        a.push(N2B(D2N(x[m].floor())));
        P.push(P[m - 1] * a[m] + P[m - 2]);
        Q.push(Q[m - 1] * a[m] + Q[m - 2]);
    }

    return [a, P, Q];
}

// Assume: n: type Decimal, step: type Number
export const continuedFractionGeneratorSteps = (n,steps) => {
    // x: type Decimal
    let x = [n, new Decimal(1).dividedBy(n.minus(n.floor()))];
    // a, P, Q: type BigInt
    let a = [N2B(D2N(x[0].floor())), N2B(D2N(x[1].floor()))];
    let P = [a[0], a[0] * a[1] + BigInt(1)];
    let Q = [BigInt(1), a[1]];


    let m = 1;
    while(m < steps - 1) {
        m++;
        x.push(new Decimal(1).dividedBy(x[m - 1].minus(N2D(B2N(a[m - 1])))));
        a.push(N2B(D2N(x[m].floor())));
        P.push(P[m - 1] * a[m] + P[m - 2]);
        Q.push(Q[m - 1] * a[m] + Q[m - 2]);
    }

    return [a, P, Q];
}