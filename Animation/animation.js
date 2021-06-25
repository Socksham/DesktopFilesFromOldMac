var ballX = 702;
var ballY = 350;

var ballRadius = 30;

var paddle1X = 100;
var paddle1Y = 220;

var ballVelocityY;
var ballVelocityX;

var paddle1Velocity;
var paddle2Velocity;

var paddle2X = 1250;
var paddle2Y = 220;

var paddle2Score = 0;
var paddle1Score = 0;

var paddle1Lose = false;
var paddle2Lose = false;

var whichWay;
var paddle1UpDown;
var paddle2UpDown;
var paddle1GotToTop = false;
var paddle2GotToTop = false;

var secondBallCall = false;

function initialize(){
    drawPaddles();
    drawCircle();
    centerLine();
}

function drawPaddles(){
    var ctx = document.getElementById("canvas").getContext("2d");

    ctx.beginPath();
    ctx.fillStyle = "#000000";
    ctx.fillRect(paddle1X, paddle1Y, 50, 275)
    ctx.stroke();

    ctx.beginPath();
    ctx.fillStyle = "#000000";
    ctx.fillRect(paddle2X, paddle2Y, 50, 275)
    ctx.stroke();
}

function centerLine(){
    var ctx = document.getElementById("canvas").getContext("2d");
    ctx.beginPath();
    ctx.fillStyle = "#000000";
    ctx.fillRect(700, 0, 5, window.innerHeight);
    ctx.stroke();

}

function drawBackground(){
    var ctx = document.getElementById("canvas").getContext("2d");
    ctx.fillStyle="#ffffff"
    ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);
}

function drawCircle(){
    var ctx = document.getElementById("canvas").getContext("2d");
    ctx.beginPath();
    ctx.arc(ballX, ballY, ballRadius, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fillStyle = "black";
    ctx.fill();
}

function animateStuff(){
    document.getElementById("start").disabled = true;
    startAnim();
}

function startAnim(){
    a=requestAnimationFrame(startAnim);
    drawBackground();
    drawPaddles();
    ballDirection();
    drawCircle();
    centerLine();
    changePaddleXY();
    checkCollisions();
    if(paddle1Lose){
        paddle1Loss();
    }else if(paddle2Lose){
        paddle2Loss();
    }
    checkWin();
    display();


}

function ballDirection(){
    if(secondBallCall == false){
        whichWay = Math.ceil(Math.random()*2); 
        ballVelocityY = Math.random()*5;
        secondBallCall = true;
        ballVelocityX = 20;
    }
    if(whichWay == 1){
        ballX += ballVelocityX;
    }else if(whichWay == 2){
        ballX -= ballVelocityX;
    }

    var up;

    if(paddle2GotToTop && paddle1GotToTop){
        up = false;
    }else{
        up = true;
    }
    console.log(ballVelocityY);

    if(up){
       ballY -= ballVelocityY;
    }else{
        ballY += ballVelocityY;
    }
}

function checkCollisions(){
    var ctx = document.getElementById("canvas").getContext("2d");
    if(ballY - ballRadius < 0){
        ballY = ballRadius;
        ballVelocityY *= -1;
    } 
    
    if(ballY + ballRadius > 670){
        ballY = 670 - ballRadius;
        ballVelocityY *= -1

    }
    
    if(ballX - 10 < 115){
        paddle2Score ++;
        paddle1Lose = true;
    }else if(ballX + 10 > 1285){
        paddle1Score++;
        paddle2Lose = true;

    }
    
    if(ballX - ballRadius < paddle1X + 50 && ballY - ballRadius < paddle1Y + 275 && ballY + ballRadius > paddle1Y){
        if(paddle1UpDown){
            ballVelocityY = Math.random()*5;
        }else{
            ballVelocityY = Math.random()*-5;
        }
        ballX += ballRadius/2;
        ballVelocityX = -ballVelocityX;
    }

    if(ballX + ballRadius > paddle2X && ballY - ballRadius < paddle2Y + 275 && ballY + ballRadius > paddle2Y){
        if(paddle2UpDown){
            ballVelocityY = Math.random()*5;
        }else{
            ballVelocityY = Math.random()*-5;
        }
        ballX -= ballRadius/2;
        ballVelocityX = -ballVelocityX;
    }
}

function resetVariables(){
    ballX = 700;
    ballY = 350;
    paddle1X = 150;
    paddle1Y = 220;
    paddle2X = 1200;
    paddle2Y = 220;
    secondBallCall = false;
    paddle2Lose = false;
    paddle1Lose = false;
}

function changePaddleXY(){
    // if(ballX > window.innerWidth/2){
    //     paddle2Y = ballY;
    // }else if(ballX < window.innerWidth/2){
    //     paddle1Y = ballY;
    // }
    previousPaddle1Y = paddle1Y;
    previousPaddle2Y = paddle2Y;

    if(paddle1GotToTop == false){
        if(paddle1Y < 0){
            paddle1GotToTop = true;
        }else{
            paddle1Velocity = -5;
        }
    }else{
        if(previousPaddle1Y < 0){
            paddle1Velocity = 5;
        }else if(paddle1Y + 275 > 670){
            paddle1Velocity  = -5;
        }
    }

    paddle1Y += paddle1Velocity;

    if(paddle2GotToTop == false){
        if(paddle2Y < 0){
            paddle2GotToTop = true;
        }else{
            paddle2Velocity = -6;
        }
    }else{
        if(previousPaddle2Y < 0){
            paddle2Velocity = 6;
        }else if(paddle2Y + 275 > 670){
            paddle2Velocity  = -6;
        }
    }

    paddle2Y += paddle2Velocity;

    if(paddle1Y - previousPaddle1Y < 0){
        paddle1UpDown = true;
    }else{
        paddle1UpDown = false;
    }

    if(paddle2Y - previousPaddle2Y < 0){
        paddle2UpDown = true;
    }else{
        paddle2UpDown = false;
    }

}


function display(){
    document.getElementById("score").innerHTML = paddle1Score + ":" + paddle2Score;
}

var angryGuy = new Image()
angryGuy.src = "justdoit.png";

function paddle1Loss(){
    var ctx = document.getElementById("canvas").getContext("2d");
    ctx.fillStyle="#ffffff"
    ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);
    
    
    if(paddle2Score == 1){
        ctx.font = "30px Arial";
        ctx.fillStyle = "blue";
        ctx.fillText("Ok", 200, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle2Score == 2){
        ctx.font = "30px Arial";
        ctx.fillStyle = "blue";
        ctx.fillText("I'm fine, no realy I am", 200, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle2Score == 3){
        ctx.font = "30px Arial";
        ctx.fillStyle = "blue";
        ctx.fillText("Ummmmmmmm", 200, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle2Score == 4){
        ctx.font = "30px Arial";
        ctx.fillStyle = "blue";
        ctx.fillText("Are you kidding me!", 200, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle2Score == 5){
        ctx.font = "30px Arial";
        ctx.fillStyle = "blue";
        ctx.fillText("This is going to be your last point", 200, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle2Score == 6){
        ctx.font = "30px Arial";
        ctx.fillStyle = "blue";
        ctx.fillText("Never Mind", 200, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle2Score == 7){
        ctx.font = "30px Arial";
        ctx.fillStyle = "blue";
        ctx.fillText("BRO!", 200, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle2Score == 8){
        ctx.font = "30px Arial";
        ctx.fillStyle = "blue";
        ctx.fillText("I actually hate this game.", 200, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle2Score == 9){
        ctx.font = "30px Arial";
        ctx.fillStyle = "blue";
        ctx.fillText("NOOOOOOOOOOOOO!", 200, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle2Score == 10){
        ctx.font = "30px Arial";
        ctx.fillStyle = "blue";
        ctx.fillText("#$^@*!", 200, 200);
        ctx.drawImage(angryGuy, 200, 200);
        document.getElementById("start").disabled = false;
        return;
    }


    window.cancelAnimationFrame(a);
    resetVariables();
    setTimeout(startAnim, 1000);

}

function paddle2Loss(){
    var ctx = document.getElementById("canvas").getContext("2d");
    ctx.fillStyle="#ffffff"
    ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);
    
    
    if(paddle1Score == 1){
        ctx.font = "30px Arial";
        ctx.fillStyle = "red";
        ctx.fillText("Ok", 900, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle1Score == 2){
        ctx.font = "30px Arial";
        ctx.fillStyle = "red";
        ctx.fillText("I'm fine, no realy I am", 900, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle1Score == 3){
        ctx.font = "30px Arial";
        ctx.fillStyle = "red";
        ctx.fillText("Ummmmmmmm", 900, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle1Score == 4){
        ctx.font = "30px Arial";
        ctx.fillStyle = "red";
        ctx.fillText("Are you kidding me!", 900, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle1Score == 5){
        ctx.font = "30px Arial";
        ctx.fillStyle = "red";
        ctx.fillText("This is going to be your last point", 900, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle1Score == 6){
        ctx.font = "30px Arial";
        ctx.fillStyle = "red";
        ctx.fillText("Never Mind", 900, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle1Score == 7){
        ctx.font = "30px Arial";
        ctx.fillStyle = "red";
        ctx.fillText("BRO!", 900, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle1Score == 8){
        ctx.font = "30px Arial";
        ctx.fillStyle = "red";
        ctx.fillText("I actually hate this game.", 900, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle1Score == 9){
        ctx.font = "30px Arial";
        ctx.fillStyle = "red";
        ctx.fillText("NOOOOOOOOOOOOO!", 900, 200);
        ctx.drawImage(angryGuy, 200, 200);
    }else if(paddle1Score == 10){
        ctx.font = "30px Arial";
        ctx.fillStyle = "red";
        ctx.fillText("#$^@*!", 900, 200);
        ctx.drawImage(angryGuy, 200, 200);
        document.getElementById("start").disabled = false;
        return;
    }


    window.cancelAnimationFrame(a);
    resetVariables();
    setTimeout(startAnim, 1000);
    
}

function checkWin(){
    if(paddle1Score == 10){
        resetVariables();
        window.cancelAnimationFrame(a);
    }else if(paddle2Score == 10){
        resetVariables();
        window.cancelAnimationFrame(a);

    }
}

function resetScore(){
    paddle1Score = 0;
    paddle2Score = 0;
    document.getElementById("start").disabled = false;
}
