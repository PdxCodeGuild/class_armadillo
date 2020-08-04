const readlineSync = require('readline-sync')

class ATM {
    // Properties
    constructor(name, balance, location) {
        this.name = name;
        this.balance = balance;
        this.location = location;
        this.history = {deposits: [], withdrawels: [], recent: []};
    };
    
    // Methods
    // Withdraw dollar amount from ATM
    withdrawAmount(amount) {
        return this.balance -= amount;
    };
    
    // Deposit dollar amount
    depositAmount(amount) {
        return this.balance += amount
    };
    
    // Check balance - returns dollar amount of balance in ATM
    checkBalance() {
        console.log(`ATM balance is currently ${this.balance}`);
    };
    
    // Check History - returns list of transactions from array
    checkHistory(transaction) {
        if(!this.history[transaction]) {
            console.log('Invalid input!\nTry again!')
        }
        else if(this.history[transaction].length === 0) {
            console.log(`No ${transaction} have been made.`)
        }
        else {
            for(let item of this.history[transaction]) {
                console.log(item)
            }
        }
    };
    
    // Adds transaction to history
    addTransaction(transaction) {
        if(transaction.type === 'deposits') {
            this.history.deposits.unshift(transaction.value);
        }
        else if(transaction.type === 'withdrawels') {
            this.history.withdrawels.unshift(transaction.value);
        }
        else if(transaction.type === 'recent') {
            this.history.recent.unshift(transaction.value);
        }
    };
};

// Object instance
let randomAtm1 = new ATM("Downtown ATM", 10000, "Portland, OR");

// UX messages - any loop variables
let welcomeMsg = 'Transactions: DEPOSIT, WITHDRAWEL, BALANCE, HISTORY';
let looping = true;

// ATM loop
while(looping) {
    let askReplay = readlineSync.question('Would you like to make a transaction?(y/n): ');

    // three conditions covering user input for loop
    if(askReplay === 'y') {
        console.log(`\n${welcomeMsg}`);
        let askTransaction = readlineSync.question('What transaction would you like to do?: ').toLowerCase();

        // Calling methods - based on user input
        if(askTransaction === 'deposit') {
            let amount = Number(readlineSync.question('\nWhat dollar amount would you like to Deposit?: '));
            randomAtm1.depositAmount(amount);
            randomAtm1.addTransaction({type: askTransaction + 's', value: `Deposited ${amount}`});
            randomAtm1.addTransaction({type: 'recent', value: `Withdraw ${amount}`});
            console.log(`Your Deposit of $${amount} has been comepleted.`);
        }
        else if(askTransaction === 'withdrawel') {
            let amount = Number(readlineSync.question('What dollar amount would you like to Withdrawel?: '));
            randomAtm1.withdrawAmount(amount);
            randomAtm1.addTransaction({type: askTransaction + 's', value: `Withdraw ${amount}`});
            randomAtm1.addTransaction({type: 'recent', value: `Withdraw ${amount}`});
            console.log(`\nYour Withdraw of $${amount} has been comepleted.`);
        }
        else if(askTransaction === 'balance') {
            randomAtm1.checkBalance()
        }
        else if(askTransaction === 'history') {
            console.log('(deposits, withdrawls, recent)');
            let type = readlineSync.question('\nWhat type would you like to access?: ');
            randomAtm1.checkHistory(type);
        };
    } 
    else if(askReplay === 'n') {
        console.log('Goodebye!');
        looping = false;
    }
    else {
        console.log(`Invalid Input! ${askReplay} (y/n)`);
    };
};

