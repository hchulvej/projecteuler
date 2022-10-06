const start = Date.now();

// Initializing the board
const BOARD = ["GO","A1","CC1","A2","T1","R1","B1",
"CH1","B2","B3","JAIL","C1","U1","C2","C3","R2","D1",
"CC2","D2","D3","FP","E1","CH2","E2","E3","R3","F1",
"F2","U2","F3","G2J","G1","G2","CC3","G3","R4","CH3",
"H1","T2","H2"];

// Initializing the Community Chest 2/16
const CC = ["GO","JAIL","NOTHING","NOTHING","NOTHING"
,"NOTHING","NOTHING","NOTHING","NOTHING","NOTHING"
,"NOTHING","NOTHING","NOTHING","NOTHING","NOTHING","NOTHING"];

// Initializing the Chance Deck 10/16
const CHANCE = ["GO","JAIL","C1","E3","H2","R1","NEXTR",
"NEXTR","NEXTU","BACK3","NOTHING","NOTHING","NOTHING","NOTHING"
,"NOTHING","NOTHING"];

// Shuffler: Modern Fisher-Yates
const shuffle = (arr) => {
    const swap = (arr2, i1, i2) => {
        const e1 = arr2[i1];
        const e2 = arr2[i2];
        arr2[i1] = e2;
        arr2[i2] = e1;
        return arr2;
    }

    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        arr = swap(arr, i, j);
    }

    return arr;
}

// Making a die
class Die {
  constructor(sides) {
    this.sides = sides;
  }

  roll() {
    return Math.floor(Math.random() * this.sides + 1);
  }
}

// Making a game
class Game {
    constructor(board, communityChest, chanceDeck, numberOfRounds) {
        this.board = board;
        this.cc = [shuffle(communityChest), shuffle(communityChest), shuffle(communityChest)];
        this.ch = [shuffle(chanceDeck),shuffle(chanceDeck),shuffle(chanceDeck)];
        this.rounds = numberOfRounds;
        this.dieOne = new Die(4);
        this.dieTwo = new Die(4);
        this.played = 0;
        this.ccPos = [0, 0, 0]; // Top card
        this.chPos = [0, 0, 0]; // Top card
        this.counter = new Array(40).fill(0);
    }

    getCounter() {
      return this.counter;
    }

    getPlayed() {
      return this.played;
    }

    // Returns the new board position
    processCommunityChest(card, current) {
      if (card === "GO" || card === "JAIL") {
        return this.board.indexOf(card);
      }
      return current;
    }

    processChanceDeck(card, current) {
      if (card === "GO" || card === "JAIL" || card === "C1" || card === "E3" || card === "H2" || card === "R1") {
        return this.board.indexOf(card);
      }
      if (card === "BACK3") {
        return (current - 3) % 40;
      }
      if (card === "NEXTR") {
        const railways = ["R1", "R2", "R3", "R4"].map(x => this.board.indexOf(x));
        if (current >= railways[0] && current < railways[1]) {
          return this.board.indexOf("R2");
        }
        if (current >= railways[1] && current < railways[2]) {
          return this.board.indexOf("R3");
        }
        if (current >= railways[2] && current < railways[3]) {
          return this.board.indexOf("R4");
        }
        return this.board.indexOf("R1");
      }
      if (card === "NEXTU") {
        const utilities = ["U1", "U2"].map(x => this.board.indexOf(x));
        if (current >= utilities[0] && current < utilities[1]) {
          return this.board.indexOf("U2");
        }
        return this.board.indexOf("U1");
      }
      return current;
    }

    runGame() {
      let current = 0; // Begin at GO
      let consec = 0;
      while (this.played < this.rounds) {
        let roundDone = false;
        this.played++;
        const roll1 = this.dieOne.roll();
        const roll2 = this.dieTwo.roll();
        if (roll1 === roll2) {
          consec++;
        } else {
          consec = 0;
        }
        // Check for three consecutive rolls
        if (consec === 3) {
          current = this.board.indexOf("JAIL");
          consec = 0;
          roundDone = true;
        }

        if (!roundDone) {
          current = (current + roll1 + roll2) % 40;
        }
        if (!roundDone && this.board[current] === "G2J") {
            current = this.board.indexOf("JAIL");
            roundDone = true;
            this.counter[current]++;
        }
        if (!roundDone && this.board[current] === "CH1") {
          current = this.processChanceDeck(this.ch[0][this.chPos[0]], current);
          this.chPos[0] = (this.chPos[0] + 1) % 16;
        }
        if (!roundDone && this.board[current] === "CH2") {
          current = this.processChanceDeck(this.ch[1][this.chPos[1]], current);
          this.chPos[1] = (this.chPos[1] + 1) % 16;
        }
        if (!roundDone && this.board[current] === "CH3") {
          current = this.processChanceDeck(this.ch[2][this.chPos[2]], current);
          this.chPos[2] = (this.chPos[2] + 1) % 16;
        }
        if (!roundDone && this.board[current] === "CC1") {
          current = this.processCommunityChest(this.cc[0][this.ccPos[0]], current);
          this.ccPos[0] = (this.ccPos[0] + 1) % 16;
        }
        if (!roundDone && this.board[current] === "CC2") {
          current = this.processCommunityChest(this.cc[1][this.ccPos[1]], current);
          this.ccPos[1] = (this.ccPos[1] + 1) % 16;
        }
        if (!roundDone && this.board[current] === "CC3") {
          current = this.processCommunityChest(this.cc[2][this.ccPos[2]], current);
          this.ccPos[2] = (this.ccPos[2] + 1) % 16;
        }
        if (!roundDone) {
          this.counter[current]++;
        }
      }
    }
  }

const game = new Game(BOARD, shuffle(CC), shuffle(CHANCE), 1000000);

game.runGame();
const counts = game.getCounter();

let scounts = [...counts];
scounts.sort((a,b) => a - b);
let popular1 = counts.indexOf(scounts[39]);
let popular2 = counts.indexOf(scounts[38]);
let popular3 = counts.indexOf(scounts[37]);

const answer = popular1.toString().concat(popular2.toString()).concat(popular3.toString());


const end = Date.now();

console.log("Execute time: ", end - start, " The modal string is: ", answer);