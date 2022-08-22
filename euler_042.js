const start = Date.now();

const { readFileSync, promises: fsPromises } = require('fs');

function syncReadFile(filename) {
    const contents = readFileSync(filename, 'utf-8');

    const arr = contents.split(",").map(s => s.replaceAll('"','')).sort();

    return arr;
}

const grid = syncReadFile('./euler_042.txt');

let letterValue = {};
let number = 1;

for (const l of "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("")) {
    letterValue[l] = number;
    number++;
}

let triangleNumbers = new Set();
triangleNumbers.add(1);
let index = 2;
while (index < 100) {
    triangleNumbers.add(Math.floor((index * (index + 1)) / 2));
    index++;
}

let wordValue = (w) => {
    return w.split("").reduce((p,c) => p + letterValue[c],0);
}

let triangleWords = 0;

for (const word of grid) {
    if (triangleNumbers.has(wordValue(word))) {
        triangleWords++;
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " Number of triangle words is: ", triangleWords);