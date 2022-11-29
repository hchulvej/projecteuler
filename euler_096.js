const start = Date.now();

import { readFileSync } from 'fs';

function syncReadFile(filename) {
    const contents = readFileSync(filename, 'utf-8');

    const arr = contents.split("\n");

    let grids = [];
    for (let g = 0; g < 50; g++) {
        let gridStr = "";
        for (let l = 1; l < 10; l++) {
            gridStr += arr[10 * g + l];
        }
        grids.push(gridStr.split("").map(x => Number(x)));
    }

    return grids;
}

/*  
    We want the grids to be global variables.

    A grid i an array with indices 0-80.
    A value of 0 means a blank cell.
    A grid has rows 1-9 and columns 1-9 and 9 boxes
    arranged as

    1 2 3
    4 5 6
    7 8 9
*/
let grids = syncReadFile('./euler_096.txt');

/*
    From index to (row, col) and back
*/
const i2rc = (i) => {
    return [Math.floor(i / 9) + 1, (i % 9) + 1];
}

const rc2i = (r, c) => {
    return 9 * (r - 1) + (c - 1);
}

/*
    Checking the validity of rows, columns and boxes
*/
const isValid = (arr) => {
    // Must contain the numbers 1-9
    return arr.sort((a, b) => a - b).join("") === "123456789";
}

const getRow = (grid, rowNo) => {
    const row = [...Array(81).keys()].filter(x => i2rc(x)[0] === rowNo).map(x => grid[x]);
    return row;
}

const getCol = (grid, colNo) => {
    const col = [...Array(81).keys()].filter(x => i2rc(x)[1] === colNo).map(x => grid[x]);
    return col;
}

const getBox = (grid, boxNo) => {
    let rowOffset = 0;
    let colOffset = 0;
    switch (boxNo) {
        case 1:
            break;
        case 2:
            colOffset = 3;
            break;
        case 3:
            colOffset = 6;
            break;
        case 4:
            rowOffset = 3;
            break;
        case 5:
            rowOffset = 3;
            colOffset = 3;
            break;
        case 6:
            rowOffset = 3;
            colOffset = 6;
            break;
        case 7:
            rowOffset = 6;
            break;
        case 8:
            rowOffset = 6;
            colOffset = 3;
            break;
        case 9:
            rowOffset = 6;
            colOffset = 6;
            break;
    }
    let box = [];
    for (let r = 1; r < 4; r++) {
        for (let c = 1; c < 4; c++) {
            box.push(grid[rc2i(r + rowOffset, c + colOffset)]);
        }
    }
    return box;
}

/*
    Finding blank cells and possible values of cells
*/
const blankCells = (grid) => {
    return [...Array(81).keys()].filter(x => grid[x] === 0);
}

const isPossible = (grid, i, val) => {
    const rowNo = i2rc(i)[0];
    const colNo = i2rc(i)[1];
    const boxNo = 3 * Math.floor((rowNo - 1) / 3) + Math.floor((colNo - 1) / 3) + 1;
    if (getRow(grid, rowNo).includes(val) || getCol(grid, colNo).includes(val) || getBox(grid, boxNo).includes(val)) {
        return false;
    }
    return true;
}


const possibleVals = (grid, i) => {
    return [1, 2, 3, 4, 5, 6, 7, 8, 9].filter(x => isPossible(grid, i, x));
}


/*
    Solving the sudoku with backtracking
*/
const solve = (gridNo, index) => {
    while (index < 81 && grids[gridNo][index]) {
        index++;
    }

    if (index === 81) {return true;}

    const pvs = possibleVals(grids[gridNo], index);

    for (const pv of pvs) {
        grids[gridNo][index] = pv;
        if (solve(gridNo, index + 1)) {
            return true;
        }
    }

    grids[gridNo][index] = 0;

    return false;
}

/*
    Collecting and adding
*/
let sum = 0;

for (let i = 0; i < 50; i++) {
    solve(i, 0);
    sum += Number([grids[i][0], grids[i][1], grids[i][2]].join(""));
}


const end = Date.now();

console.log("Execute time: ", end - start, " Sum of top left corners is: ", sum)