const start = Date.now();

let sum = BigInt(0);

const digitSum = (num) => {
    return num.toString().split("").reduce((p,c) => p + BigInt(c), BigInt(0));
}

for (let a = 1; a < 100; a++) {
    for (let b = 1; b < 100; b++) {
        let ds = digitSum(BigInt(a)**BigInt(b));
        if (ds > sum) {
            sum = ds;
        }
    }
}


const end = Date.now();

console.log("Execute time: ", end - start, " Maximal digit sum is: ", Number(sum));