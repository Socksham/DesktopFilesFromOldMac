document.addEventListener("keydown", function(e){
    if(e.keyCode === 13){
        initMap();
        init();
        document.getElementById("foodinpounds").value = "";
    }
})

function init(){
    var foodInPounds = document.getElementById("pounds").value

    var numberofpeople = Math.floor(foodInPounds/1.2);

    document.getElementById("numberofpeople").innerHTML = numberofpeople + " people can be fed with this much food!"   
}

