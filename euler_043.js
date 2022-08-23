const start = Date.now();

// Possible d2 d3 d4, d3 d4 d5 etc
//
let possibles = new Map();
possibles.set(0, []); //d2 d3 d4
possibles.set(1, []); //d3 d4 d5
possibles.set(2, []); // etc
possibles.set(3, []);
possibles.set(4, []);
possibles.set(5, []);
possibles.set(6, []);


const numberAsString = (num) => {
    if (num < 10) {
        return "00" + num.toString();
    }
    if (num < 100) {
        return "0" + num.toString();
    }
    return num.toString();
}

for (let n = 1; n < 1000; n++) {
    const primes = [2,3,5,7,11,13,17];
    for (let i = 0; i < 7; i++) {
        if (n % primes[i] === 0) {
            let arr = possibles.get(i);
            arr.push(numberAsString(n));
            possibles.set(i, arr);
        }
    }
}

// Candidate numbers (only last 9 digits)
const connect = (left, right) => {
    return left.slice(left.length - 2) === right.slice(0,2);
}

let candidates = possibles.get(6);

for (let i = 5; i > -1; i--) {
    let temp = [];
    for (const r of candidates) {
        for (const l of possibles.get(i)) {
            if (connect(l,r)) {
                temp.push(l[0] + r);
            }
        }
    }
    candidates = temp;
}

//Pandigitals
let pandigitals = [];

const isPandigital = (str) => {
    return str.split("").sort().join("") === "0123456789";
}

for (const c of candidates) {
    for (let f = 1; f < 10; f++) {
        if (isPandigital(f.toString() + c)) {
            pandigitals.push(f.toString() + c);
        }
    }
}

const sum = pandigitals.reduce((p,c) => p + Number(c),0);


const end = Date.now();

console.log("Execute time: ", end - start, " Total sum is: ", sum);