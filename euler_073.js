const start = Date.now();

const isLarger = (f1, f2) => {
    return f1[0] * f2[1] > f1[1] * f2[0];
}

const gcd = (a, b) => {
  if (b > a) {
    return gcd(b, a);
  }
  while (true) {
    a %= b;
    if (a === 0) {
      return b;
    }
    b %= a;
    if (b === 0) {
      return a;
    }
  }
};

const lower = [1,3];
const upper = [1,2];

let fractions = new Set();

for (let d = 2; d < 12001; d++) {
    let nums = [...Array(d).keys()].slice(1).filter(x => gcd(d, x) === 1);
    for (const n of nums) {
        if (isLarger([n, d], lower)  && isLarger(upper, [n,d])) {
            fractions.add([n, d]);
        }
    }
}

const res = fractions.size;


const end = Date.now();

console.log("Execute time: ", end - start, " The number of fractions is: ", res);