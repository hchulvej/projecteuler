const start = Date.now();

const isPalindromicString = (str) => {
    const len = str.length;
    for (let i = 0; i < Math.floor(len / 2); i++) {
        if (str.charAt(i) !== str.charAt(len - i - 1)) {
            return false;
        }
    }
    return true;
}

const digits = ["", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

let palindromicBase10 = new Set();

for (let a = 0; a < 11; a++) {
    for (let b = 0; b < 11; b++) {
        for (let c = 0; c < 11; c++) {
            palindromicBase10.add(digits[a] + digits[b] + digits[c] + digits[b] + digits[a]);
            palindromicBase10.add(digits[a] + digits[b]  + digits[c] + digits[c] + digits[b] + digits[a]);
        }
    }
}

let doubleBasePalindromes = [...palindromicBase10.values()].filter(x => isPalindromicString(Number(x).toString(2)));

const res = doubleBasePalindromes.filter(x => x.length > 0).map(x => Number(x)).reduce((p,c) => p + c,0);


const end = Date.now();

console.log("Execute time: ", end - start, " Sum of digits: ", res);