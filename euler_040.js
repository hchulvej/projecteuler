const start = Date.now();

let product = 1;

// Construction of Champernowne's constant
let cc = "0";
let totalLength = 0;
let n = 1;

while (totalLength < 10**6 + 1) {
    cc += n.toString();
    totalLength += Math.floor(Math.log10(n)) + 1;
    n++;
}

for (let p = 0; p < 7; p++) {
    product *= Number(cc.charAt(10**p));
}

const end = Date.now();

console.log("Execute time: ", end - start, " The product is: ", product);