const start = Date.now();

// See euler_094.pdf for an in-depth explanation of the method

// Solving Pell's equation x^2 - 3y^2 = 1
//
// Fundemental solution (x_0, y_0) = (2, 1)
//
// Recursion algorithm:
//
// x_(k+1) = x_0 * x_k + 3 * y_0 * y_k
//
// y_(k+1) = x_0 * y_k + y_0 * x_k

let xvals = [BigInt(2)];
let yvals = [BigInt(1)];

let limit = BigInt(10**9);
let k = 1;

while (BigInt(3) * xvals[k - 1] + BigInt(1) < BigInt(2) * limit) {
    xvals.push(xvals[0] * xvals[k - 1] + BigInt(3) * yvals[0] * yvals[k - 1]);
    yvals.push(xvals[0] * yvals[k - 1] + yvals[0] * xvals[k - 1]);
    k++;
}

// Checking if a solution leads to an almost equilateral triangle
//
// solution (d, c)
//
// Type 1: a, a, a + 1
//
// a = (2*d+1)/3: integer <=> (2d+1)%3 = 0
//
// perimeter = 3*a+1 < 10^9
//
// b = 2*c, check b^2 = 3a^2-2a-1
//
//
// Type 2: a, a, a - 1
//
// a = (2*d-1)/3: integer <=> (2d-1)%3 = 0
//
// perimeter = 3*a-1 < 10^9
//
// b = 2*c, check b^2 = 3a^2+2a-1

const check = (d, c, type) => {
    if (type === 1) {
        if ((BigInt(2) * d + BigInt(1)) % BigInt(3) !== BigInt(0)) {
            return BigInt(0);
        }
        const a = (BigInt(2) * d + BigInt(1)) / BigInt(3);
        const b = BigInt(2) * c;
        const perim = BigInt(3) * a + BigInt(1);

        if (perim < limit && b**BigInt(2) === BigInt(3) * (a**BigInt(2)) - BigInt(2) * a - BigInt(1)) {
            return perim;
        }
        return BigInt(0);
    }
    if (type === 2) {
        if ((BigInt(2) * d - BigInt(1)) % BigInt(3) !== BigInt(0)) {
            return BigInt(0);
        }
        const a = (BigInt(2) * d - BigInt(1)) / BigInt(3);
        const b = BigInt(2) * c;
        const perim = BigInt(3) * a - BigInt(1);

        if (perim < limit && b**BigInt(2) === BigInt(3) * (a**BigInt(2)) + BigInt(2) * a - BigInt(1)) {
            return perim;
        }
        return BigInt(0);
    }
}

let sumOfPerimeters = BigInt(0);

// 1-1-2 triangle not allowed
for (let i = 1; i < xvals.length; i++) {
    try {
        sumOfPerimeters += (check(xvals[i], yvals[i], 1) + check(xvals[i], yvals[i], 2));
    }
    catch {
        console.log(xvals[i], yvals[i], check(xvals[i], yvals[i], 1), check(xvals[i], yvals[i], 2));
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " The sum of the perimeters is: ", Number(BigInt(sumOfPerimeters)));