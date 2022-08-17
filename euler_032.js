const start = Date.now();

const pandigitalProduct = (x,y) => {
    const s = x.toString()
        .concat(y.toString())
        .concat((x * y).toString());
    return s.split("").sort().join("") === "123456789";
}

let pandigitalProducts = new Set();

// 1d * 4d = 4d
for (let d = 2; d < 10; d++) {
    let e = 1000;
    while (d * e < 10000) {
        if (pandigitalProduct(d,e)) {
            pandigitalProducts.add(d * e);
        }
        e++;
    }
}

// 2d * 3d = 4d
for (let d = 10; d < 100; d++) {
    let e = 100;
    while (d * e < 10000) {
        if (pandigitalProduct(d,e)) {
            pandigitalProducts.add(d * e);
        }
        e++;
    }
}

const sum = [...pandigitalProducts.values()].reduce((p,c) => p + c,0);

const end = Date.now();

console.log("Execute time: ", end - start, " Sum of pandigital products is: ", sum);