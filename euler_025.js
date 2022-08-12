const start = Date.now();

let n = 2;
let fib = [BigInt(1),BigInt(1)];

while (fib[1].toString().length < 1000) {
    fib = [fib[1], fib[0] + fib[1]];
    n++;
}




const end = Date.now();

console.log("Execute time: ", end - start, " First 1000-digit Fibonacci number's index is: ", n);