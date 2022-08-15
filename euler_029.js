const start = Date.now();

let terms = new Set();

for (let a = 2; a < 101; a++) {
    for (let b = 2; b < 101; b++) {
        terms.add(BigInt(a)**BigInt(b));
    }
}
    


const end = Date.now();

console.log("Execute time: ", end - start, " Sum of diagonal numbers is: ", terms.size);