var animals = ["GIRAFFE", "LION", "TIGER"];
var carCompanies = ["LAMBORGHINI", "FERRARI", "TOYOTA", "HONDA"]
var dollarAmounts = [5000, 500, 900, 700, 300, 800, 550, 400, 500,
600, 350, 500, 900, "BANKRUPT", 650, "FREE PLAY", 700,
"LOST A TURN",];
var characters = ["!", "@", "#", "$", "%", "^", "&", "*", "~", ":", ";", "}", "{", 
"?", "/"]
var guessedLetters = [];
var topics = [animals, carCompanies];
var gameStarted = false;
var newSpin = false;
var prize;
var stringToUse;
var stringToShow = "";
var string = "";

document.addEventListener("keyup", function(e){
    if(e.keyCode == 13){
        guessLetter();
        document.getElementById("Guess").value = "";

    }

})

function setup(){
    string = "";
    stringToShow = "";
    guessedLetters = [];
    var arrayToUse = topics[Math.floor(Math.random()*topics.length)];
    stringToUse = arrayToUse[Math.floor(Math.random()*arrayToUse.length)];
    gameStarted = true;

    console.log(stringToUse);

    for(i=0; i < stringToUse.length; i++){
        stringToShow += characters[i];
    }
    console.log(stringToShow);
}

function spin(){
    if(gameStarted == true){
        prize = dollarAmounts[Math.floor(Math.random()*dollarAmounts.length)];
        newSpin = true;
    }
}

function guessLetter(){
    var guess = document.getElementById("Guess").value;
    if(gameStarted && newSpin){
        for(i = 0;i<stringToUse.length;i++){
            if(guess.toUpperCase() == stringToUse.charAt(i).toUpperCase()){
                stringToShow.replace(stringToShow.charAt(i), guess.toUpperCase());
            }
        }
        console.log(stringToShow);
    }
}


