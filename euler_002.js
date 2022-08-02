const start = Date.now();

let fib = [1,2,3];

let sum = 2;

while (fib[2] <= 4000000) {
    fib = [fib[1], fib[2], fib[1] + fib[2]];
    if (fib[2] % 2 === 0) {
        sum += fib[2];
    }
}


const end = Date.now();

console.log("Execute time: ", end - start, " Sum is: ", sum);