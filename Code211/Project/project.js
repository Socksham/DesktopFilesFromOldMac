//chess board
var pawns = [];

var rooks = [];

var bishops = [];

var knights = [];

var kings = [];

var queens = [];



var board = createImage("chessboard.jpeg", "board", 0, 0);

var whiteKing;

var blackKing;

function init(){
    createPieces();
    animate()
}

function animate(){
    a = requestAnimationFrame(animate);
    drawChessBoard();
    drawPieces();
    
}

function createImage(src, title,xcoord,ycoord) {
    var img = new Image();
    img.src = src;
    img.title = title;
    img.left = xcoord;
    img.top = ycoord;

    return img;
};

function kingMoves(){
    
}


function drawChessBoard(){
    var ctx = document.getElementById("board").getContext("2d");
    ctx.drawImage(board, board.left, board.top, 600, 600);
}

function drawPieces(){
    var ctx = document.getElementById("board").getContext("2d");
    for(i = 0; i < 32; i++){
        if(i == 0){
            ctx.drawImage(kings[0], kings[0].left, kings[0].top, 70, 70);
        }else if(i == 1){
            ctx.drawImage(kings[1], kings[1].left, kings[1].top, 90, 90);
        }else if(i == 2){
            ctx.drawImage(queens[0], queens[0].left, queens[0].top, 70, 70)
        }
    }
}

function createPieces(){
    for(var i = 0; i < 32; i++){
        if(i == 0){
            kings.push(createImage("whiteking.png", "whiteking", 304, 530));
        }else if(i == 1){
            kings.push(createImage("blackking.png", "blackking", 294, -10));
        }else if(i == 2){
            queens.push(createImage("whitequeen.png", "whitequeen", 264, 530));
        }else if(i == 3){
            queens.push(createImage("blackqueen.png", "blackqueen", 264, 0));
        }
    }
    console.log(queens)
}
