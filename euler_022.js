const start = Date.now();

const { readFileSync, promises: fsPromises } = require('fs');

function syncReadFile(filename) {
    const contents = readFileSync(filename, 'utf-8');

    const arr = contents.split(",").map(s => s.replaceAll('"','')).sort();

    return arr;
}

const grid = syncReadFile('./euler_022.txt');

let letterValue = {};
let number = 1;

for (const l of "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("")) {
    letterValue[l] = number;
    number++;
}

let sum = 0;

for (let i = 0; i < grid.length; i++) {
    let val = grid[i].split("").reduce((p,c) => p + letterValue[c],0);
    sum += val * (i + 1);
}

const end = Date.now();

console.log("Execute time: ", end - start, " Total sum is: ", sum);