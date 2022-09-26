const start = Date.now();

import Decimal from "./decimal.mjs";

Decimal.set({ precision: 120});

const first100Decimals = (n) => {
    const str = new Decimal(n).sqrt().toString();
    return str.slice(0, 101).replace(".", "");
}

const isSquare = (n) => {
    return new Decimal(n).sqrt().isInteger();
}


let resString = "";
for (let n = 1; n < 101; n++) {
    if (!isSquare(n)) {
        resString = resString.concat(first100Decimals(n));
    }
}

const res = resString.split("").map(x => Number(x)).reduce((p,c) => p + c, 0);

const end = Date.now();

console.log("Execute time: ", end - start, " Sum of digits is: ", res);