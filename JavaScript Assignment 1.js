console.log('**Program to find whether the year is leap year or not**');
year = 2004;
console.log('The given year is --> ' + year)
if (year % 4 === 0 && year % 100 !== 0) {
    console.log('The given year is a leap year');
}
else {
    console.log('The given year is not a leap year')
}

console.log('**Program to convert celsius to fahrenheit and vice versa**');
let outputUnit = 'fahrenheit';
let value = 37.7777;
let temp = 0;
console.log('The program is to convert to %{outputUnit}');
if (outputUnit === 'celsius') {
    temp = (5 / 9) * (value - 32);
    console.log('The temperature is ' + temp + ' F')
}
else {
    temp = (9 / 5) * (value) + 32;
    console.log('The temperature is ' + temp + ' C')

}

console.log('**Program to find the factorial of a number**');
let number = 6;
let factorial = 1;
if (number === 0) {
    console.log('The factorial value is', factorial);
}
while (number !== 0) {
    factorial = factorial * number;
    number = number - 1;
}
console.log('The factorial value is ' + factorial);
