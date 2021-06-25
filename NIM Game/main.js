var stack;
var maxTake = Math.floor(stack/2);
var mode;

document.addEventListener("keyup", function(e){
    if(e.keyCode == 13){
        var playerInput = parseInt(Math.floor(document.getElementById("playerInput").value
        ));
        if(mode == "Impossible"){
            removeFromStackImpossible(playerInput);
        }else if(mode == "Hard"){
            removeFromStackHard(playerInput);
        }else if(mode == "Medium"){
            removeFromStackMedium(playerInput);
        }else if(mode == "Easy"){
            removeFromStackEasy(playerInput);
        }else{
            document.getElementById("playerNum").innerHTML = "Choose a mode first!";
        }
        console.log(stack);

        document.getElementById("playerInput").value = "";
    }
})

function startGameImpossible(){
    stack = Math.ceil(Math.random()* 100);
    maxTake = Math.floor(stack/2);
    mode = "Impossible";

    document.getElementById("maxTake").innerHTML = "The max you can take is: " + maxTake;
    document.getElementById("stack").innerHTML = "Stack: " + stack;
}

function startGameHard(){
    stack = Math.ceil(Math.random()* 100);
    maxTake = Math.floor(stack/2);
    mode = "Hard";

    document.getElementById("maxTake").innerHTML = "The max you can take is: " + maxTake;
    document.getElementById("stack").innerHTML = "Stack: " + stack;
}

function startGameMedium(){
    stack = Math.ceil(Math.random()* 100);
    maxTake = Math.floor(stack/2);
    mode = "Medium";

    document.getElementById("maxTake").innerHTML = "The max you can take is: " + maxTake;
    document.getElementById("stack").innerHTML = "Stack: " + stack;
}

function startGameEasy(){
    stack = Math.ceil(Math.random()* 100);
    maxTake = Math.floor(stack/2);
    mode = "Easy";

    document.getElementById("maxTake").innerHTML = "The max you can take is: " + maxTake;
    document.getElementById("stack").innerHTML = "Stack: " + stack;
}

function removeFromStackImpossible(playerNum){
    if(playerNum > maxTake){
        document.getElementById("compNum").innerHTML = "Enter a number that is less than or equal to " + maxTake;
    }else{
        
        stack -= playerNum;
        if(2**6 < stack){
            var numToGetTo = 63;
            var compNum = stack - numToGetTo;
        }else if (2**5 < stack){
            var numToGetTo = 31;
            var compNum = stack - numToGetTo;
        }else if(2**4 < stack){
            var numToGetTo = 15;
            var compNum = stack - numToGetTo;
        }else if(2**3 < stack){
            var numToGetTo = 6;
            var compNum = stack - numToGetTo;
        }else if(2**2 < stack){
            var numToGetTo = 3;
            var compNum = stack - numToGetTo;
        }else if(2**1 < stack){
            var numToGetTo = 1;
            var compNum = stack - numToGetTo;
        }else{
            maxTake = 0;
            endGame();
            return null;
        }
        stack -= compNum;
        maxTake = Math.floor(stack/2);
        display(compNum, playerNum);
    }
}

function removeFromStackEasy(playerNum){
    stack -= playerNum;
    if(maxTake > 0){
        var compNum = Math.ceil(Math.random()*maxTake);
        stack -= compNum;
        maxTake = Math.floor(stack/2);
    }else{
        maxTake = 0;
        endGame();
        return null;
    }
    display(compNum, playerNum);
}
    

function removeFromStackHard(playerNum){

}

function removeFromStackMedium(playerNum){

}

function display(compNum, playerNum){
    document.getElementById("maxTake").innerHTML = "The max you can take is: " + maxTake;
    document.getElementById("playerNum").innerHTML = "You took out: " + playerNum;
    document.getElementById("compNum").innerHTML = "Computer took out: " + compNum;
    document.getElementById("stack").innerHTML = "Stack: " + stack;
}

function endGame(){
    if(maxTake == 0){
        document.getElementById("maxTake").innerHTML = " ";
        document.getElementById("playerNum").innerHTML = " ";
        document.getElementById("compNum").innerHTML = " ";
        document.getElementById("stack").innerHTML = "You lost! Start a New Game!";
    }
    
}