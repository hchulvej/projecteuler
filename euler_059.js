const start = Date.now();

const { readFileSync, promises: fsPromises } = require('fs');

function syncReadFile(filename) {
    const contents = readFileSync(filename, 'utf-8');

    const arr = contents.split(",").map(x => Number(x));

    return arr;
}

const cipherText = syncReadFile('./euler_059.txt');

// Converts a text (String) to ASCII (Array of numbers)
const toASCII = (t) => {
    let a = [];
    for (let i = 0; i < t.length; i++) {
        a.push(t.charCodeAt(i));
    }
    return a;
}

// Converts ASCII (Array of numbers) to text (String)
const fromASCII = (a) => {
    return a.reduce((p,c) => p + String.fromCharCode(c), "");
}

// Takes an ASCII array (Array of numbers) and a key (String)
// and XORS the array and the key and returns the result converted to a text (String)
const decipher = (asciiArr, key) => {
    let realKey = key;
    while (realKey.length < asciiArr.length) {
        realKey += key;
    }
    let a2 = toASCII(realKey);
    let xor = [];
    for (let i = 0; i < asciiArr.length; i++) {
        xor.push(asciiArr[i]^a2[i]);
    }
    return fromASCII(xor);
}

// An English text will probably have "the" in it.
for (const a of "abcdefghijklmnopqrstuvwxyz".split("")) {
    for (const b of "abcdefghijklmnopqrstuvwxyz".split("")) {
        for (const c of "abcdefghijklmnopqrstuvwxyz".split("")) {
            if (decipher(cipherText, a + b + c).includes(" the ")) {
                console.log(a + b + c);
            }
        }
    }
}
// This yields only one key: 'exp'

const clearASCII = toASCII(decipher(cipherText, 'exp'));
const sum = clearASCII.reduce((p,c) => p + c,0);



const end = Date.now();

console.log("Execute time: ", end - start, " The ASCII code is: ", sum);