const start = Date.now();

let res = 1;

// Analysis
// The number, we are seeking is smaller than 16666...7 ( = 1/6 * 10^n)
// because otherwise 6 times the number will have one digit too many

const upperLimit = (n) => {
    // n is the number of digits
    return Math.ceil(1 / 6 * 10**n);
}

const sameDigits = (num1, num2) => {
    return num1.toString().split("").sort().join("") === num2.toString().split("").sort().join("");
}

const arePermutedMultiples = (num) => {
    for (let m = 2; m < 7; m++) {
        if (!sameDigits(num, m * num)) {
            return false;
        }
    }
    return true;
}

let found = false;
let nd = 1;
while (!found) {
    for (let num = 10**(nd - 1); num < upperLimit(nd); num++) {
        if (arePermutedMultiples(num)) {
            found = true;
            res = num;
            break;
        }
    }
    nd++;
}

const end = Date.now();

console.log("Execute time: ", end - start, " The product is: ", res);