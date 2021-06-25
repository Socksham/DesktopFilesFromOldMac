let theme = "cat";
let model;
let previousPen = "down";
let x = null;
let y = null;
let mouseY = null;
let mouseX = null;

let strokePath;
let seedStrokes = [];
let canvas, ctx;
let width = 640;
let heigth = 480;

let mouseDown = false;

async function setup(){
    canvas = createCanvas(640, 480);
    ctx = canvas.getContext("2d");
    ctx.fillStyle("#fff");

    model = await ml5.sketchRNN(theme, modelReady);

    button = document.querySelector("#clearBtn");

    button.addEventListener("click", clearDrawing);

    canvas.addEventListener("mousemove", onMouseUpdate);
    canvas.addEventListener("mousedown", onMouseDown);
    canvas.addEventListener("mouseup", onMouseUp);

    requestAnimationFrame(draw);
}

function modelReady(){
    canvas.addEventListener("mouseup", startSketchRNN);

}

function clearDrawing(){
    clearCanvas();

    seedStrokes = [];
    model.reset();
}

function startSketchRNN(){
    x = mouseX;
    y = mouseY;

    model.generate(seedStrokes, goStroke);
}

function draw(){

    requestAnimationFrame(draw);

    if(pX == null || pY == null){
        pX = mouseX;
        pY = mouseY
    }

    if(mouseDown){
        ctx.lineWidth = 10;
        ctx.strokeStyle = "#000";

        ctx.beginPath();
        ctx.lineCap = "round";
        ctx.moveTo(mouseX, mouseY);
        ctx.lineTo(pX, pY);
        ctx.stroke();

        let userStroke = {
            dx: mouseX - pX,
            dy: mouseY - pY,
            pen: "down"
        }
    }

    

    if(strokePath){
        if(previousPen == "down"){
            ctx.beginPath();
            ctx.lineCap = "round";
            ctx.moveTo(x, y);
            ctx.lineTo(x + strokePath.dx + strokePath.dy)
        }

        x += strokePath.dx;
        y += strokePath.dy;

        previousPen = strokePath.pen;

        if(strokePath != "end"){
            strokePath = null;
            model.generate(goStroke);
        }
    }

    pX = mouseX;
    pY = mouseY;
    
}