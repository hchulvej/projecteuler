const start = Date.now();

let arr = Array(1001);
arr.fill(false);

let sum = 0;

let i = 1;
while (i * 3 < 1000) {
    if (!arr[3 * i]) {
        arr[3 * i] = true;
        sum += 3 * i;
    }
    i++;
}
let j = 1;
while (j * 5 < 1000) {
    if (!arr[5 * j]) {
        arr[5 * j] = true;
        sum += 5 * j;
    }
    j++;
}


const end = Date.now();

console.log("Execute time: ", end - start, " Sum is: ", sum);