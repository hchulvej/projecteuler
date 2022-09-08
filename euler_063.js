const start = Date.now();

let count = 1; // a = 1, 1^1 = 1

const numberOfDigits = (num) => {
    return Math.floor(Math.log10(num)) + 1;
}

// Analysis
//
// if a^n is an n-digit number, then 10^(n-1) <= a^n < 10^n
//
// taking log10: n-1 <= n*log(a) < n
//
// so a = 1, 2, 3, 4, 5, 6, 7, 8, 9 are the only options

for (const a of [2,3,4,5,6,7,8,9]) {
    let n = 1;
    while (numberOfDigits(a**n) < n + 1) {
        if (numberOfDigits(a**n) === n) {
            count++;
        }
        n++;
    }
}


const end = Date.now();

console.log("Execute time: ", end - start, " Number of integers is: ", count);