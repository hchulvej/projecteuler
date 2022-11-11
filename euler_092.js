const start = Date.now();

let squares = [];
for (let i = 0; i < 10; i++) {
    squares[i] = i * i;
}

const nextNumber = (cur) => {
    if (cur < 10) {
        return squares[cur];
    }
    return squares[cur % 10] + nextNumber(Math.floor(cur / 10));
}

let checked = new Array(10**7);
checked.fill(0);

for (let i = 2; i < 10**7; i++) {
    if (checked[i] === 0) {
        let chain = [i];
        let cur = nextNumber(i);
        while (cur !== 1 && cur !== 89) {
            chain.push(cur);
            cur = nextNumber(cur);
        }
        for (const c of chain) {
            checked[c] = cur;
        }
    }
}

const eightyNines = checked.filter(x => x === 89).length;

const end = Date.now();

console.log("Execute time: ", end - start, " The number of starting numbers is: ", eightyNines);