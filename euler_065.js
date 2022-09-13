import { continuedFractionGeneratorSteps } from "./continuedFractions.mjs";
import Decimal from "./decimal.mjs";

Decimal.set({precision: 1000});

const start = Date.now();

const e = Decimal.exp(1);

const num = continuedFractionGeneratorSteps(e, 100)[1][99];
const sum = num.toString().split("").map(x => Number(x)).reduce((p,c) => p + c, 0);


const end = Date.now();

console.log("Execute time: ", end - start, " Sum of digits is: ", sum);