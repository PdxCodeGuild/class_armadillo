let btnConvert = document.querySelector('button');
let input = document.querySelector('input');
let output = document.querySelector('hi');

btnConvert.addEventListener('click', () => {
    output.innerText = numberToWords.ToWords(input.value)
})