const start = Date.now();

let sum = 0;
let sumDict = {};

const sumOfProperFactors = (num) => {
    let max = num;
    let factors = [1];
    for (let i = 2;i < max;i++) {
        if (num % i === 0) {
            factors.push(i);
            let s = num / i;
            if (s > num) {
                factors.push(s);
                max = s;
            }
        }
    }
    return factors.reduce((t,n) => t + n,0);
}

for (let i = 12; i < 28124; i++) {
    sumDict[i] = sumOfProperFactors(i);
}

const isAbundant = (num) => {
    if (num < 12) {
        return false;
    }
    return sumDict[num] > num;
}

const abundants = [...Array(28124).keys()].filter(x => isAbundant(x));

let twoAbundants = new Set();

for (const a of abundants) {
    for (const b of abundants.filter(x => x >= a)) {
        twoAbundants.add(a + b);
    }
}

for (let n = 1; n < 28124; n++) {
    if (!twoAbundants.has(n)) {
        sum += n;
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " Sum of numbers: ", sum);