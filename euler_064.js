import { continuedFractionGenerator, simpleSqrtCF } from "./continuedFractions.mjs";
import Decimal from "./decimal.mjs";

Decimal.set({precision: 100});

const start = Date.now();

const period = (n) => {
    if (new Decimal(n).sqrt().isInt()) {
        return 0;
    }
    let a = [new Decimal(n).sqrt().floor()];
    let b = [new Decimal(0), a[0]];
    let c = [b[0], new Decimal(n).minus(a[0].toPower(2))];

    let i = 1;
    while (!(new Decimal(a[0].times(2)).equals(a[a.length - 1]))) {
        i++;
        a.push(((a[0].plus(b[i - 1])).dividedBy(c[i - 1])).floor());
        b.push((a[i - 1].times(c[i - 1])).minus(b[i - 1]));
        c.push((new Decimal(n).minus(b[i].toPower(2))).dividedBy(c[i - 1]));
    }
    return a.length - 1;
}

let oddPeriods = 0;
for (let k = 2; k < 10001; k++) {
    if (period(k) % 2 === 1) {
        oddPeriods++;
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " Number of odd-period continued fractions is: ", oddPeriods);