const start = Date.now();

const base = BigInt("2");
const exponent = BigInt("1000");
const power = base ** exponent;

const digits = power.toString().split("").map(x => Number.parseInt(x));

const res = digits.reduce((sum, num) => sum + num,0);


const end = Date.now();

console.log("Execute time: ", end - start, " Sum of digits: ", res);