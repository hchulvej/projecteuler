const start = Date.now();

let biggest = 0;
let d = 2

function unitFractionDecimals(d) {
    let table = {}
    // Initialization
    table["length"] = 0;
    table["dividend"] = 1;
    table["quotient"] = 0;
    table["remainders"] = new Set();
    table["recurring"] = false;
    table["string"] = "";

    while (table["dividend"] < d) {
        table["dividend"] *= 10;
    }

    while (!table["recurring"]) {
        table["quotient"] = Math.floor( table["dividend"] / d );
        let rem = table["dividend"] % d;
        if (rem === 0) {
            return 0;
        }
        if (table["remainders"].has(rem)) {
            table["recurring"] = true;
        }
        table["remainders"].add(rem);
        table["length"]++;
        table["dividend"] = 10 * rem;
        table["string"] += table["quotient"].toString();
    }

    return table["string"].length - 1;
}
    
for (let i = 3; i < 1000; i++) {
    let len = unitFractionDecimals(i);
    if ( len > biggest) {
        d = i;
        biggest = len;
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " Value with longest recurring cycle is: ", d);