const start = Date.now();

const b = BigInt(28433);
const a = BigInt(7830457);

let power = BigInt(1);
let temp = b;

while (power <= a) {
    temp = (temp * BigInt(2)) % BigInt(10000000000);
    power = power + BigInt(1);
}

temp = temp + BigInt(1);

const end = Date.now();

console.log("Execute time: ", end - start, " The last ten digits are: ", temp.toString());