const start = Date.now();

function noOfFactors(n) {
    if (n === 1) {return 1;}

    let factors = [1, n];
    let max = n;

    for (let i = 2; i < max; i++) {
        if (n % i === 0) {
            factors.push(i);

            let r = n / i;
            if (r !== i) {
                factors.push(r);
            }
            max = r;
        }
    }

    return factors.length;
}


let triangleNumber = 28;
let n = 7;

while (noOfFactors(triangleNumber) < 501) {
    n++;
    triangleNumber += n;
}

const end = Date.now();

console.log("Execute time: ", end - start, " First triangle number is: ", triangleNumber);