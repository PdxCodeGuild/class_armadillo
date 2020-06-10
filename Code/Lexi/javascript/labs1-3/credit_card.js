<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
    
    function validate_cc(card){
        let nums = card
        //STEP 1. Convert the input string into a list of ints
        let nums_list = nums.split('') 

                //Slice off the last digit. That is the check digit.
                check_digit = nums_list.pop(-1) //4
                console.log(check_digit)

        //STEP 2. Remove last digit from list
        
        console.log(nums_list)

        //STEP 3. Reverse the digits.
        nums_list.reverse() 
        console.log(nums_list)

        //STEP 4. Get every other element in the reversed list.
        nums_list = nums_list.filter((element, index) => {
            return index % 2 === 0
        })
        console.log(nums_list) 

        //STEP 5. double it
        nums_list = nums_list.map(x => x * 2)
        console.log(nums_list) 

        //STEP 6. Subtract nine from numbers over nine.
  
        nums_list = nums_list.map(function (x){ if (x>9) {return x-9} else{ return x} })
        console.log(nums_list) 

        //STEP 7. sum all values

        const add = (a, b) => a+b
        nums_list = nums_list.reduce(add)
        console.log(nums_list) 

        //STEP 8. Remove second digit
        removed =nums_list %= 10
        console.log(removed) 

        //STEP 9. compare second digit from STEP 8 to check digit in STEP 2
        if (removed === check_digit) {
            return true
        } else {
            return false
        }
    }
    is_valid = validate_cc('5177419781721269')
    console.log(is_valid)

    </script>
</body>
</html>