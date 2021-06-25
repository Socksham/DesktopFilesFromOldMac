document.addEventListener("click", function(e){
    let mouseX = e.x;
    let mouseY = e.y;
    changeBoard(mouseX, mouseY);
})

let turn = "X"


function createBoard(){
    ctx = document.getElementById("board").getContext("2d");
    ctx.fillRect(130, 0, 20, 450);
    ctx.fillRect(280, 0, 20, 450);
    ctx.fillRect(0, 130, 450, 20);
    ctx.fillRect(0, 280, 450, 20);

}


function initialize(){
    createBoard();
}

let board = ["", "", "", "", "", "", "", "", ""]

function changeBoard(x, y){
    if(x < 130 && x > 0 && y < 130 && y > 0){
        if(board[0] == ""){
            if(turn == "X"){
                turn ="O";
            }else if(turn == "O"){
                turn = "X"
            }
            board[0] = "taken"

        }
        console.log("Box1");
    }else if(x < 280 && x > 130 && y < 130 && y > 0){
        if(board[1] == ""){
            if(turn == "X"){
                turn ="O";
            }else if(turn == "O"){
                turn = "X"
            }
            board[1] = "taken"

        }
        console.log("Box2");
    }else if(x < 450 && x > 280 && y < 130 && y > 0){
        if(board[2] == ""){
            if(turn == "X"){
                turn ="O";
            }else if(turn == "O"){
                turn = "X"
            }
            board[2] = "taken"

        }
        console.log("Box3")
    }else if(x < 130 && x > 0 && y < 280 && y > 130){
        if(board[3] == ""){
            if(turn == "X"){
                turn ="O";
            }else if(turn == "O"){
                turn = "X"
            }
            board[3] = "taken"

        }
        console.log("Box4");
    }else if(x < 280 && x > 130 && y < 280 && y > 130){
        if(board[4] == ""){
            if(turn == "X"){
                turn ="O";
            }else if(turn == "O"){
                turn = "X"
            }
            board[4] = "taken"

        }
        console.log("Box5");
    }else if(x < 450 && x > 280 && y < 280 && y > 130){
        if(board[5] == ""){
            if(turn == "X"){
                turn ="O";
            }else if(turn == "O"){
                turn = "X"
            }
            board[5] = "taken"

        }
        console.log("Box6")
    }else if(x < 130 && x > 0 && y < 450 && y > 280){
        if(board[6] == ""){
            if(turn == "X"){
                turn ="O";
            }else if(turn == "O"){
                turn = "X"
            }
            board[6] = "taken"

        }
        console.log("Box7");
    }else if(x < 280 && x > 130 && y < 450 && y > 280){
        if(board[7] == ""){
            if(turn == "X"){
                turn ="O";
            }else if(turn == "O"){
                turn = "X"
            }
            board[7] = "taken"
        }
        console.log("Box8");
    }else if(x < 450 && x > 280 && y < 450 && y > 280){
        if(board[8] == ""){
            if(turn == "X"){
                turn ="O";
            }else if(turn == "O"){
                turn = "X"
            }
        }
        board[8] = "taken"

        console.log("Box9")
    }
    console.log(turn)
}