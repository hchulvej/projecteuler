const start = Date.now();

// Magic 5-gon
// Five lines consisting of three numbers
// The second node is equal to the third node of the previous line
// Let n[i][j] be the j'th node of the i'th line
//
// This means:
// n[1][3] = n[2][2]
// n[2][3] = n[3][2]
// n[3][3] = n[4][2]
// n[4][3] = n[5][2]
// n[5][3] = n[1][2]

let lines = [];
for (let a = 1; a < 11; a++) {
    for (let b = 1; b < 11; b++) {
        for (let c = 1; c < 11; c++) {
            let line = [a, b, c];
            if (new Set(line).size === 3) {
                lines.push(line);
            }
        }
    }
}

let sameSumLines = new Map();
for (const line of lines) {
    const sum = line.reduce((p,c) => p + c, 0);
    if (sameSumLines.has(sum)) {
        let sslines = sameSumLines.get(sum);
        sslines.push(line);
    } else {
        sameSumLines.set(sum, []);
    }
}

let fiveGons = new Set();

for (const l1 of lines) {
    const sum = l1.reduce((p,c) => p + c, 0);
    for (const l2 of sameSumLines.get(sum)) {
        if (l1[2] === l2[1]) {
            for (const l3 of sameSumLines.get(sum)) {
                if (l2[2] === l3[1]) {
                    for (const l4 of sameSumLines.get(sum)) {
                        if (l3[2] === l4[1]) {
                            for (const l5 of sameSumLines.get(sum)) {
                                if (l4[2] === l5[1] && l5[2] === l1[1]) {
                                    if (new Set([l1, l2, l3, l4, l5].flat()).size === 10) {
                                        let minNode = Math.min(l1[0], l2[0], l3[0], l4[0], l5[0]);
                                        switch (minNode) {
                                            case l1[0]:
                                                fiveGons.add([l1, l2, l3, l4, l5]);
                                                break;
                                            case l2[0]:
                                                fiveGons.add([l2, l3, l4, l5, l1]);
                                                break;
                                            case l3[0]:
                                                fiveGons.add([l3, l4, l5, l1, l2]);
                                                break;
                                            case l4[0]:
                                                fiveGons.add([l4, l5, l1, l2, l3]);
                                                break;
                                            case l5[0]:
                                                fiveGons.add([l5, l1, l2, l3, l4]);
                                                break;
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

const fiveGonTo16digitString = (fiveGon) => {
    const str = fiveGon.flat().join("");
    if (str.length === 16) {
        return str;
    }
    return "0";
}

let max = 0;
fiveGons.forEach( (fg) => {
    max = Math.max(Number(fiveGonTo16digitString(fg)), max);
});

const end = Date.now();

console.log("Execute time: ", end - start, " Maximum 16-digit string is: ", max);