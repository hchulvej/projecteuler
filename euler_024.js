const start = Date.now();

let factorials = [BigInt(1), BigInt(1)];
for (let i = 2; i < 10; i++) {
    factorials.push(BigInt(i) * factorials[i - 1]);
}
factorials.reverse();

let perm = "";
let rem = BigInt(1000000);
let digits = [...Array(10).keys()].map(x => BigInt(x));

for (const f of factorials) {
    let div = BigInt(0);
    while (rem > div * f) {
        div = div + BigInt(1);
    }
    div = div - BigInt(1);
    let digit = digits[Number(div)];    
    perm += digit;
    digits = digits.filter(x => x !== digit);
    rem -= div * f;
    console.log(rem);
}




const end = Date.now();

console.log("Execute time: ", end - start, " The millionth lexicographic permutation is: ", perm);