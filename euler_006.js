const start = Date.now();

const sumOfSquaresUpTo = (n) => {return (n * (n + 1) * (2 * n + 1)) / 6;}
const squareOfSumUpTo = (n) => {return Math.pow((n * (n + 1)) / 2 , 2);}

const end = Date.now();

console.log("Execute time: ", end - start, " Difference is: ", squareOfSumUpTo(100) - sumOfSquaresUpTo(100));