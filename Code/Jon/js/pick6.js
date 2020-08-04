// Generate a list of 6 random numbers representing the winning tickets
const getRandomTicket = () => {
    const randomTicket = [];

    for(let i = 0; i < 6; i++) {
        const randomNum = Math.floor(Math.random() * 10);
        randomTicket.push(randomNum);
    };
    return randomTicket;
};
// 1. Start your balance at 0
const getTicketMatches = (winningTicket, randomTicket) => {
    let matches = 0

    for(let i = 0; i < winningTicket.length; i++) {
        if(winningTicket[i] === randomTicket[i]) {
            matches += 1
        } else {
            continue
        }
    };
    return matches
};

const getBalance = (getTicketMatches) => {
    let balance = 0;
    const AmountCalc = {
        0: 0,
        1: 2,
        2: 4,
        3: 6,
        4: 8,
        5: 10
    };

    let amount = AmountCalc[getTicketMatches]
    balance += amount

    return balance
};
// 2. Loop 100,000 times, for each loop:
// 3. Generate a list of 6 random numbers representing the ticket
// 4. Subtract 2 from your balance (you bought a ticket)
// 5. Find how many numbers match
// 6. Add to your balance the winnings from your matches
// 7. After the loop, print the final balance

const mainLoop = () => {
    let counter = 0;
    let balance = 0;
    const winningTicket = getRandomTicket();
    while(counter < 10) {
        let matches = getTicketMatches(winningTicket, getRandomTicket())
        let addBalance = getBalance(matches)
        balance += addBalance;

        counter += 1;
    };
    console.log(`Final balance is ${balance}`);
};
mainLoop();