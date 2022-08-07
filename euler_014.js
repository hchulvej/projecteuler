const start = Date.now();

let collatz = {2 : 2};
let number = 2;
let longest = 2;

const nextCollatz = (n) => {return (n % 2 === 0) ? (n / 2) : (3 * n + 1); }


for (let i = 2; i < 1000000; i++) {
    let steps = 0;
    let next = i;
    while (!collatz[next]) {
        next = nextCollatz(next);
        steps++;
    }
    collatz[i] = steps + collatz[next];

    if (collatz[i] > longest) {
        [number, longest] = [i, collatz[i]];
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " Longest chain is produced by: ", number);