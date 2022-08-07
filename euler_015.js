const start = Date.now();

let factorial = [1,1];
for (let i = 2;i <= 40;i++) {
    factorial[i] = i * factorial[i-1];
}

const number = factorial[40] / (factorial[20] * factorial[20]);


const end = Date.now();

console.log("Execute time: ", end - start, " Number of routes ", number);