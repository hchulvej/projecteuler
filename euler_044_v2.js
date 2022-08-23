const start = Date.now();

let D = 0;

// Pentagonals
let pentagonals = Array(10**7);
pentagonals.fill(false);
let i = 1;
let n = 1;

while (i < 10**7) {
    pentagonals[i] = true;
    i += (3 * n + 1);
    n++;
}

let stillLooking = true;
let k = 1;

while (stillLooking) {
    for (let j = 1; j < k; j++) {
        if (pentagonals[Math.floor((k / 2) * (3 * k - 1) - (j / 2) * (3 * j - 1))]) {
            if (pentagonals[Math.floor((k / 2) * (3 * k - 1) + (j / 2) * (3 * j - 1))]) {
                stillLooking = false;
                D = Math.floor((k / 2) * (3 * k - 1) - (j / 2) * (3 * j - 1));
            }
        }
    }
    k++;
}




const end = Date.now();

console.log("Execute time: ", end - start, " The value of D is: ", D);