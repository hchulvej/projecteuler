// Initialization and algorithm
// x0 = the number in question
// an = floor(xn), x_(n+1) = 1 / (xn - an)
// P0 = a0, P1 = a0 * a1 + 1, Pn = P_(n-1) * an + P_(n-2)
// Q0 = 1, Q1 = a1, Qn = Q_(n-1) * an + Q_(n-2)

export function* continuedFractionGenerator(n) {
    let x = [n];
    let a = [Math.floor(n)];
    let P = [a[0]];
    let Q = [1];

    yield [x[0], a[0], P[0], Q[0]];

    x[1] = 1 / (x[0] - a[0]);
    a[1] = Math.floor(x[1]);
    P[1] = a[0] * a[1] + 1;
    Q[1] = a[1];

    yield [x[1], a[1], P[1], Q[1]];

    let m = 2;
    while(true) {
        x[m] = 1 / (x[m - 1] - a[m - 1]);
        a[m] = Math.floor(x[m]);
        P[m] = P[m - 1] * a[m] + P[m - 2];
        Q[m] = Q[m - 1] * a[m] + Q[m - 2];
        yield [x[m], a[m], P[m], Q[m]];
        m++;
    }
}