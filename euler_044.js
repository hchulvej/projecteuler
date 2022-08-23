const start = Date.now();

let D = 0;

// The quest to find any pentagon differences
let pentagonals = [1];
let n = 2;
let p = 5;

while (p < 10**7) {
    pentagonals.push(p);
    p += (3 * n + 1);
    n++;
}

let diffPairs = [];

for (let i = 0; i < pentagonals.length; i++) {
    for (let j = i; j < pentagonals.length; j++) {
        let diff = pentagonals[j] - pentagonals[i];
        if (pentagonals.indexOf(diff) > -1) {
            diffPairs.push([pentagonals[j],pentagonals[i]]);
        }
    }    
}

let sumAndDiffPairs = [];

for (const pair of diffPairs) {
    let sum = pair[0] + pair[1];
        if (pentagonals.indexOf(sum) > -1) {
            sumAndDiffPairs.push(pair);
        }
}

console.log(sumAndDiffPairs[0][0] - sumAndDiffPairs[0][1]);


const end = Date.now();

console.log("Execute time: ", end - start, " The value of D is: ", D);