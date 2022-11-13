const start = Date.now();

// https://www.johndcook.com/blog/2013/10/03/parenthesize-expression-catalan/
// (1) (axb)x(cxd)
// (2) ax(bx(cxd))
// (3) ax((bxc)xd)
// (4) ((axb)xc)xd
// (5) (ax(bxc))xd
//
// x = 1: +
// x = 2: *
// x = 3: -
// x = 4: /

const binary = (a,b,x) => {
    switch (x) {
        case 1:
            return a + b;
        case 2:
            return a * b;
        case 3:
            return a - b;
        case 4:
            if (b !== 0) {
                return a / b;
            }
            return Number.POSITIVE_INFINITY;
    }
}

const result = (a, b, c, d, xArr, num) => {
    switch (num) {
        case 1:
            return (binary(binary(a, b, xArr[0]), binary(c, d, xArr[2]), xArr[1]));
        case 2:
            return (binary(a, binary(b, binary(c, d, xArr[2]), xArr[1]), xArr[0]));
        case 3:
            return (binary(a, binary(binary(b, c, xArr[1]), d, xArr[2]), xArr[0]));
        case 4:
            return (binary(binary(binary(a, b, xArr[0]), c, xArr[1]), d, xArr[2]));
        case 5:
            return (binary(binary(a, binary(b, c, xArr[1]), xArr[0]), d, xArr[2]));
    }
}

let xArrays = [];
for (let i = 1; i < 5; i++) {
    for (let j = 1; j < 5; j++) {
        for (let k = 1; k < 5; k++) {
            xArrays.push([i, j, k]);
        }
    }
}

const longestSet = (setOfNumbers) => {
    let cur = 1;
    while (setOfNumbers.has(cur)) {
        cur++;
    }
    return cur - 1;
}

const permutations = (arr) => {
    let res = [];
    for (const a of arr) {
        for (const b of arr) {
            for (const c of arr) {
                for (const d of arr) {
                    if (a !== b && a !== c && a !== d && b !== c && b !== d && c !== d) {
                        res.push([a, b, c, d]);
                    }
                }
            }
        }
    }
    return res;
}

let largestN = 0;
let combination = [];

for (let a = 0; a < 10; a++) {
    for (let b = 0; b < 10; b++) {
        for (let c = 0; c < 10; c++) {
            for (let d = 0; d < 10; d++) {
                let expressible = new Set();
                for (const p of permutations([a, b, c, d])) {
                    for (const xArr of xArrays) {
                        for (let j = 1; j < 6; j++) {
                            expressible.add(result(p[0], p[1], p[2], p[3], xArr, j));
                        }
                    }
                }
                const longest = longestSet(expressible);
                if (largestN < longest) {
                    largestN = longest;
                    combination = [a, b, c, d];
                }
            }
        }
    }
}



const end = Date.now();

console.log("Execute time: ", end - start, " The distinct four digits concatenated is: ", combination.join(""));