var num;
var base;
var sum;

function whichOne(){
    alert("got here");
    num = prompt("Please choose a number");
    base = prompt("What is your base?");
    binaryConverter();
}
function binaryConverter(){
    var conv = 2;
    sum = 0;
    for(i = 1; i <= num.length; i++) {
        sum += num.substring(i - 1, i) * Math.pow(conv, num.length - i);
    }
    decConverter();
}

function decConverter(){
    var string = "";
    alert(sum);
    while(sum > 0){
        var rem = 0;
        while(sum % base != 0){
            sum--;
            rem++;
        }
        sum = sum/base;
        string = rem + string;
    }
    alert(string);
}