const start = Date.now();

const { readFileSync, promises: fsPromises } = require('fs');

function syncReadFile(filename) {
    const contents = readFileSync(filename, 'utf-8');

    const arr = contents.split("\n");

    return arr;
}

// An array of ten cards
const hands = syncReadFile('./euler_054.txt');

// Arrays of 5 cards
let playerOneHands = [];
let playerTwoHands = [];

for (const twoHands of hands) {
    const cards = twoHands.split(" ");
    playerOneHands.push(cards.slice(0,5));
    playerTwoHands.push(cards.slice(5));
}


// Conversion of faces and suits to values
const suits = new Map();
suits.set('S', 1);
suits.set('H', 2);
suits.set('C', 3);
suits.set('D', 4);

const faces = new Map();
for (let v = 2; v < 10; v++) {
    faces.set(v.toString(), v);
}
faces.set("T", 10);
faces.set("J", 11);
faces.set("Q", 12);
faces.set("K", 13);
faces.set("A", 14);

// The (value) signature of a hand
const signature = (hand) => {
    let sig = Array(15);
    sig.fill(0);

    for (const card of hand) {
        sig[faces.get(card[0])]++;
    }
    sig[1] = sig[14]; // Aces can be smallest and largest
    return sig;
}
// End signature

// Test for flush
const flush = (hand) => {
    let s = new Set();
    for (const card of hand) {
        s.add(suits.get(card[1]));
    }
    return s.size === 1;
}
// End test flush

// Test for straight
const straight = (hand) => {
    const sig = signature(hand);
    for (let i = 1; i < 11; i++) {
        if (sig.slice(i, i + 5).map(x => x.toString()).join("") === "11111") {
            return true;
        }
    }
    return false;
}
// End test straight

// Get high card
const highCard = (hand) => {
    let hc = 0;
    for (const card of hand) {
        hc = Math.max(faces.get(card[0]), hc);
    }
    return hc;
}
// End get high card

// Ranking signature of a hand
const ranking = (hand) => {
    let s = signature(hand);
    let r = new Map();
    for (rank of ['RF', 'SF', '4K', 'FH', 'F', 'S', '3K', '2P', '1P']) {
        r.set(rank, 0);
    }
    r.set('HC', highCard(hand));

    // Check for Royal Flush and Straight Flush
    if (flush(hand) && straight(hand)) {
        if (r.get('HC') === 14) {
            r.set('RF', 14);
        } else {
            r.set('SF', r.get('HC'));
        }
    }

    // Check for 4 of a kind
    if (s.some(x => x === 4)) {
        r.set('4K', s.indexOf(4));
    }

    // Check for Full House and three of a kind
    if (s.some(x => x === 3)) {
        if (s.some(x => x === 2)) {
            r.set('FH', [s.indexOf(3), s.indexOf(2)]);
        } else {
            r.set('3K', s.indexOf(3));
        }
    }

    // Check for Flush
    if (flush(hand)) {
        r.set('F', 1);
    }

    // Check for Straight
    if (straight(hand)) {
        r.set('S', r.get('HC'));
    }

    // Check for Two Pairs and One Pair
    let sa = [...s];
    sa[1] = 0;
    if (sa.some(x => x === 2)) {
        let firstPair = sa.indexOf(2);
        if (sa.slice(firstPair + 1).some(x => x === 2)) {
            let lastPair = sa.lastIndexOf(2);
            r.set('2P', [lastPair, firstPair]);
        } else {
            r.set('1P', firstPair);
        }
    }

    return r;
}
// End of ranking

// Compare two hands
const compare = (hand1, hand2) => {
    const r1 = ranking(hand1);
    const r2 = ranking(hand2);

    if (r1.get('RF') !== r2.get('RF')) {
        if (r1.get('RF') > r2.get('RF')) {
            //console.log("RF 1: ", hand1, hand2);
            return 1;
        } else {
            //console.log("RF 2: ", hand1, hand2);
            return 2;
        }
        
    }

    if (r1.get('SF') !== r2.get('SF')) {
        if (r1.get('SF') > r2.get('SF')) {
            //console.log("SF 1: ", hand1, hand2);
            return 1;
        } else {
            //console.log("SF 2: ", hand1, hand2);
            return 2;
        }
    }

    if (r1.get('4K') !== r2.get('4K')) {
        if (r1.get('4K') > r2.get('4K')) {
            //console.log("4K 1: ", hand1, hand2);
            return 1;
        } else {
            //console.log("4K 2: ", hand1, hand2);
            return 2;
        }
    }

    if (r1.get('FH') !== 0 || r2.get('FH') !== 0) {
        if (r1.get('FH')[0] > r2.get('FH')[0]) {
            //console.log("FH 1: ", hand1, hand2);
            return 1;
        }
        if (r1.get('FH')[0] < r2.get('FH')[0]) {
            //console.log("FH 2: ", hand1, hand2);
            return 2;
        }
        if (r1.get('FH')[1] > r2.get('FH')[1]) {
            //console.log("FH 1: ", hand1, hand2);
            return 1;
        } else {
            //console.log("FH 2: ", hand1, hand2);
            return 2;
        }
    }

    if (r1.get('F') !== 0 || r2.get('F') !== 0) {
        if (r1.get('F') > r2.get('F')) {
            //console.log("F 1: ", hand1, hand2);
            return 1;
        }
        if (r1.get('F') < r2.get('F')) {
            return 2;
        }
    }

    if (r1.get('S') !== r2.get('S')) {
        if (r1.get('S') > r2.get('S')) {
            //console.log("S 1: ", hand1, hand2);
            return 1;
        } else {
            //console.log("S 2: ", hand1, hand2);
            return 2;
        }
    }

    if (r1.get('3K') !== r2.get('3K')) {
        if (r1.get('3K') > r2.get('3K')) {
            //console.log("3K 1: ", hand1, hand2);
            return 1;
        } else {
            //console.log("3K 2: ", hand1, hand2);
            return 2;
        }
    }

    if (r1.get('2P') === 0 && r2.get('2P') !== 0) {
        return 2;
    }
    if (r1.get('2P') !== 0 && r2.get('2P') === 0) {
        return 1;
    }
    if (r1.get('2P') !== 0 && r2.get('2P') !== 0) {
        if (r1.get('2P')[0] !== r2.get('2P')[0]) {
            if (r1.get('2P')[0] > r2.get('2P')[0]) {
                return 1;
            } else {
                return 2;
            }
        } else {
            if (r1.get('2P')[1] > r2.get('2P')[1]) {
                return 1;
            } else {
                return 2;
            }
        }
    }

    if (r1.get('1P') !== r2.get('1P')) {
        if (r1.get('1P') > r2.get('1P')) {
            return 1;
        } else {
            return 2;
        }
    }

    if (r1.get('HC') !== r2.get('HC')) {
        if (r1.get('HC') > r2.get('HC')) {
            return 1;
        } else {
            return 2;
        }
    }

    return 0;
}

let playerOneWins = 0

for (let i = 0; i < 1000; i++) {
    if (compare(playerOneHands[i], playerTwoHands[i]) === 1) {
        playerOneWins++;
    }
}

console.log(playerOneHands.length);
console.log(playerTwoHands.length);

const end = Date.now();

console.log("Execute time: ", end - start, " Player 1 wins ", playerOneWins, " hands.");