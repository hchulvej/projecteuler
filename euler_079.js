const start = Date.now();

import { readFileSync } from 'fs';

function syncReadFile(filename) {
    const contents = readFileSync(filename, 'utf-8');

    const arr = contents.split("\n");

    return arr;
}

const successes = syncReadFile('./euler_079.txt').slice(0,50);

const isSucces = (passcode, success) => {
    if (!passcode.includes(success[0])) {
        return false;
    }

    const index1 = passcode.indexOf(success[0]);

    if (!passcode.slice(index1).includes(success[1])) {
        return false;
    }

    const index2 = passcode.slice(index1).indexOf(success[1]);

    if (!passcode.slice(index1).slice(index2).includes(success[2])) {
        return false;
    }

    return true;
}

const isValidPasscode = (passcode) => {
    return successes.every(x => isSucces(passcode, x));
}

let pc = "";
let n = 1000;
while (pc.length === 0) {
    if (isValidPasscode(n.toString())) {
        pc = n.toString();
    }
    n++;
}

const end = Date.now();

console.log("Execute time: ", end - start, " Shortest possible passcode is: ", pc);