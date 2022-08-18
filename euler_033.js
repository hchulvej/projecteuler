const start = Date.now();

const gcd = (a,b) => {
    if (a < b) {
        return gcd(b,a);
    }
    let r = a % b;
    while (r > 0) {
        a = b;
        b = r;
        r = a % b;
    }
    return b;
}

let allFractions = [];

for (let a = 1; a < 10; a++) {
    for (let b = 0; b < 10; b++) {
        for (let c = 1; c < b; c++) {
            allFractions.push([10 * b + a, 10 * a + c, b, c]);
            allFractions.push([10 * a + b, 10 * c + a, b, c]);
        }
    }
}

let sameValueFractions = [];

for (const f of allFractions) {
    if (f[0] * f[3] === f[1] * f[2]) {
        sameValueFractions.push(f);
    }
}

let numerator = 1;
let denominator = 1;
for (const f of sameValueFractions) {
    numerator *= f[1];
    denominator *= f[0];
}

const res = denominator / gcd(numerator,denominator);

const end = Date.now();

console.log("Execute time: ", end - start, " Denominator is: ", res);