const start = Date.now();

import { readFileSync } from 'fs';
import { Permutation }  from 'js-combinatorics';

function syncReadFile(filename) {
    const contents = readFileSync(filename, 'utf-8');

    const arr = contents.split(",");

    let words = [];
    for (const element of arr) {
        words.push(element.replaceAll('"',''));
    }

    return words;
}

const wordList = syncReadFile('./euler_098.txt');

/*
    Create anagram pairs
*/
const areAnagrams = (word1, word2) => {
    if (word1 === word2) {
        return false;
    }
    return word1.split("").sort().join("") === word2.split("").sort().join("");
}

let anagramPairs = [];
let longestAnagramPair = 0;

for (let i = 0; i < wordList.length; i++) {
    const sameLengthWords = wordList.filter(x => (x.length === wordList[i].length && wordList.indexOf(x) > i));
    for (const word of sameLengthWords) {
        if (areAnagrams(wordList[i], word)) {
            anagramPairs.push([wordList[i], word]);
            longestAnagramPair = Math.max(longestAnagramPair, word.length);
        }
    }
}

anagramPairs.sort((pair1, pair2) => pair2[0].length - pair1[1].length);

console.log("Anagram pairs created. Longest words have", longestAnagramPair, "letters.");

/*
    Convert an anagramic pair to two numbers via a permutation
*/
const word2Number = (word, perm) => {
    const letters = Array.from(new Set(word.split("")));
    for (let i = 0; i < letters.length; i++) {
        word = word.replaceAll(letters[i], perm[letters[i]]);
    }
    return Number(word);
}

let squares = [];
let i = 4;
while (i * i < 10 ** longestAnagramPair) {
    squares.push(i * i);
    i++;
}

console.log("Squares created.");

/*
    (word1, square) => key
    (word2, key) => number
    check if number is square
*/
const key = (word, square) => {
    const letters = Array.from(new Set(word.split("")));
    const digits = Array.from(new Set(square.toString().split("")));
    let res = {};
    if (letters.length !== digits.length) {
        return res;
    }
    for (let i = 0; i < letters.length; i++) {
        res[letters[i]] = digits[i];
    }
    return res;
}

const word2number = (word, k) => {
    for (const e of Object.keys(k)) {
            word = word.replaceAll(e, k[e]);
    }
    return Number(word);
}

const checkPairwithSquare = (pair, square) => {
    const k = key(pair[0], square);
    if (k) {
        let temp = (" " + pair[1]).slice(1);
        for (const e of Object.keys(k)) {
            temp = temp.replaceAll(e, k[e]);
        }
        return (temp[0] !== '0' && squares.includes(Number(temp)));
    }
    return false;
}


let largestSquare = 0;

for (const pair of anagramPairs) {
    const listOfSquares = [...squares].filter(x => x.toString().length === pair[0].length);
    for (const square of listOfSquares) {
        if (checkPairwithSquare(pair, square)) {
            largestSquare = Math.max(largestSquare, square, word2number(pair[1], key(pair[0], square)));
        }
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " Largest square is: ", largestSquare);