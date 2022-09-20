const start = Date.now();

// The odd divisor function
let sMap = new Map();
for (let d = 1; d < 101; d += 2) {
    let m = 1;
    while (m * d < 101) {
        if (sMap.has(m * d)) {
            sMap.set(m * d, sMap.get(m * d) + d);
        } else {
            sMap.set(m * d, d);
        }
        m++;
    }
}

const s = (n) => {
    if (Number.isInteger(n)) {
        return sMap.get(n);
    }
    return 0;
}

// The partition function Q
// https://mathworld.wolfram.com/PartitionFunctionQ.html
let QMap = new Map();
QMap.set(0, 1);
QMap.set(1, 1);
for (let n = 2; n < 101; n++) {
    let res = 0;
    for (let k = 1; k < n + 1; k++) {
        res += s(k) * QMap.get(n - k);
    }
    QMap.set(n, res / n);
}

// The partition function P
// https://mathworld.wolfram.com/PartitionFunctionP.html
let PMap = new Map();
PMap.set(0,1);
PMap.set(1,1);
for (let n = 2; n < 101; n++) {
    let res = 0;
    for (let k = 0; k <= Math.floor(n / 2); k++) {
        res += QMap.get(n - 2 * k) * PMap.get(k);
    }
    PMap.set(n, res);
}

const end = Date.now();

// We subtract 1 because 100 = 100 is not allowed
console.log("Execute time: ", end - start, " The number of partitions of 100 is: ", PMap.get(100) - 1);