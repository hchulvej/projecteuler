const start = Date.now();

let sum = 0;

const fifthPowers = [...Array(10).keys()].map(x => x**5);

const specialSumOfDigits = (num) => {
    let digits = [num % 10];
    while (num > 10) {
        num = Number.parseInt((num - (num % 10)) / 10);
        digits.push(num % 10);
    }
    return digits.reduce((prev,curr) => prev + fifthPowers[curr],0);
}

// Analysis
//
// 7 * 9^5 = 413343 which is less than any 7-digit number
// so we only need to check numbers less than 6 * 9^5 = 354294

for (let n = 2; n < 354295; n++) {
    if (specialSumOfDigits(n) === n) {
        sum += n;
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " Sum of all the numbers is: ", sum);