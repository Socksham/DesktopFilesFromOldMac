var array = [];
var array2 = [];

function searchArray(){
    array = [];
    array2 = [];

    for(i = 0; i < 10; i++){
        var numIn = Math.floor(Math.random()*100);
        var numIn2 = Math.floor(Math.random()*100);
        array.push(numIn);
        array2.push(numIn2);
    }
    findMatches();
}

function findMatches(){
    var findMatches = [];

    for(x = 0; x<array.length; x++){
        if(array.includes(array2[x])){
            findMatches.push(array2[x]);
        }
    }
    display(findMatches);
    
}

function display(matches){
    document.getElementById("display").innerHTML = array;
    document.getElementById("display2").innerHTML = array2;
    document.getElementById("matches").innerHTML = matches;

}

