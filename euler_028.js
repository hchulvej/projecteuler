const start = Date.now();

let sum = 1;

// Analysis
//
// for every n = 3, 5, 7, ..., 1001 an additional (4n - 4) numbers are added to the spiral
//
// the corner numbers' indices are n - 1, 2n - 2, 3n - 3 and 4n - 4 if the smallest number has index 1.
//
// the nth circle has the numbers from (n - 2)^2 + 1 (index 1) to n^2 (index 4n - 4)
//
// hence: first number (lower right corner) is (n - 2)^2 + 1 + (n - 2) = n^2 - 3n + 3
// second number (lower left corner): n^2 - 3n + 3 + (n - 1) = n^2 - 2n + 2
// third number (upper left corner): n^2 - 2n + 2 + (n - 1) = n^2 - n + 1
// fourth number (upper right corner): n^2 - n + 1 + (n - 1) = n^2
let n = 3;

while (n < 1002) {
    sum += n * n - 3 * n + 3;
    sum += n * n - 2 * n + 2;
    sum += n * n - n + 1;
    sum += n * n;
    n += 2;
}
    


const end = Date.now();

console.log("Execute time: ", end - start, " Sum of diagonal numbers is: ", sum);