const start = Date.now();

function* triangular() {
    let n = 2;
    let t = 3;
    while (true) {
        yield t;
        n++;
        t += n;
    }
}

const tgen = triangular();

const isInteger = (n) => {
    return Math.floor(n) === n;
}

const isPentagonal = (n) => {
    return isInteger((1 + Math.sqrt(1 + 24 * n)) / 6);
}

const isHexagonal = (n) => {
    return isInteger((1 + Math.sqrt(1 + 8 * n)) / 4);
}

let counter = 0;
let res;

while (counter < 2) {
    let t = tgen.next().value;
    if (isPentagonal(t) && isHexagonal(t)) {
        counter++;
        if (counter === 2) {
            res = t;
        }
    }
}


const end = Date.now();

console.log("Execute time: ", end - start, " The next triangle number is: ", res);