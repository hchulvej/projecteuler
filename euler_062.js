const start = Date.now();

const specialToString = (num) => {
    return num.toString().split("").sort().join("");
}

let countPermutations = new Map();
let found = false;
let n = 0;
let base;

while (!found) {
    n++;
    let sts = specialToString(n**3);
    if (!countPermutations.has(sts)) {
        countPermutations.set(sts, []);
    }
    let cp = countPermutations.get(sts);
    cp.push(n);
    countPermutations.set(sts, cp);
    if (cp.length === 5) {
        found = true;
        base = cp[0];
    }
}




const end = Date.now();

console.log("Execute time: ", end - start, " Smallest cube is: ", base**3);