const start = Date.now();

import { readFileSync } from 'fs';


function syncReadFile(filename) {
    const contents = readFileSync(filename, 'utf-8');

    const arr = contents.split("\n");

    let pairs = [];
    for (const element of arr) {
        pairs.push(element.split(",").map(x => Number(x)));
    }

    return pairs;
}

const baseExponentPairs = syncReadFile('./euler_099.txt');

const deepCopy = [...baseExponentPairs];

deepCopy.sort((pair1, pair2) => Math.log(pair2[0]) * pair2[1] - Math.log(pair1[0]) * pair1[1]);

const end = Date.now();

console.log("Execute time: ", end - start, " Line number is: ", baseExponentPairs.indexOf(deepCopy[0]) + 1);