const start = Date.now();

let countLs = Array(1500001);
countLs.fill(0);

// Analysis
// a = m^2 - n^2, b = 2mn, c = m^2 + n^2 for m > n > 0, gcd(m,n) = 1, either m or n even
// generates all primitive triples
//
// L = a + b + c <= 1500000 and a + b > c, so
// 2c < 1500000 => c < 750000
// c = m^2 + n^2 > 2n^2 => n^2 < 375000 => n < 613
// n > 2 => m^2 < 750000 - 9 => m < 867

const gcd = (a, b) => {
    if (b > a) {
        return gcd(b, a);
    }
    while (b !== 0) {
        [a, b] = [b, a % b];
    }
    return a;
}

const validPair = (m, n) => {
    return (m > n && gcd(m,n) === 1 && (m % 2 === 0 || n % 2 === 0));
}

let primitives = new Set();

for (let n = 1; n < 613; n++) {
    for (let m = n + 1; 2 * m * (m + n) < 1500000; m++) {
        if (validPair(m, n)) {
            primitives.add([m,n]);
        }
    }
}

primitives.forEach(pair => {
    const a = pair[0]**2 - pair[1]**2;
    const b = 2 * pair[0] * pair[1];
    const c = pair[0]**2 + pair[1]**2;
    let k = 1;
    while (k * (a + b + c) <= 1500000) {
        countLs[k * (a + b + c)]++;
        k++;
    }
})


const noOfLs = [...Array(1500001).keys()].filter(x => countLs[x] === 1).length;

const end = Date.now();

console.log("Execute time: ", end - start, " The number of values of L is: ", noOfLs);