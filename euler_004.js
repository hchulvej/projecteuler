const start = Date.now();

const isPalindrome = (num) => {
    const asString = num.toString();
    for (let i = 0;i <= Math.floor(asString.length / 2);i++) {
        if (asString[i] !== asString[asString.length - 1 - i]) {
            return false;
        }
    }
    return true;
}

let largestPalindrome = 1;
const threeDigitNumbers = [...Array(1000).keys()].slice(100);

for (const num1 of threeDigitNumbers) {
    for (const num2 of threeDigitNumbers) {
        if (num1 >= num2 && isPalindrome(num1 * num2) && largestPalindrome < num1 * num2) {
            largestPalindrome = num1 * num2;
        }
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " Largest palindrome is: ", largestPalindrome);