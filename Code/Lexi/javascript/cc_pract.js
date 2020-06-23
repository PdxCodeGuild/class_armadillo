
    
    function validate_cc(card){
        let nums = card
        const fullNumber = nums;
        const last4Digits = fullNumber.slice(-4);
        const maskedNumber = last4Digits.padStart(fullNumber.length, '*');
        
        console.log(maskedNumber);
        let nums_list = nums.split('') 

                check_digit = nums_list.pop(-1) //4
                console.log(check_digit)


        console.log(nums_list)

        nums_list.reverse() 
        console.log(nums_list)

        nums_list = nums_list.filter((element, index) => {
            return index % 2 === 0
        })
        console.log(nums_list) 

        nums_list = nums_list.map(x => x * 2)
        console.log(nums_list) 

        nums_list = nums_list.map(function (x){ if (x>9) {return x-9} else{ return x} })
        console.log(nums_list) 

        const add = (a, b) => a+b
        nums_list = nums_list.reduce(add)
        console.log(nums_list) 

        removed =nums_list %= 10
        console.log(removed) 

        if (removed === check_digit) {
            return true
        } else {
            return false
        }
    }
    is_valid = validate_cc(nums_list)
    console.log(is_valid)

 