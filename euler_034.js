const start = Date.now();

let sum = 0;

// Analysis
// 0! = 1! = 1, 2! = 2, 3! = 6, 4! = 24, 5! = 120, 6! = 720, 7! = 5040
// 8! = 40320, 9! = 362880
//
// There are no 1-digit curious numbers
// 2-digit curious numbers only have digits 0-4
// 3-digit curious numbers only have digits 0-6
// 4-digit curious numbers only have digits 0-7
// 5-digit curious numbers only have digits 0-8
// 6-digit curious numbers only have digits 0-8
//
// n * 9! < 10^(n-1) for n > 7
// Hence there are no curious numbers with 8 or more digits


let factorials = {0 : 1, 1 : 1};
for (let i = 2; i < 10; i++) {
    factorials[i] = i * factorials[i - 1];
}

const factorialSum = (num) => {
    return num.toString().split("").map(x => Number.parseInt(x)).reduce((p,c) => p + factorials[c],0);
}

for (let n = 10; n < 9 * factorials[9]; n++) {
    if (factorialSum(n) === n) {
        sum += n;
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " Sum of curious numbers is: ", sum);