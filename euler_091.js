const start = Date.now();

const arePerpendicular = (v1, v2) => {
    if ((v1[0] === 0 && v1[1] === 0) || (v2[0] === 0 && v2[1] === 0)) {
        return false;
    }
    return v1[0] * v2[0] + v1[1] * v2[1] === 0;
}

const formsRightTriangle = (x1, y1, x2, y2) => {
    const v1 = [x1, y1];
    const v2 = [x2, y2];
    const v3 = [x2 - x1, y2 - y1];
    return arePerpendicular(v1, v2) || arePerpendicular(v1, v3) || arePerpendicular(v2, v3);
}

let rightTriangles = 0;

for (let x1 = 0; x1 < 51; x1++) {
    for (let x2 = x1; x2 < 51; x2++) {
        for (let y1 = 0; y1 < 51; y1++) {
            for (let y2 = 0; y2 < 51; y2++) {
                if (formsRightTriangle(x1, y1, x2, y2)) {
                    rightTriangles++;
                    if (x1 === x2 && y1 > y2) {
                        rightTriangles--;
                    }
                }
            }
        }
    }
}



const end = Date.now();

console.log("Execute time: ", end - start, " The number of right triangles is: ", rightTriangles);