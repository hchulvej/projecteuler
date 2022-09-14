import { continuedFractionGeneratorSteps } from "./continuedFractions.mjs";
import Decimal from "./decimal.mjs";

Decimal.set({precision: 1000});

const start = Date.now();

const minimalX = (D) => {
    const n = new Decimal(D).sqrt();
    const cf = continuedFractionGeneratorSteps(n, 100);
    const x = cf[1];
    const y = cf[2];
    
    for (let i = 0; i < x.length; i++) {
        if (x[i] * x[i] - BigInt(D) * y[i] * y[i] === BigInt(1)) {
            return x[i];
        }
    }
    return BigInt(-1);
}

const isSquare = (c) => {
    return new Decimal(c).sqrt().isInteger();
}

let maxx = BigInt(-1);
let optimalD = 0;

let D = 2;
while (D < 1001) {
  if (!isSquare(D)) {
    const minxD = minimalX(D);
    if (minxD === BigInt(-1)) {
      console.log("Problem ", D);
    }
    if (minxD > maxx) {
      optimalD = D;
      maxx = minxD;
    }
  }

  D++;
}


const end = Date.now();

console.log("Execute time: ", end - start, " The value of D is: ", optimalD);