const start = Date.now();

let factorial = [1,1];
for (let n = 2; n < 10; n++) {
    factorial[n] = n * factorial[n - 1];
}

const factorialSum = (num) => {
    return num.toString().split("").map(x => Number(x)).map(x => factorial[x]).reduce((p,c) => p + c, 0);
}

let checked = Array(1000000);
checked.fill(false);
checked[0] = true;
checked[1] = true;

let longChains = 0;


for (let n = 2; n < 1000000; n++) {
  if (!checked[n]) {
    let chain = [n];
    let fs = factorialSum(n);

    while (chain.indexOf(fs) === -1) {
      chain.push(fs);
      fs = factorialSum(fs);
    }

    if (chain.length < 60) {
        new Set(chain).forEach((x) => {
            checked[x] = true;
        });
    }

    if (chain.length === 60) {
        longChains++;
        new Set(chain).forEach((x) => {
            checked[x] = true;
        });
    }
  }
}


const end = Date.now();

console.log("Execute time: ", end - start, " The numerator is: ", longChains);