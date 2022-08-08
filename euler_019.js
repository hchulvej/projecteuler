const start = Date.now();

let sundays = 0;

for (let y = 1901;y < 2001;y++) {
    for (const m of ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]) {
        let day = new Date("" + y + "-" + m + "-01");
        if (day.getDay() === 0) {
            sundays++;
        }
    }
}

const end = Date.now();

console.log("Execute time: ", end - start, " Number of Sundays: ", sundays);