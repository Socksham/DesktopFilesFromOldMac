var halloween = ["Ghost", "Pumpkin", "Witch", "Candy"];

function randomValue(){
    var halloweenRand = Math.floor(Math.random()*halloween.length);
    var value = halloween[halloweenRand];
    var valueLength = halloween[halloweenRand].length;
    var string = "";
    for(i=0; i < valueLength; i++){
        string += " _";
    }

    for (var i = 0; i < valueLength; i++) {
        alert(value.charAt(i));
    }

    alert(value);
    alert(valueLength);
    document.getElementById("underscore").innerHTML = string;

}