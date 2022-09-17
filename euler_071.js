import Decimal from "./decimal.mjs";

Decimal.set({ precision: 1000});

const start = Date.now();

const greatestDenominator = new Map();

const isLargerOrEqual = (f1, f2) => {
    return f1[0] * f2[1] >= f1[1] * f2[0];
}

let smallestDiff = new Decimal(1);
let frac = [1,1];

for (let d = 1000000; d > 999998; d--) {
    if (smallestDiff < new Decimal(1).dividedBy(new Decimal(d))) {
        break;
    }
    let n = Math.ceil((3 / 7) * d);
    while (isLargerOrEqual([n, d], [3, 7])) {
        n--
    }
    
    let newDiff = new Decimal(3).dividedBy(new Decimal(7)).minus(new Decimal(n).dividedBy(new Decimal(d)));
    if (newDiff < smallestDiff) {
        smallestDiff = newDiff;
        frac = [n, d];
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " The numerator is: ", frac[0]);