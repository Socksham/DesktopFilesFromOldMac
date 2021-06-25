var animals = ["GIRAFFE", "LION", "TIGER", "SEAGULL"];
var carCompanies = ["LAMBORGHINI", "FERRARI", "TOYOTA", "HONDA", "TESLA", ];
var time = ["WATCH", "CLOCK"];

var dollarAmounts = [5000, 500, 900, 700, 300, 800, 550, 400, 500,
600, 350, 500, 900, "BANKRUPT", 650, "FREE PLAY", 700,
"LOST A TURN",];

var characters = ["!", "@", "#", "$", "%", "^", "&", "*", "~", ":", ";", "}", "{", 
"?", "/"]
var vowels = ["A", "E", "I", "O", "U"];
var guessedLetters = [];
var topics = [animals, carCompanies];
var gameStarted = false;
var newSpin = false;
var prize;
var stringToUse;
var stringToShow = "";
var turn = 1;

var second = false;

var p1Money = 0;
var p2Money = 0;
var p3Money = 0;


//CANNOT BUY A VOWEL IF THEY HAVE LESS THAN 250 DOLLARS///////////////
//TAKE AWAY MONEY EVEN IF VOWEL IS NOT IN STRING/////

document.addEventListener("keyup", function(e){
    if(e.keyCode == 13){
        guessLetter();
        document.getElementById("Guess").value = "";
    }
})

function setup(){
    fixTurn();
    newSpin = false;
    stringToShow = "";
    guessedLetters = [];
    var arrayToUse = topics[Math.floor(Math.random()*topics.length)];
    stringToUse = arrayToUse[Math.floor(Math.random()*arrayToUse.length)];
    gameStarted = true;
    document.getElementById("bank").innerHTML = "BANK";
    document.getElementById("p1Money").innerHTML = "Player 1: " + p1Money;
    document.getElementById("p2Money").innerHTML = "Player 2: " + p2Money;
    document.getElementById("p3Money").innerHTML = "Player 3: " + p3Money;

    console.log(stringToUse);

    for(i=0; i < stringToUse.length; i++){
        stringToShow += characters[i];
    }
    fixDashes();
}

function spin(){
    if(gameStarted == true && newSpin == false){
        prize = dollarAmounts[Math.floor(Math.random()*dollarAmounts.length)];
        newSpin = true;
        if(prize == "BANKRUPT"){
            newSpin = false;
            if(turn == 1){
                p1Money = 0;
                turn = 2;
            }else if(turn == 2){
                p2Money = 0;
                turn = 3;
            }else{
                p3Money = 0
                turn = 1;
            }
        }else if(prize == "LOST A TURN"){
            newSpin = false;
            if(turn == 1){
                turn = 2;
            }else if(turn == 2){
                turn = 3;
            }else{
                turn = 1;
            }
        }
        document.getElementById("prize").innerHTML = "Wheel: " + prize;
    }else{
        document.getElementById("error").innerHTML = "You have already spun the wheel!"
    }
    fixTurn();

}

function guessLetter(){
    console.log(turn);
    second = false;
    var guess = document.getElementById("Guess").value;
    if(gameStarted && newSpin){
        if(guess == ""){
            document.getElementById("error").innerHTML = "Please type in a valid argument";
            return;
        }else if(guess.toUpperCase() == stringToUse.toUpperCase()){
            document.getElementById("puzzle").innerHTML = stringToUse;
            if(turn == 1){
                p1Money += 1000;
            }else if(turn == 2){
                p2Money += 1000;
            }else{
                p3Money += 1000;
            }
            newSpin = false;
            document.getElementById("p1Money").innerHTML = "Player 1: " + p1Money;
            document.getElementById("p2Money").innerHTML = "Player 2: " + p2Money;
            document.getElementById("p3Money").innerHTML = "Player 3: " + p3Money;
            setTimeout(setup, 2000);
            return;
        }else if(guessedLetters.includes(guess)){
            document.getElementById("error").innerHTML = guess.toUpperCase() + " has already been guessed";
            if(prize != "FREE PLAY"){
                newSpin = false;
                if(turn < 3){
                    turn ++;
                }else{
                    turn = 1;
                }
            }
            return;
        }else if(guess.length > 1){
            document.getElementById("error").innerHTML = "That is the wrong guess!";
            if(prize != "FREE PLAY"){
                newSpin = false;
                if(turn == 1){
                    turn++;
                }else if(turn == 2){
                    turn++;
                }else{
                    turn = 1;
                }
            }
            return;
        }else{
            if(turn == 1){
                var playerMon = p1Money;
            }else if(turn == 2){
                var playerMon = p2Money;
            }else{
                var playerMon = p3Money;
            }
            if(checkGuess(guess.toUpperCase()) == true && playerMon >= 250 || checkGuess(guess.toUpperCase()) == false){
                document.getElementById("error").innerHTML = "";
                newSpin = false;
                var previousString = stringToShow;
                guessedLetters.push(guess);
                for(i = 0;i<stringToUse.length;i++){
                    if(guess.toUpperCase() == stringToUse.charAt(i).toUpperCase()){
                        var show = stringToShow.replace(stringToShow.charAt(i), guess.toUpperCase());
                        stringToShow = show;
                        if(checkGuess(guess.toUpperCase()) == false){
                            addMoney();
                        }else{
                            removeMoney();
                        }
                    }
                }
            }else{
                document.getElementById("error").innerHTML = "You do not have enough money to buy a vowel.";
            }
            if(stringToShow == previousString){
                if(prize != "FREE PLAY"){
                    if(vowels.includes(guess.toUpperCase())){
                        removeMoney();
                    }
                    if(turn == 1){
                        turn = 2;
                    }else if(turn == 2){
                        turn = 3;
                    }else{
                        turn = 1;
                    }
                }
                document.getElementById("error").innerHTML = guess.toUpperCase() + " was not in the puzzle"; 
            }
            if(stringToShow == stringToUse.toUpperCase()){
                document.getElementById("puzzle").innerHTML = stringToUse;
                setTimeout(setup, 4000);
                return;
            }
        }
    }else{
        document.getElementById("error").innerHTML = "Please spin the wheel"
    }
    fixTurn();
    fixDashes();
}

function fixDashes(){
    var replaceDashes = stringToShow;
    for(x=0;x<stringToShow.length; x++){
        if(characters.includes(stringToShow.charAt(x))){
            replaceDashes = replaceDashes.replace(stringToShow.charAt(x), "_");
        }
    }
    display(replaceDashes);
}

function display(toBeDisplayed){
    document.getElementById("puzzle").innerHTML = toBeDisplayed.split("").join(" ");
}

function addMoney(){
    if(prize != "FREE PLAY"){
        if(turn == 1){
            p1Money += prize;
        }else if(turn == 2){
            p2Money += prize;
        }else{
            p3Money += prize;
        }
    }
    document.getElementById("p1Money").innerHTML = "Player 1: " + p1Money;
    document.getElementById("p2Money").innerHTML = "Player 2: " + p2Money;
    document.getElementById("p3Money").innerHTML = "Player 3: " + p3Money;
}

function checkGuess(playerGuess){
    if(vowels.includes(playerGuess)){
        return true;
    }else{
        return false;
    }
}

function removeMoney(){
    if(second == false){
        if(turn == 1){
            p1Money -= 250;
        }else if(turn == 2){
            p2Money -= 250;
        }else{
            p3Money -= 250;
        }
        second = true;
        
        document.getElementById("p1Money").innerHTML = "Player 1: " + p1Money;
        document.getElementById("p2Money").innerHTML = "Player 2: " + p2Money;
        document.getElementById("p3Money").innerHTML = "Player 3: " + p3Money;
    }
    
}

function fixTurn(){
    if(turn == 1){
        document.getElementById("p1Money").style.backgroundColor = "red";
        document.getElementById("p3Money").style.backgroundColor = "";
        document.getElementById("p2Money").style.backgroundColor = "";
    }else if(turn == 2){
        document.getElementById("p1Money").style.backgroundColor = "";
        document.getElementById("p3Money").style.backgroundColor = "";
        document.getElementById("p2Money").style.backgroundColor = "red";
    }else{
        document.getElementById("p1Money").style.backgroundColor = "";
        document.getElementById("p3Money").style.backgroundColor = "red";
        document.getElementById("p2Money").style.backgroundColor = "";    
    }
}