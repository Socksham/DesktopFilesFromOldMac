var lat_restaurant = [42.0479158, 42.0351471, 42.0079406, 40.5545642];
var long_restaurant = [-88.0870861, -88.5711292, -88.161472, -118.0049522];

var phone_numbers = ["(847)519-1770", "(847)619-9095", "(847)891-4740", "(530)587-9814"]

var restaurant_names = ["Thai Garden", "Olive Garden", "McDonalds", "Squeeze In"]

document.addEventListener("keydown", function(e){
    if(e.keyCode == 13){
        lat_restaurant.push(document.getElementById("latitude").value);
        long_restaurant.push(document.getElementById("longitude").value);
    }
})