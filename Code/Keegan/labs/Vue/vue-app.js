

let numberToPhrase = new Vue({
    el: '#vue-container',
    data: {
        num_names: {
            0: {
                0: 'zero',
                1: 'one',
                2: 'two',
                3: 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7: 'seven',
                8: 'eight',
                9: 'nine'
            },
            1: {
                1: 'eleven',
                2: 'twelve',
                3: 'thirteen',
                4: 'fourteen',
                5: 'fifteen',
                6: 'sixteen',
                7: 'seventeen',
                8: 'eighteen',
                9: 'nineteen'
            },
            2: 'twenty',
            3: 'thirty',
            4: 'fourty',
            5: 'fifty',
            6: 'sixty',
            7: 'seventy',
            8: 'eighty',
            9: 'ninety'
        },
        userNumber: 0,
        result: 'zero'
    },
    methods: {

        getHundreds: function(number){
            return Math.floor(number / 100)
        },
    
        getTens: function(number){
            return Math.floor(number / 10) % 10
        },
    
        getOnes: function(number){
            return number % 10
        },
    
        getPhrase: function(number){
            let hundreds = this.getHundreds(number);
            let tens     = this.getTens(number);
            let ones     = this.getOnes(number);
        
            let phrase = ''
    
            if(hundreds > 0){
                phrase += this.num_names[0][hundreds] + ' hundred '
            }

            if(tens < 2){
                phrase += this.num_names[tens][ones]
            } else if(tens > 1){
                phrase += this.num_names[tens]
                if(ones > 0){
                    phrase += '-' + this.num_names[0][ones]
                }
            }
            return phrase

        },
    
        updateResult: function(){
            if(this.userNumber === '') {
                this.result = 'zero';
            }
            if(this.userNumber < 0 || this.userNumber > 999){
                this.result = 'Please enter a number 0-999'
            } else {
                this.result = this.getPhrase(this.userNumber)
            }
        }
    }
});