const start = Date.now();

const smallSquares = new Set([...Array(1000).keys()].map(x => x**2));

const isPythagorean = (a,b) => {
    return smallSquares.has(a * a + b * b);
}

let perims = new Map();
perims.set(12, 1);
let maxSols = 1;
let maxPerim = 12;

for (let a = 3; a < 334; a++) {
    for (let b = a; b < 500; b++) {
        if (isPythagorean(a,b)) {
            let perim = Number.parseInt(a + b + Math.sqrt(a * a + b * b));
            if (perims.has(perim)) {
                perims.set(perim, perims.get(perim) + 1);
            } else {
                perims.set(perim, 1);
            }
            if (perims.get(perim) > maxSols) {
                maxPerim = perim;
                maxSols = perims.get(perim);
            }
            
        }
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " Number of solutions is maximized for p = ", maxPerim);