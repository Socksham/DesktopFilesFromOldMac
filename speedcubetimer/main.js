var timer = document.getElementById("timer");
var watch = new stopWatch(timer);

var secondTime = false;

var phase = 1;

var check = true;

document.addEventListener('keydown', function(){
    if (phase == 3){
        if(event.keyCode == 32){
            if(watch.isOn){
                console.log("got here3");
                watch.stop();
                secondTime = false;
                phase = 1;
                check = true;
            }
        }
    }
    
})

document.addEventListener('keyup', function(){
    if(phase == 2){
        if(event.keyCode == 32){
            if(secondTime == true){
                if(!watch.isOn){            
                    console.log("got here1");
                    watch.reset();
                    watch.start();
                    watch.isOn = true;
                    phase = 3;
                }
            }
           secondTime = true;
        }
    }
    
})

document.addEventListener('keyup', function(){
    if(event.keyCode == 32){
        if(phase == 1){
            if(check == true){
                console.log("got here");
                new countdown;
                phase = 2;
                check = false;
            }
            
        }
    }
})