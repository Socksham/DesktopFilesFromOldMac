var stack;
var maxTake;
var turn;
var mode;

var marbles;
var gameStarted = false;


var gameOver = false;

var playerNum;
var compNum;

document.addEventListener("keyup", function(e) {
  if (e.keyCode == 13) {
    if (mode == "Easy") {
      playerTurnEasy();
    }else if(mode == "Hard"){
			playerTurnHard();
		}else if(mode == "DrNim"){
    	playerTakesDrNim();
    }else if(mode == "2V2"){
    	if(turn == 1){
      	playerTakesPlayer1();
      }else if(turn == 2){
      	playerTakesPlayer2();
      }
    }else{
    	document.getElementById("")
    }
		document.getElementById("text").value = "";
  }
})

function startGameEasy() {
  mode = "Easy";
  document.getElementById("background").innerHTML = "Don't take away the last marble!";
  stack = Math.floor(Math.random() * (100 - 20 + 1) + 20);
  maxTake = Math.floor(stack / 2)
  turn = Math.floor(Math.random() * (2 - 1 + 1) + 1);
	
	if (turn == 1) {
    document.getElementById("turn").innerHTML = "It is your turn first";
    document.getElementById("stack").innerHTML = "Stack: " + stack;
		document.getElementById("comp").innerHTML = "";
		document.getElementById("player").innerHTML = "";
    document.getElementById("maxTake").innerHTML = "The max you can take is: " + maxTake;
  } else {
    document.getElementById("turn").innerHTML = "It was the computer's turn first";
    document.getElementById("stack").innerHTML = stack;
		document.getElementById("comp").innerHTML = "";
		document.getElementById("player").innerHTML = "";
    document.getElementById("maxTake").innerHTML = "The max you can take is: " + maxTake;
		compTurnEasy();
  }
  
}

function playerTurnEasy() {
  playerNum = document.getElementById("text").value;
  //check maxTake here
  getMaxTake();
  document.getElementById("maxTake").innerHTML = "The max you can take is: " + maxTake;

  if(playerNum > maxTake){
  	document.getElementById("turn").innerHTML = "Your number cannot be greater than: " + maxTake;
  }else if(playerNum == 0){
  	document.getElementById("turn").innerHTML = "Your number cannot be 0";
  }else if(playerNum > 0 && playerNum <= maxTake){
  	document.getElementById("turn").innerHTML = "";

    parseInt(playerNum);
    document.getElementById("player").innerHTML = "You took out: " + playerNum;
    stack -= playerNum;
    if(checkEndGame() == false){
			turn = 2;
    	getMaxTake();
			if(mode == "Easy"){
				compTurnEasy();
			}
    	
		}else{
			document.getElementById("turn").innerHTML = "You Lost!";
			document.getElementById("stack").innerHTML = "Pick a mode";
			document.getElementById("comp").innerHTML = "";
			document.getElementById("player").innerHTML = "";
			document.getElementById("maxTake").innerHTML = "";
		}
		
    
  }else{
  	document.getElementById("turn").innerHTML = "That's not a number";
  }
}

function compTurnEasy() {
	getMaxTake();
  if(maxTake == 1){
  	compNum = 1;
  }else{
  	compNum = Math.ceil(Math.random()* maxTake);
  }
  stack -= compNum;
	
	if(checkEndGame() == false){
		turn = 1;

		getMaxTake();
		document.getElementById("maxTake").innerHTML = "The max you can take is: " + maxTake;

		display();
	}else{
		document.getElementById("turn").innerHTML = "You Won";
		document.getElementById("stack").innerHTML = "Pick a mode";
		document.getElementById("comp").innerHTML = "";
		document.getElementById("player").innerHTML = "";
		document.getElementById("maxTake").innerHTML = "";
	}
	
  
}

function checkEndGame() {
  if (stack <= 0) {
    return true;
  }else {
		return false;
	}
}

function getMaxTake() {
	if(stack == 1){
		maxTake = 1;
	}else{
		maxTake = Math.floor(stack/2);
	}
}

function display(){
	document.getElementById("stack").innerHTML = "Stack: " + stack;
	document.getElementById("comp").innerHTML = "Computer took out: " + compNum;
}

///////////////////////////////////////////////////////////////////////////////
//DrNim///////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////

function startGameDrNim(){

  mode = "DrNim";
  marbles = 12;
  gameStarted = true;
  document.getElementById("stack").innerHTML = marbles + " marbles";
  document.getElementById("background").innerHTML = "Dr.Nim is a game where you take away up to 3 marbles. You win when you take away the last marble."

}

function playerTakesDrNim(){

	if(gameStarted == true){

    var marblesPlayer = parseInt(document.getElementById("text").value);
    
    if(marblesPlayer ==  0 || marblesPlayer > 3 || marblesPlayer < 0 || isNaN(marblesPlayer) == true){
    	document.getElementById("turn").innerHTML = "Your number can only be 1, 2 or 3";
    }else{
      var marblesComp = 4 - marblesPlayer;
      var total = 4

      marbles -= total;

      displayDrNim(marblesComp);
      endGameDrNim();
    }
  }
}

function displayDrNim(marblesComp){

	document.getElementById("comp").innerHTML = "Computer took out " + marblesComp + " marbles";
	document.getElementById("stack").innerHTML = marbles + " marbles left";
  
}

function endGameDrNim(){

	if(marbles <= 0){
  
 	 	document.getElementById("turn").innerHTML = "You Lost";
    gameStarted = true;

  }
}

/////////////////////////////////////////////////////////////////////////////////
//2V2///////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////

var name1;
var name2;

function startGame2V2(){
	name1 = prompt("What is Player 1's name?")
 	name2 = prompt("What is Player 2's name?")

  mode = "2V2";
  document.getElementById("background").innerHTML = "Don't take away the last marble!";
  stack = Math.floor(Math.random() * (100 - 20 + 1) + 20);
  maxTake = Math.floor(stack / 2)
  turn = Math.floor(Math.random() * (2 - 1 + 1) + 1);
  document.getElementById("turn").innerHTML = "";
  document.getElementById("stack").innerHTML = "";
  document.getElementById("comp").innerHTML = "";
  document.getElementById("player").innerHTML = "";
  document.getElementById("maxTake").innerHTML = "";

  if (turn == 1) {
    document.getElementById("turn").innerHTML =  name1 + " is first";
    document.getElementById("stack").innerHTML = "Stack: " + stack;
    document.getElementById("comp").innerHTML = "";
    document.getElementById("player").innerHTML = "";
    document.getElementById("maxTake").innerHTML = "The max you can take is: " + maxTake;
    player1Takes();
  } else {
    document.getElementById("turn").innerHTML = name2 + " is first";
    document.getElementById("stack").innerHTML = stack;
    document.getElementById("comp").innerHTML = "";
    document.getElementById("player").innerHTML = "";
    document.getElementById("maxTake").innerHTML = "The max you can take is: " + maxTake;
    player2Takes();
  }

}

function player1Takes(){
	document.getElementById("turn").innerHTML = name1 + "'s turn";
  
}

function player2Takes(){
	
}

//////////////////////////////////////////////////////////////////
//Impossible/////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////

function startGameHard(){
	mode = "Easy";
  document.getElementById("background").innerHTML = "Don't take away the last marble! The computer always goes first.";
  stack = Math.floor(Math.random() * (100 - 20 + 1) + 20);
  maxTake = Math.floor(stack / 2)
  turn = 2;
  
  document.getElementById("turn").innerHTML = "";
  document.getElementById("stack").innerHTML = "Stack: " + stack;
  document.getElementById("comp").innerHTML = "";
  document.getElementById("player").innerHTML = "";
  document.getElementById("maxTake").innerHTML = "The max you can take is: " + maxTake;
  compTurnHard();
}

function playerTurnHard(){
	playerNum = document.getElementById("text").value;
  getMaxTake();
  if(playerNum > maxTake){
  	document.getElementById("turn").innerHTML = "Your number cannot be greater than" + maxTake;
  }else if(playerNum == 0){
  	document.getElementById("turn").innerHTML = "Your number cannot be 0";
  }else if(playerNum > 0 && playerNum <= maxTake){
  	document.getElementById("turn").innerHTML = "";

    parseInt(playerNum);
    document.getElementById("player").innerHTML = "You took out: " + playerNum;
    stack -= playerNum;
    
    if(checkEndGame() == false){
			turn = 2;
    	getMaxTake();
			compTurnHard();
		}else{
			document.getElementById("turn").innerHTML = "You Lost!";
			document.getElementById("stack").innerHTML = "Pick a mode";
			document.getElementById("comp").innerHTML = "";
			document.getElementById("player").innerHTML = "";
			document.getElementById("maxTake").innerHTML = "";
  	}
  }
}

function compTurnHard(){
	alert("got here");
  	alert("got here");

	alert("got here");

	alert("got here");

	alert("got here");


	if(63 < stack){
    var compNum = stack - 63;
    stack -= compNum;
    document.getElementById("stack").innerHTML = "Stack: " + stack;
	document.getElementById("comp").innerHTML = "Computer took out: " + compNum;
  }else if (31 < stack){
    var compNum = stack - 31;
    stack -= compNum;
  	document.getElementById("stack").innerHTML = "Stack: " + stack;
	document.getElementById("comp").innerHTML = "Computer took out: " + compNum;
  }else if(15 < stack){
    var compNum = stack - 15;
    stack -= compNum;
  	document.getElementById("stack").innerHTML = "Stack: " + stack;
	document.getElementById("comp").innerHTML = "Computer took out: " + compNum;
  }else if(7 < stack){
    var compNum = stack - 7;
    stack -= compNum;
  	document.getElementById("stack").innerHTML = "Stack: " + stack;
	document.getElementById("comp").innerHTML = "Computer took out: " + compNum;
  }else if(3 < stack){
    var numToGetTo = 3;
    var compNum = stack - numToGetTo;
    stack -= compNum;
  	document.getElementById("stack").innerHTML = "Stack: " + stack;
	document.getElementById("comp").innerHTML = "Computer took out: " + compNum;
  }else if(1 < stack){
    var numToGetTo = 1;
    var compNum = stack - numToGetTo;
		stack -= compNum;
    document.getElementById("stack").innerHTML = "Stack: " + stack;
    document.getElementById("comp").innerHTML = "Computer took out: " 			+ compNum; 
    }
  
  if(checkEndGame() == false){
		turn = 1;
    getMaxTake();
    
  }else{
  	document.getElementById("turn").innerHTML = "You Won!";
    document.getElementById("stack").innerHTML = "Pick a mode";
    document.getElementById("comp").innerHTML = "";
    document.getElementById("player").innerHTML = "";
    document.getElementById("maxTake").innerHTML = "";
  }
}