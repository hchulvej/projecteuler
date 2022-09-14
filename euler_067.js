import { readFileSync } from 'fs';

const start = Date.now();

function syncReadFile(filename) {
    const contents = readFileSync(filename, 'utf-8');

    const arr = contents.split(/\r?\n/);

    for (let i = 0; i < arr.length; i++) {
        arr[i] = arr[i].split(" ").map(x => parseInt(x));
    }

    return arr;
}

const grid = syncReadFile('./euler_067.txt');
grid.reverse();

console.log(grid.length);

const reduceRows = (longRow, shortRow) => {
    let newRow = [];
    for (let i = 0; i < shortRow.length; i++) {
        newRow.push(Math.max(shortRow[i] + longRow[i], shortRow[i] + longRow[i + 1]));
    }
    return newRow;
}

for (let r = 0; r < grid.length - 1; r++) {
    grid[r + 1] = reduceRows(grid[r], grid[r + 1]);
}

let maxSum = grid[grid.length - 1][0];

const end = Date.now();

console.log("Execute time: ", end - start, " Maximal sum is: ", maxSum);