const start = Date.now();

let num = BigInt(0);
for (let i = 1; i < 1001; i++) {
    num += BigInt(i)**BigInt(i);
}

const last10Digits = (b) => {
    let digs = b.toString();
    return digs.slice(digs.length - 10, digs.length);
}

let res = last10Digits(num);

const end = Date.now();

console.log("Execute time: ", end - start, " The last 10 digits are: ", res);