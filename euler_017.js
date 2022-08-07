const start = Date.now();

let allTheNumbers = "";

const oneDigits = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"};
const tenToNineteen = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"};
const divisibleByTen = {20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"};

let hundreds ={};
for (const [key,value] of Object.entries(oneDigits)) {
    hundreds[key * 100] = value + " hundred";
}

let collection = {};

// 0-9
for (const [key,value] of Object.entries(oneDigits)) {
    collection[key] = value;
}

// 10-19
for (const [key,value] of Object.entries(tenToNineteen)) {
    collection[key] = value;
}

// 20-99
for (let n = 20; n < 100; n++) {
    if (n % 10 === 0) {
        collection[n] = divisibleByTen[n];
    } else {
        let rem = n % 10;
        collection[n] = divisibleByTen[n - rem] + "-" + collection[rem];
    }
}

// 100-999
for (let n = 100; n < 1000; n++) {
    if (n % 100 === 0) {
        collection[n] = collection[n / 100] + " hundred";
    } else {
        let rem = n % 100;
        collection[n] = collection[(n - rem) / 100] + " hundred and " + collection[rem];
    }
}

// 1000
collection[1000] = "one thousand";

for (const v of Object.values(collection)) {
    allTheNumbers += v;
}

const res = allTheNumbers.replaceAll(" ","").replaceAll("-","").length;

const end = Date.now();

console.log("Execute time: ", end - start, " Number of letters: ", res);