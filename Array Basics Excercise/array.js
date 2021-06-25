var die1 = [1, 2, 3, 4, 5, 6];
var die2 = [1, 2, 3, 4, 5, 6];

var times2 = 0;
var times3 = 0;
var times4 = 0;
var times5 = 0;
var times6 = 0;
var times7 = 0;
var times8 = 0;
var times9 = 0;
var times10 = 0;
var times11 = 0;
var times12 = 0;

function randomNumber(){
    var random1 = Math.floor(Math.random()*6);
    var random2 = Math.floor(Math.random()*6);
    picker(random1, random2);
}

function picker(d1rand, d2rand){
    var die1Val = die1[d1rand];
    var die2Val = die2[d2rand];
    var addition = die1Val + die2Val;
    
    if(addition == 2){
        times2++;
    }else if(addition == 3){
        times3++;
    }else if(addition == 4){
        times4++;
    }else if(addition == 5){
        times5++;
    }else if(addition == 6){
        times6++;
    }else if(addition == 7){
        times7++;
    }else if(addition == 8){
        times8++;
    }else if(addition == 9){
        times9++;
    }else if(addition == 10){
        times10++;
    }else if(addition == 11){
        times11++;
    }else if(addition == 12){
        times12++;
    }

    display(addition);
}

function display(addition){
    document.getElementById("display").innerHTML = addition;
    document.getElementById("2").innerHTML = "2: " + times2;
    document.getElementById("3").innerHTML = "3: " + times3;
    document.getElementById("4").innerHTML = "4: " + times4;
    document.getElementById("5").innerHTML = "5: " + times5;
    document.getElementById("6").innerHTML = "6: " + times6;
    document.getElementById("7").innerHTML = "7: " + times7;
    document.getElementById("8").innerHTML = "8: " + times8;
    document.getElementById("9").innerHTML = "9: " + times9;
    document.getElementById("10").innerHTML = "10: " + times10;
    document.getElementById("11").innerHTML = "11: " + times11;
    document.getElementById("12").innerHTML = "12: " + times12;

}