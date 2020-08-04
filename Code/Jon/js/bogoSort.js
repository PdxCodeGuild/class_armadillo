// Bogo sort algorithm

function randomNums(n) {
    let numList = [];
    for(let i = 0; i <= n-1; i++) {
        numList.push(Math.round(Math.random(100) * 100));
    }
    return numList;
}

const shuffleList = (numList) => {
    for(let i = 0; i <= numList.length-1; i++) {
        console.log(numList);
        let randomIndex = Math.round(Math.random(10) * 10);
        if(numList[i] > numList[randomIndex]) {
            numList[i], numList[randomIndex] = numList[randomIndex], numList[i]
        } else {
            continue;
        }
    }
    return numList;
}

shuffleList(randomNums(10))

// CURRETLY WORKING ON
function isSorted(numList) {
    for(let i = 0; i < numList.length; i++) {
        // let randomIndex = Math.round(Math.random(10) * 10)
        if(numList[i] <= numList[i+1]) {
            continue;
        } 
        else if(numList[i] > numList[i+1]) {
            shuffleList(randomNums(10));
        } else {
            return false
        }
    }
    return true;
}

console.log(isSorted([4,3,4]))




const bogoSort = () => {
    let tries = 0;
    while(isSorted(shuffleList(randomNums(10))) != true) {
        isSorted(shuffleList(randomNums(10)));
        tries ++;
    }
    
    console.log(`Sorted in ${tries}`)
}

// bogoSort()

// Write a function to combine two lists of equal length into one, alternating elements.

function combineLists(list1, list2) {
    const newList = [];
    for(let i = 0; i < list1.length; i++) {
        newList.push(list1[i], list2[i]);
    }
    return newList;
};

// console.log(combineLists([1,3,5],[2,4,6]));


// Given a list of numbers, and a target number, find pair of numbers from the list that sum to a target number. 
// Optional return a list of all pairs of numbers that sum to a target number

const findPairs = (nums, target) => {
    const output = [];
    for(let i = 0; i < nums.length; i++) {
        console.log(nums[i])
        for(let j = 1; j < nums.length; j++) {
            if(nums.indexOf(nums[i]) === nums.indexOf(nums[j])) {
                continue
            }
            // console.log(nums[j])
            if(nums[i] + nums[j] === target) {
                output.unshift([nums[i], nums[j]]);
            }
        };
    };
    return output;
};

// console.log(findPairs([5,6,2,3], 9));

const findPairs1 = (nums, target) => {
    let newNums = nums.reduce((x,y) => {
        return (x+y===target) ? [x,y] : 'No' 
    })
    console.log(newNums)
};

// console.log(findPairs1([5,4,2,3], 9));
// let nums = [1,2,3,4]

// let newNums = nums.reduce((x,y) => {
//     return x+y
// })

// console.log(newNums)


// random list of numbers
const randomList = (n) => {
    const numList = [];
    for(let i = 0; i < n; i++) {
        let randomNum = Math.floor(Math.random() * 100);
        numList.unshift(randomNum);
    };
    return numList;
};

const bogoSort = (numList) => {
    for(let i = 0; i < numList.length; i++) {
        let iteration1 = Math.floor(Math.random() * numList.length);
        // let iteration2 = Math.floor(Math.random() * numList.length);
        [numList[i], numList[iteration1]] = [numList[iteration1], numList[i]]
    }
    return numList;
};


const isSorted = (numList) => {
    for(let i = 0; i < numList.length; i++) {
        // console.log(numList)
        if(numList[i] < numList[i+1]) {
            continue;
        }
        else if (numList[i] > numList[i+1]) {
            return false;
        }
    };
    return true;
};


const testLoop = (numList) => {
    let counter = 0;
    while(!isSorted(numList)) {
        // console.log(`Iteration ${counter}`)
        counter++;
        bogoSort(numList)
    };
    console.log(`Sorted! ${numList} in ${counter} tries`);
};

// testLoop(randomList(4));