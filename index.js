const numbers = document.querySelectorAll('.numbers');
const result = document.querySelectorAll('.result span');

let firstValue = "";
let isfirstValue = "false";
let secondValue = "";
let isSecondValue = "false";
let sign = "";
let resultValue = 0;

for(let i = 0; i < numbers.length; i++) {
    numbers[i].addEventListener('click', (e) => {let atr = e.target.getAttribute('value');
        if(isfirstValue === false) {
            getfirstValue(atr)
        }
    })
           
}

function getfirstValue(el){
    result.innerHTML = ""
    firstValue += el;
    result.innerHTML = firstValue
    firstValue = +firstValue;
}