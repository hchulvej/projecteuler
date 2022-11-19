const start = Date.now();

// Proper Divisors

let sumOfProperDivisors = new Array(1000001);
sumOfProperDivisors.fill(0);
sumOfProperDivisors[1] = 1;
for (let div = 2; div < 1000001; div++) {
    let k = 2;
    while (k * div < 1000001) {
        sumOfProperDivisors[k * div] += div;
        k++;
    }
    sumOfProperDivisors[div] += 1;
}

// Tracking numbers we have already checked

let checked = new Array(10**6 + 2);
checked.fill(false);
checked[0] = checked[1] = checked[2] = true;

// Longest chain info

let smallest = 10**6 + 1;
let longest = 0;


// Building the chains

const chain = (num) => {
    let res = [num];
    let current = sumOfProperDivisors[res];

    while (current < 10**6 + 1 && !res.includes(current)) {
        res.push(current);
        current = sumOfProperDivisors[current];
    }

    for (const el of res) {
        if (el < 10**6 + 1) {
            checked[el] = true;
        }
    }

    if (res[res.length - 1] > 10**6) {
        return [];
    }

    let i = res.indexOf(current);
    res = res.slice(i);
    return res.slice(0,res.length);
}

for (let num = 3; num < 10**6 + 1; num++) {
    if (!checked[num]) {
        let c = chain(num).sort((a, b) => a - b);
        if (c.length > longest) {
            longest = c.length;
            smallest = c[0];
        }
    }
}


const end = Date.now();

console.log("Execute time: ", end - start, " The smallest member of the logest chain is: ", smallest);