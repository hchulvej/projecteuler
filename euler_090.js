const start = Date.now();

// Inputs are arrays of 6 numbers between 0-9
const checkArrays = (arr1, arr2) => {
    //Check 1
    const hasOne = (arr1.includes(0) && arr2.includes(1)) || (arr1.includes(1) && arr2.includes(0));

    //Check 4
    const hasFour = (arr1.includes(0) && arr2.includes(4)) || (arr1.includes(4) && arr2.includes(0));

    //Check 9
    const hasNine = (arr1.includes(0) && arr2.includes(6)) || (arr1.includes(6) && arr2.includes(0)) || (arr1.includes(0) && arr2.includes(9)) || (arr1.includes(9) && arr2.includes(0));

    //Check 16
    const hasSixteen = (arr1.includes(1) && arr2.includes(6)) || (arr1.includes(6) && arr2.includes(1)) || (arr1.includes(1) && arr2.includes(9)) || (arr1.includes(9) && arr2.includes(1));

    //Check 25
    const hasTwentyFive = (arr1.includes(2) && arr2.includes(5)) || (arr1.includes(5) && arr2.includes(2));

    //Check 36
    const hasThirtySix = (arr1.includes(3) && arr2.includes(6)) || (arr1.includes(6) && arr2.includes(3)) || (arr1.includes(3) && arr2.includes(9)) || (arr1.includes(9) && arr2.includes(3));

    //Check 49
    const hasFortyNine = (arr1.includes(4) && arr2.includes(6)) || (arr1.includes(6) && arr2.includes(4)) || (arr1.includes(4) && arr2.includes(9)) || (arr1.includes(9) && arr2.includes(4));

    //Check 64
    const hasSixtyFour = hasFortyNine;

    //Check 81
    const hasEightyOne = (arr1.includes(1) && arr2.includes(8)) || (arr1.includes(8) && arr2.includes(1));

    return hasOne && hasFour && hasNine && hasSixteen && hasTwentyFive && hasThirtySix && hasFortyNine && hasSixtyFour && hasEightyOne;
}

const countAsOne = (arr1, arr2) => {
  let str1 = arr1.toString();
  let str2 = arr2.toString();
  if (str1.replaceAll("6", "9") === str2 || str1.replaceAll("9", "6") === str2) {
    return true;
  }
  return false;
}

const allArrays = () => {
  let arrays = [];
  for (let a = 0; a < 10; a++) {
    for (let b = a + 1; b < 10; b++) {
      for (let c = b + 1; c < 10; c++) {
        for (let d = c + 1; d < 10; d++) {
          for (let e = d + 1; e < 10; e++) {
            for (let f = e + 1; f < 10; f++) {
              arrays.push([a, b, c, d, e, f]);
            }
          }
        }
      }
    }
  }
  return arrays;
};

const cube1 = allArrays();
const cube2 = allArrays();

let validArrangements = 0;

for (let i = 0; i < cube1.length; i++) {
    for (let j = i + 1; j < cube2.length; j++) {
        if (cube1[i].toString() !== cube2[j].toString() && !countAsOne(cube1[i], cube2[j]) && checkArrays(cube1[i], cube2[j])) {
            validArrangements++;
        }
    }
}


const end = Date.now();

console.log("Execute time: ", end - start, " The number of distinct arrangements is: ", validArrangements);