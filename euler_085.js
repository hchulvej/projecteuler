const start = Date.now();

// The number of rectangles in an m x n grid is
// m * (m + 1) * n * (n + 1) / 4

const rect = (m,n) => {
    return m * (m + 1) * n * (n + 1) / 4;
}

let optimalArea = 1;
let optimalRows = 1;
let optimalCols = 1;
for (let rows = 1; rows < 2000; rows++) {
    for (let cols = rows; cols < 2000; cols++) {
        if (Math.abs(2000000 - rect(optimalRows,optimalCols)) > Math.abs(2000000 - rect(rows, cols))) {
            optimalRows = rows;
            optimalCols = cols;
            optimalArea = rows * cols;
        }
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " The area is: ", optimalArea);