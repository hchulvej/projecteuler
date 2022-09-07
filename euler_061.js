const start = Date.now();

// Creation of all the different numbers
//
const upperBound = 10000;
let numbers = new Map();

const triangular = (n) => {
    return n * (n + 1) / 2;
}

const square = (n) => {
    return n * n;
}

const pentagonal = (n) => {
    return n * (3 * n - 1) / 2;
}

const hexagonal = (n) => {
    return n * (2 * n - 1);
}

const heptagonal = (n) => {
    return n * (5 * n - 3) / 2;
}

const octagonal = (n) => {
    return n * (3 * n - 2);
}

for (const g of [3, 4, 5, 6, 7, 8]) {
    let n = 1;
    if (g === 3) {
        let set3 = [];
        while (triangular(n) < upperBound) {
            set3.push([triangular(n),3]);
            n++;
        }
        numbers.set(3, set3.filter(x => x[0] > 999));
    }
    if (g === 4) {
        let set4 = [];
        while (square(n) < upperBound) {
            set4.push([square(n),4]);
            n++;
        }
        numbers.set(4, set4.filter(x => x[0] > 999));
    }
    if (g === 5) {
        let set5 = [];
        while (pentagonal(n) < upperBound) {
            set5.push([pentagonal(n),5]);
            n++;
        }
        numbers.set(5, set5.filter(x => x[0] > 999));
    }
    if (g === 6) {
        let set6 = [];
        while (hexagonal(n) < upperBound) {
            set6.push([hexagonal(n),6]);
            n++;
        }
        numbers.set(6, set6.filter(x => x[0] > 999));
    }
    if (g === 7) {
        let set7 = [];
        while (heptagonal(n) < upperBound) {
            set7.push([heptagonal(n),7]);
            n++;
        }
        numbers.set(7, set7.filter(x => x[0] > 999));
    }
    if (g === 8) {
        let set8 = [];
        while (octagonal(n) < upperBound) {
            set8.push([octagonal(n),8]);
            n++;
        }
        numbers.set(8, set8.filter(x => x[0] > 999));
    }
}
//

// Creation of all the cyclic numbers
const areCyclic = (num1, num2) => {
    return num1 % 100 === (num2 - (num2 % 100)) / 100;
}

let allNumbers = [];
for (const g of [3,4,5,6,7,8]) {
    allNumbers = allNumbers.concat(numbers.get(g));
}

for (const a of allNumbers) {
    for (const b of allNumbers.filter(x => areCyclic(a[0],x[0]))) {
        for (const c of allNumbers.filter(x => areCyclic(b[0],x[0]))) {
            for (const d of allNumbers.filter(x => areCyclic(c[0],x[0]))) {
                for (const e of allNumbers.filter(x => areCyclic(d[0],x[0]))) {
                    for (const f of allNumbers.filter(x => areCyclic(e[0],x[0]))) {
                        if ([a[1], b[1], c[1], d[1], e[1], f[1]].sort().join("") === "345678" && areCyclic(f[0], a[0])) {

                            console.log([a[0],b[0],c[0],d[0],e[0],f[0]].reduce((p,c) => p + c,0));
                        }
                        
                    }
                }
            }
        }
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " Sum is: ", 1);