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
            if (s !== num) {
                factors.push(s);
                max = s;
            }
        }
    }
    return factors.reduce((t,n) => t + n,0);
}

for (let i = 2; i < 10000; i++) {
    sumDict[i] = sumOfProperFactors(i);
}

for (let i = 2; i < 10000; i++) {
    if (sumDict[sumDict[i]] === i && sumDict[i] !== i) {
        sum += i;
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " Sum of amicable numbers: ", sum);