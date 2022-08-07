const start = Date.now();

const { readFileSync, promises: fsPromises } = require('fs');

function syncReadFile(filename) {
    const contents = readFileSync(filename, 'utf-8');

    const arr = contents.split(/\r?\n/);

    for (let i = 0; i < arr.length; i++) {
        arr[i] = arr[i].split(" ").map(x => parseInt(x));
    }

    return arr;
}

const grid = syncReadFile('./euler_011.txt');

function subGrid(row, col) {
    let res = [];
    for (let i = 0; i < 4; i++) {
        let newRow = [];
        for (let j = 0; j < 4; j++) {
            newRow.push(grid[row + i][col + j]);
        }
        res.push(newRow);

    }
    return res;
}

function prodArr4(arr) {
    return arr.reduce((p, c) => p * c, 1);
}

function maxProd(sg) {
    let maxP = 0;
    // horizontal products
    for (let i = 0; i < 4; i++) {
        let p = prodArr4(sg[i]);
        if (p > maxP) {
            maxP = p;
        }
    } 
    // vertical products
    for (let j = 0; j < 4; j++) {
        let p = prodArr4([sg[0][j], sg[1][j], sg[2][j], sg[3][j]]);
        if (p > maxP) {
            maxP = p;
        }
    }
    // diagonal products
    if (sg[0][0] * sg[1][1] * sg[2][2] * sg[3][3] > maxP) {
        maxP = sg[0][0] * sg[1][1] * sg[2][2] * sg[3][3];
    }
    if (sg[3][0] * sg[2][1] * sg[1][2] * sg[0][3] > maxP) {
        maxP = sg[3][0] * sg[2][1] * sg[1][2] * sg[0][3];
    }
    return maxP;
}

let maxProduct = 0;

for (let i = 0; i < 15; i++) {
    for (let j = 0; j < 15; j++) {
        let p = maxProd(subGrid(i,j));
        if (p > maxProduct) {
            maxProduct = p;
        }
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " Maximal product is: ", maxProduct);

