const start = Date.now();

const upperBound = 60000;
let result;

// https://en.wikipedia.org/wiki/Partition_function_(number_theory)
const pentagonals = (k) => {
    return [(-k)*(3*(-k)-1)/2, (k)*(3*(k)-1)/2];   
}

let storedValues = new Map();
storedValues.set(0, BigInt(1));

const P = (n) => {
    if (n < 0) {
        return BigInt(0);
    }
    return storedValues.get(n);
}

for (let n = 1; n < upperBound; n++) {
    if (!storedValues.has(n)) {
        storedValues.set(n, BigInt(0));
    }
    let k = 1;
    
    while (pentagonals(k)[1] <= n) {
        let pents = pentagonals(k);
        if (k % 2 === 0) {
            storedValues.set(n, storedValues.get(n) - P(n - pents[0]) - P(n - pents[1]));
        } else {
            storedValues.set(n, storedValues.get(n) + P(n - pents[0]) + P(n - pents[1]));
        }
        
        k++;
    }
    if (P(n) % BigInt(1000000) === BigInt(0)) {
        result = n;
        break;
    }
}




const end = Date.now();

console.log("Execute time: ", end - start, " The least value of n is: ", result);