const start = Date.now();

const { readFileSync, promises: fsPromises } = require('fs');

function syncReadFile(filename) {
    const contents = readFileSync(filename, 'utf-8');

    return contents.split(/\r?\n/).map(x => Number.parseInt(x));
}

const numbers = syncReadFile('./euler_013.txt');

const first10dDigits = numbers.reduce((total, next) => total + next,0).toString().replace(".","").slice(0,10);

const end = Date.now();

console.log("Execute time: ", end - start, " Maximal product is: ", first10dDigits);