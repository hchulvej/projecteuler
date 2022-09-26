const start = Date.now();

import { readFileSync } from 'fs';

function syncReadFile(filename) {
    const contents = readFileSync(filename, 'utf-8');

    const arr = contents.split("\n");

    return arr.map(row => row.split(",").map(cell => Number(cell)));
}

const matrix = syncReadFile('./euler_081.txt');

let sumMatrix = Array(80);
sumMatrix.fill(Array(80));

for (let row = 79; row >= 0; row--) {
    for (let col = 79; col >= 0; col--) {
        if (row === 79 && col === 79) {
            sumMatrix[row][col] = matrix[row][col];
        }
        if (row === 79 && col < 79) {
            sumMatrix[row][col] = matrix[row][col] + sumMatrix[row][col + 1];
        }
        if (row < 79 && col === 79) {
            sumMatrix[row][col] = matrix[row][col] + sumMatrix[row + 1][col];
        }
        if (row < 79 && col < 79) {
            sumMatrix[row][col] = Math.min(matrix[row][col] + sumMatrix[row][col + 1], matrix[row][col] + sumMatrix[row + 1][col]);
        }
    }
}

const minSum = sumMatrix[0][0];

const end = Date.now();

console.log("Execute time: ", end - start, " Minimal path sum is: ", minSum);