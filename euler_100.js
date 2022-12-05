const start = Date.now();

/*
    Analysis:

    P(BB) = (B/N) * ((B-1)/(N-1)) = 1/2

    N^2 - 2B^2 - N + 2B = 0

    This is a Binary Quadratic Diophantine Equation with

    A = 1, B = 0, C = -2, D = -1, E = 2, F = 0

    Algorithm found here:

    https://www.alpertron.com.ar/QUAD.HTM

    x_(n+1) = 3⁢ * x_n + 4 * ⁢y_n - 3
    y_(n+1) = 2 * ⁢x_n + 3 * ⁢y_n - 2

    We havee been given a solution: x_0 = 21 and y_0 = 15.
*/

let [N, B] = [BigInt(21), BigInt(15)];

while (N < BigInt(10) ** BigInt(12)) {
    [N, B] = [BigInt(3) * N + BigInt(4) * B - BigInt(3), BigInt(2) * N + BigInt(3) * B - BigInt(2)];
}


const end = Date.now();

console.log("Execute time: ", end - start, " Number of blue discs is: ", Number(B));