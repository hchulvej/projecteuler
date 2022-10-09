const start = Date.now();

// Box dimensions: a x b x c, a >= b >= c
const shortestPath = (a,b,c) => {
    const p1 = Math.sqrt((a + c)**2 + b**2);
    const p2 = Math.sqrt((b + c)**2 + a**2);
    const m = Math.min(p1, p2);
    if (Number.isInteger(m)) {
        return m;
    }
    return 0;
}

const numberOfIntegerPaths = (M) => {
    let count = 0;
    for (let a = 1; a < M + 1; a++) {
        for (let b = 1; b < a + 1; b++) {
            for (let c = 1; c < b + 1; c++) {
                if (shortestPath(a,b,c) > 0) {
                    count++;
                }
            }
        }
    }
    return count;
}

// Closest 100 is 18
// Closest 10 is 1
let ones = 1;
while (numberOfIntegerPaths(18 * 100 + 1 * 10 + ones) < 1000000) {
    ones++;
}
ones--; // ones = 7

const end = Date.now();

console.log("Execute time: ", end - start, " The least value of M is: ", 1817);