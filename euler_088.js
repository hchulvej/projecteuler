const start = Date.now();

// The minimal product-sum number with "size" k has to satisfy
// k <= M <= 2k, so 2 <= M <= 24000
// All a_j's >= 1
// {2, k, "k - 2 1's"} shows that 2k is a product-sum number

let elements = [];

for (let n1 = 2; n1 <= 24000; n1++) {
    for (let n2 = n1; n1 * n2 <= 24000; n2++) {
        elements.push([n1, n2]);
        for (let n3 = n2; n1 * n2 * n3 <= 24000; n3++) {
            elements.push([n1, n2, n3]);
            for (let n4 = n3; n1 * n2 * n3 * n4 <= 24000; n4++) {
                elements.push([n1, n2, n3, n4]);
                for (let n5 = n3; n1 * n2 * n3 * n4 * n5 <= 24000; n5++) {
                    elements.push([n1, n2, n3, n4, n5]);
                    for (let n6 = n5; n1 * n2 * n3 * n4 * n5 * n6 <= 24000; n6++) {
                        elements.push([n1, n2, n3, n4, n5, n6]);
                        for (let n7 = n6; n1 * n2 * n3 * n4 * n5 * n6 * n7 <= 24000; n7++) {
                            elements.push([n1, n2, n3, n4, n5, n6, n7]);
                            for (let n8 = n7; n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 <= 24000; n8++) {
                                elements.push([n1, n2, n3, n4, n5, n6, n7, n8]);
                                for (let n9 = n8; n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 <= 24000; n9++) {
                                    elements.push([n1, n2, n3, n4, n5, n6, n7, n8, n9]);
                                    for (let n10 = n9; n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10 <= 24000; n10++) {
                                        elements.push([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]);
                                        for (let n11 = n10; n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10 * n11 <= 24000; n11++) {
                                            elements.push([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11]);
                                            for (let n12 = n11; n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10 * n11 * n12 <= 24000; n12++) {
                                                elements.push([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12]);
                                                for (let n13 = n12; n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10 * n11 * n12 * n13 <= 24000; n13++) {
                                                    elements.push([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13]);
                                                    for (let n14 = n13; n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10 * n11 * n12 * n13 * n14 <= 24000; n14++) {
                                                        elements.push([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14]);
                                                    }
                                                }
                                            }
                                        }
                                    }                         
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

const lengthAndProduct = (arr) => {
    const prod = arr.reduce((p,c) => p * c, 1);
    const sum = arr.reduce((p,c) => p + c, 0);
    const len = prod - sum + arr.length;
    return [len, prod];
}

let minimalPSN = Array(12001);
minimalPSN.fill(0);


for (const arr of elements) {
    const lp = lengthAndProduct(arr);
    const l = lp[0];
    const p = lp[1];
    if (l> 1 && l < 12001) {
        if (minimalPSN[l] === 0) {
            minimalPSN[l] = p;
        } else {
            minimalPSN[l] = Math.min(minimalPSN[l], p);
        }
        
    }
}


const uniquePSN = [... new Set(minimalPSN)];

const sum = uniquePSN.reduce((p,c) => p + c, 0);

const end = Date.now();

console.log("Execute time: ", end - start, " The sum of minimal product-sum numbers is: ", sum);