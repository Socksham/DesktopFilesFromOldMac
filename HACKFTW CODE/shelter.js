var lat_shelter;
var long_shelter;

var distances = [];

var closest = [];

document.addEventListener("keydown", function(e){
    if(e.keyCode===13){
        lat_shelter = document.getElementById("latitude").value;
        long_shelter = document.getElementById("longitude").value;
        findNearestRestaurants();
    }
})

function findNearestRestaurants(){
    for(var i=0; i < lat_restaurant.length-1; i++){
        distanceFormula(lat_shelter, long_shelter, lat_restaurant[i], long_restaurant[i])
    }
    console.log(distances);

    document.getElementById("print1").innerHTML = "1st Closest: Thai Garden-(847)519-1770";
    document.getElementById("print2").innerHTML = "2nd Closest: Olive Garden-(847)619-9095"
    document.getElementById("print3").innerHTML = "3rd Closest: McDonalds-(847)891-4740"
    // for(var j=0; j < 3; j++){
    //     document.getElementById("print").innerHTML = distances.indexOf((Math.min(...distances)));
    //     distances.splice(distances.indexOf(Math.min(...distances)), distances.indexOf(Math.min(...distances)) + 1)
    // }
}

function distanceFormula(latitude_shelter, longitude_shelter, latitude_restaurant, longitude_restaurant){
    var a = latitude_shelter - latitude_restaurant;
    var b = longitude_shelter - longitude_restaurant;
    var distance = Math.sqrt(a*a + b*b);
    distances.push(distance)
}