const start = Date.now();

import { readFileSync } from 'fs';

function syncReadFile(filename) {
    const contents = readFileSync(filename, 'utf-8');

    const arr = contents.split("\n");

    return arr.map(row => row.split(",").map(cell => Number(cell)));
}

const matrix2D = syncReadFile('./euler_083.txt');

// From row x col (0..79 x 0..79) to index in array (0..6399)
const index = (row, col) => {
    return row * 80 + col;
}

// Converting 2-dim matrix to 1-dim array
let matrix = Array(6400);
for (let row = 0; row < 80; row++) {
    for (let col = 0; col < 80; col++) {
        matrix[index(row, col)] = matrix2D[row][col];
    }
}
const entry = (row, col) => {
    return matrix[index(row, col)];
}

// Bellmann-Ford Algorithm
// Distance matrix
let distance = Array(6400);
distance.fill(Number.POSITIVE_INFINITY);

// Handling overflow
const dist = (row, col) => {
    if (row < 0 || col < 0 || row > 79 || col > 79) {
        return Number.POSITIVE_INFINITY;
    } else {
        return distance[index(row, col)];
    }
}

// Initialize
distance[index(0,0)] = entry(0,0);

// Max number of iterations i 6400 - 1 (number of nodes minus 1)
for (let it = 0; it < 6399; it++) {
    for (let row = 0; row < 80; row++) {
        for (let col = 0; col < 80; col++) {
            let minDistFromNode = Math.min(dist(row - 1, col), dist(row + 1, col), dist(row, col - 1), dist(row, col + 1));
            distance[index(row, col)] = Math.min(entry(row, col) + minDistFromNode, distance[index(row, col)]);
        }
    }
}

const minSum = dist(79,79);


const end = Date.now();

console.log("Execute time: ", end - start, " Minimal path sum is: ", minSum)