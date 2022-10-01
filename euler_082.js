const start = Date.now();

import { readFileSync } from 'fs';

function syncReadFile(filename) {
    const contents = readFileSync(filename, 'utf-8');

    const arr = contents.split("\n");

    return arr.map(row => row.split(",").map(cell => Number(cell)));
}

const matrix2D = syncReadFile('./euler_082.txt');

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

// The sub-sum matrix
let SSM = Array(6400);
// Last column is the same as the matrix
for (let i = 0; i < 80; i++) {
    SSM[index(i, 79)] = entry(i, 79);
}

for (let c = 78; c >= 0; c--) {
    for (let r = 0; r < 80; r++) {
        // Straight right
        let minVal = entry(r,c) + SSM[index(r, c + 1)];
        let exceededMin = false;
        let current = entry(r,c);
        // Look up
        for (let rl = r - 1; !exceededMin && rl >= 0; rl--) {
            current += entry(rl, c);
            exceededMin = current >= minVal;
            minVal = Math.min(minVal, current + SSM[index(rl, c + 1)]);
        }
        // Look down
        exceededMin = false;
        current = entry(r,c);
        for (let rl = r + 1; !exceededMin && rl < 80; rl++) {
            current += entry(rl, c);
            exceededMin = current >= minVal;
            minVal = Math.min(minVal, current + SSM[index(rl, c + 1)]);
        }
        SSM[index(r,c)] = minVal;
    }
}


let firstCol = [];
for (let i = 0; i < 80; i++) {
    firstCol.push(SSM[index(i, 0)]);
}

const minSum = Math.min(...firstCol);

const end = Date.now();

console.log("Execute time: ", end - start, " Minimal path sum is: ", minSum);