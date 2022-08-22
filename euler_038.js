const start = Date.now();

const isPandigital = (str) => {
    return str.split("").sort().join("") === "123456789";
}

const concatProduct = (num,n) => {
    let prod = "";
    for (let i = 1; i < n + 1; i++) {
        prod += (i * num).toString();
    }

    return prod;
}

let largestPN = 918273645;

for (let n = 2; n < 10; n++) {
    let ul = 10**(Math.ceil(9 / n));
    
    for (let num = 1; num <= ul; num++) {
        let cp = concatProduct(num,n);
        if (cp.length > 9) {
            break;
        }
        if (cp.length === 9 && Number(cp) > largestPN && isPandigital(cp)) {
            largestPN = Number(cp);
        }
    }
}


const end = Date.now();

console.log("Execute time: ", end - start, " Largest pandigital number is: ", largestPN);