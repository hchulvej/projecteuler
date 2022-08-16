const start = Date.now();

let combinations = Array(201);
combinations.fill(0);
combinations[0] = 1;

const coins = [1,2,5,10,20,50,100,200];
const target = 200;

for (const coin of coins) {
    for (let amount = coin; amount <= target; amount++) {
        combinations[amount] += combinations[amount - coin];
    }
}


const sum = combinations[target];


const end = Date.now();

console.log("Execute time: ", end - start, " Number of different ways is: ", sum);